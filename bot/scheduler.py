"""
Scheduler for daily automatic forecast sending
Uses APScheduler to trigger at 8 PM Vietnam time
"""

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
import logging
from datetime import datetime, timedelta

from config.settings import settings
from core.lunar_calendar import get_vietnam_datetime
from agents.agent_1_data_collector import DataCollectorAgent
from agents.agent_2_metaphysical import MetaphysicalAnalystAgent
from agents.agent_3_dev_strategist import DevStrategistAgent
from agents.agent_4_telegram_notifier import TelegramNotifierAgent

logger = logging.getLogger(__name__)


class ForecastScheduler:
    """Scheduler for automatic daily forecasts"""
    
    def __init__(self, telegram_bot):
        """
        Initialize the scheduler
        
        Args:
            telegram_bot: TelegramBot instance for sending messages
        """
        self.telegram_bot = telegram_bot
        self.scheduler = AsyncIOScheduler()
        self.timezone = pytz.timezone(settings.TIMEZONE)
        
        # Initialize agents
        self.agent1 = DataCollectorAgent(
            user_birth_day=settings.USER_BIRTH_DAY,
            user_birth_month=settings.USER_BIRTH_MONTH
        )
        
        self.agent2 = MetaphysicalAnalystAgent(
            user_element=settings.USER_ELEMENT,
            user_branch=settings.USER_BRANCH,
            user_life_path=settings.get_life_path_number()
        )
        
        self.agent3 = DevStrategistAgent()
        self.agent4 = TelegramNotifierAgent()
    
    def start(self):
        """Start the scheduler"""
        # Schedule daily forecast at configured hour (default 8 PM)
        trigger = CronTrigger(
            hour=settings.SCHEDULE_HOUR,
            minute=0,
            timezone=self.timezone
        )
        
        self.scheduler.add_job(
            self.send_daily_forecast,
            trigger=trigger,
            id='daily_forecast',
            name='Daily Feng Shui Forecast',
            replace_existing=True
        )
        
        self.scheduler.start()
        logger.info(f"Scheduler started. Daily forecast will be sent at {settings.SCHEDULE_HOUR}:00 {settings.TIMEZONE}")
    
    def stop(self):
        """Stop the scheduler"""
        self.scheduler.shutdown()
        logger.info("Scheduler stopped")
    
    async def send_daily_forecast(self):
        """
        Generate and send daily forecast for TOMORROW
        Called automatically by the scheduler
        """
        try:
            # Get tomorrow's date
            now = get_vietnam_datetime()
            tomorrow = now + timedelta(days=1)
            
            logger.info(f"Generating forecast for {tomorrow.strftime('%d/%m/%Y')}")
            
            # Run the 4-agent chain
            message = await self.run_agent_chain(tomorrow)
            
            # Send to Telegram
            await self.telegram_bot.send_message_to_user(message)
            
            logger.info("Daily forecast sent successfully")
            
        except Exception as e:
            logger.error(f"Error sending daily forecast: {e}", exc_info=True)
            # Optionally send error notification to user
            await self.telegram_bot.send_message_to_user(
                f"❌ Lỗi khi tạo bản tin: {str(e)}"
            )
    
    async def run_agent_chain(self, target_date: datetime) -> str:
        """
        Run the 4-agent chain sequentially
        
        Args:
            target_date: Date to generate forecast for
            
        Returns:
            Formatted Telegram message
        """
        # Agent 1: Data Collection
        logger.info("Running Agent 1: Data Collector")
        data_result = self.agent1.analyze(target_date)
        
        # Agent 2: Metaphysical Analysis
        logger.info("Running Agent 2: Metaphysical Analyst")
        meta_result = self.agent2.analyze(data_result)
        
        # Agent 3: Dev Strategy
        logger.info("Running Agent 3: Dev Strategist")
        dev_result = self.agent3.analyze(data_result, meta_result)
        
        # Agent 4: Telegram Formatting
        logger.info("Running Agent 4: Telegram Notifier")
        telegram_result = self.agent4.analyze(data_result, meta_result, dev_result)
        
        return telegram_result["message"]
