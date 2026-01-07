"""
Main entry point for Thiên Cơ Đại Tướng Quân
Starts the Telegram bot, scheduler, and health check server
"""

import asyncio
import logging
import signal
from aiohttp import web

from config.settings import settings
from bot.telegram_bot import TelegramBot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class HealthCheckServer:
    """Simple HTTP server for health checks (required for Render.com)"""
    
    def __init__(self, port: int):
        """Initialize health check server"""
        self.port = port
        self.app = web.Application()
        self.app.router.add_get('/health', self.health_check)
        self.app.router.add_get('/', self.root)
        self.runner = None
    
    async def health_check(self, request):
        """Health check endpoint"""
        return web.json_response({
            "status": "healthy",
            "service": "Thiên Cơ Đại Tướng Quân",
            "version": "1.0.0"
        })
    
    async def root(self, request):
        """Root endpoint"""
        return web.Response(text="🔮 Thiên Cơ Đại Tướng Quân is running!")
    
    async def start(self):
        """Start the health check server"""
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '0.0.0.0', self.port)
        await site.start()
        logger.info(f"Health check server started on port {self.port}")
    
    async def stop(self):
        """Stop the health check server"""
        if self.runner:
            await self.runner.cleanup()
        logger.info("Health check server stopped")


class Application:
    """Main application"""
    
    def __init__(self):
        """Initialize the application"""
        self.telegram_bot = None
        self.health_server = None
        self.running = False
    
    async def start(self):
        """Start all services"""
        try:
            # Validate settings
            settings.validate()
            logger.info("Configuration validated successfully")
            
            # Start health check server
            self.health_server = HealthCheckServer(settings.PORT)
            await self.health_server.start()
            
            # Start Telegram bot
            logger.info("Starting Telegram bot...")
            self.telegram_bot = TelegramBot()
            await self.telegram_bot.start()
            
            self.running = True
            logger.info("✅ All services started successfully!")
            logger.info(f"📅 Daily forecasts will be sent at {settings.SCHEDULE_HOUR}:00 {settings.TIMEZONE}")
            logger.info("🤖 Bot is ready to receive commands")
            
            # Keep running
            while self.running:
                await asyncio.sleep(1)
                
        except Exception as e:
            logger.error(f"Error starting application: {e}", exc_info=True)
            await self.stop()
            raise
    
    async def stop(self):
        """Stop all services"""
        logger.info("Shutting down...")
        self.running = False
        
        if self.telegram_bot:
            await self.telegram_bot.stop()
        
        if self.health_server:
            await self.health_server.stop()
        
        logger.info("✅ Shutdown complete")
    
    def handle_signal(self, sig):
        """Handle shutdown signals"""
        logger.info(f"Received signal {sig}, initiating shutdown...")
        self.running = False


async def main():
    """Main function"""
    app = Application()
    
    # Setup signal handlers
    loop = asyncio.get_event_loop()
    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(
            sig, 
            lambda s=sig: app.handle_signal(s)
        )
    
    try:
        await app.start()
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received")
    finally:
        await app.stop()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Application stopped by user")
