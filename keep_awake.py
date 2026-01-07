"""
Anti-Sleep Service - Keeps the bot awake by pinging health endpoint
This script should be run on a separate service or locally
"""

import asyncio
import aiohttp
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class KeepAwakeService:
    """Service to ping health endpoint and keep bot awake"""
    
    def __init__(self, bot_url: str, interval_minutes: int = 10):
        """
        Initialize the keep-awake service
        
        Args:
            bot_url: Base URL of the bot (e.g., https://your-app.onrender.com)
            interval_minutes: How often to ping (default 10 minutes)
        """
        self.bot_url = bot_url.rstrip('/')
        self.health_endpoint = f"{self.bot_url}/health"
        self.interval_seconds = interval_minutes * 60
        self.running = False
    
    async def ping_health(self):
        """Ping the health endpoint"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.health_endpoint, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        logger.info(f"✅ Bot is awake! Status: {data.get('status', 'unknown')}")
                        return True
                    else:
                        logger.warning(f"⚠️ Unexpected status code: {response.status}")
                        return False
        except asyncio.TimeoutError:
            logger.error("❌ Timeout while pinging bot")
            return False
        except Exception as e:
            logger.error(f"❌ Error pinging bot: {e}")
            return False
    
    async def run(self):
        """Run the keep-awake service"""
        self.running = True
        logger.info(f"🚀 Keep-Awake service started")
        logger.info(f"📍 Target: {self.health_endpoint}")
        logger.info(f"⏰ Interval: {self.interval_seconds / 60} minutes")
        
        ping_count = 0
        
        while self.running:
            ping_count += 1
            logger.info(f"🔔 Ping #{ping_count} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            success = await self.ping_health()
            
            if success:
                logger.info(f"✅ Ping #{ping_count} successful")
            else:
                logger.error(f"❌ Ping #{ping_count} failed")
            
            # Wait for next interval
            logger.info(f"😴 Sleeping for {self.interval_seconds / 60} minutes...")
            await asyncio.sleep(self.interval_seconds)
    
    def stop(self):
        """Stop the service"""
        logger.info("🛑 Stopping keep-awake service...")
        self.running = False


async def main():
    """Main function"""
    # IMPORTANT: Replace this with your actual Render.com URL
    BOT_URL = "https://tuongphongthuy.onrender.com"  # Change this!
    
    # Ping every 10 minutes (Render free tier sleeps after 15 minutes of inactivity)
    service = KeepAwakeService(bot_url=BOT_URL, interval_minutes=10)
    
    try:
        await service.run()
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received")
        service.stop()


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════╗
║          🔮 Thiên Cơ Đại Tướng Quân - Keep Awake           ║
╚══════════════════════════════════════════════════════════════╝

⚠️  CHÚ Ý: Đổi BOT_URL thành URL thực của bạn trên Render!

Hoặc tốt hơn: Dùng dịch vụ MIỄN PHÍ như cron-job.org
(Xem file DEPLOY_GUIDE.md để biết cách setup)
""")
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Service stopped by user")
