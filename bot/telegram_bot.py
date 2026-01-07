"""
Telegram Bot for Thiên Cơ Đại Tướng Quân
Handles commands and message sending
"""

import logging
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode

from config.settings import settings
from core.lunar_calendar import parse_date_string, get_vietnam_datetime
from bot.scheduler import ForecastScheduler

logger = logging.getLogger(__name__)


class TelegramBot:
    """Telegram Bot for Feng Shui forecasts"""
    
    def __init__(self):
        """Initialize the Telegram Bot"""
        self.application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
        self.scheduler = None
        
        # Register command handlers
        self.application.add_handler(CommandHandler("start", self.cmd_start))
        self.application.add_handler(CommandHandler("help", self.cmd_help))
        self.application.add_handler(CommandHandler("dubao", self.cmd_dubao))
        self.application.add_handler(CommandHandler("ngaymai", self.cmd_ngaymai))
    
    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        welcome_message = """
🔮 *Chào mừng đến với Thiên Cơ Đại Tướng Quân!*

Hệ thống AI chuyên về Phong Thủy Bát Tự và Thần Số Học, phục vụ riêng cho *Nguyễn Hùng Mạnh*.

*🎯 Các lệnh có sẵn:*
• `/dubao DD/MM/YYYY` - Xem dự báo cho một ngày cụ thể
  Ví dụ: `/dubao 08/01/2026`

• `/ngaymai` - Xem dự báo cho ngày mai

• `/help` - Xem hướng dẫn

📅 *Tự động:*
Mỗi ngày lúc 8:00 PM, bạn sẽ nhận được bản tin dự báo cho ngày hôm sau.

⚡ *Powered by 4-Agent AI System*
Kết hợp Bát Tự truyền thống + Thần số học hiện đại + Developer mindset
"""
        await update.message.reply_text(
            welcome_message,
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def cmd_help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_message = """
📖 *HƯỚNG DẪN SỬ DỤNG*

*1️⃣ Xem dự báo cho một ngày:*
`/dubao DD/MM/YYYY`
Ví dụ: `/dubao 15/01/2026`

*2️⃣ Xem dự báo cho ngày mai:*
`/ngaymai`

*3️⃣ Hiểu bản tin:*
• *Độ may mắn (1-10):* Chỉ số tổng hợp từ Bát Tự và Thần số học
• *Trạng thái mệnh:* Vượng/Tướng/Hưu/Tù/Tử dựa trên mùa
• *NÊN LÀM:* Những việc có lợi theo phong thủy
• *NÊN TRÁNH:* Những việc nên cẩn thận
• *Lời nhắn vũ trụ:* Insight sâu sắc từ AI

*🔮 Hệ thống 4 Agent:*
1. Thám Tử Thời Gian - Chuyển đổi lịch
2. Thầy Phán Bát Tự - Phân tích phong thủy
3. Quân Sư Code Dạo - Tư vấn cho Dev
4. Sứ Giả Telegram - Format tin nhắn

💡 *Tips:* Dự báo dựa trên Can Chi, Ngũ Hành, và năng lượng cá nhân. Hãy dùng như tham khảo, không phải chân lý tuyệt đối!
"""
        await update.message.reply_text(
            help_message,
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def cmd_dubao(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handle /dubao command
        Usage: /dubao DD/MM/YYYY
        """
        try:
            # Check if date argument is provided
            if not context.args or len(context.args) == 0:
                await update.message.reply_text(
                    "❌ *Cách dùng:* `/dubao DD/MM/YYYY`\n"
                    "Ví dụ: `/dubao 08/01/2026`",
                    parse_mode=ParseMode.MARKDOWN
                )
                return
            
            # Parse date
            date_str = context.args[0]
            target_date = parse_date_string(date_str)
            
            # Send "processing" message
            processing_msg = await update.message.reply_text("🔮 Đang tính toán năng lượng vũ trụ...")
            
            # Generate forecast
            message = await self.scheduler.run_agent_chain(target_date)
            
            # Delete processing message and send result
            await processing_msg.delete()
            await update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
            
        except ValueError as e:
            await update.message.reply_text(
                f"❌ Lỗi: {str(e)}\n"
                "Vui lòng dùng định dạng: `/dubao DD/MM/YYYY`",
                parse_mode=ParseMode.MARKDOWN
            )
        except Exception as e:
            logger.error(f"Error in /dubao command: {e}", exc_info=True)
            await update.message.reply_text(
                f"❌ Có lỗi xảy ra: {str(e)}"
            )
    
    async def cmd_ngaymai(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /ngaymai command - forecast for tomorrow"""
        try:
            # Get tomorrow's date
            now = get_vietnam_datetime()
            tomorrow = now + timedelta(days=1)
            
            # Send "processing" message
            processing_msg = await update.message.reply_text("🔮 Đang dự báo cho ngày mai...")
            
            # Generate forecast
            message = await self.scheduler.run_agent_chain(tomorrow)
            
            # Delete processing message and send result
            await processing_msg.delete()
            await update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
            
        except Exception as e:
            logger.error(f"Error in /ngaymai command: {e}", exc_info=True)
            await update.message.reply_text(
                f"❌ Có lỗi xảy ra: {str(e)}"
            )
    
    async def send_message_to_user(self, message: str):
        """
        Send a message to the configured user
        
        Args:
            message: Message text (Markdown formatted)
        """
        try:
            await self.application.bot.send_message(
                chat_id=settings.TELEGRAM_CHAT_ID,
                text=message,
                parse_mode=ParseMode.MARKDOWN
            )
            logger.info("Message sent to user successfully")
        except Exception as e:
            logger.error(f"Error sending message to user: {e}", exc_info=True)
            raise
    
    async def start(self):
        """Start the bot"""
        # Initialize and start the scheduler
        self.scheduler = ForecastScheduler(self)
        self.scheduler.start()
        
        # Initialize the application
        await self.application.initialize()
        await self.application.start()
        
        # Start polling (compatible with v21)
        await self.application.updater.start_polling(
            allowed_updates=Update.ALL_TYPES,
            drop_pending_updates=True
        )
        
        logger.info("Telegram bot started successfully")
    
    async def stop(self):
        """Stop the bot"""
        if self.scheduler:
            self.scheduler.stop()
        
        # Stop polling and shutdown
        if self.application.updater and self.application.updater.running:
            await self.application.updater.stop()
        
        await self.application.stop()
        await self.application.shutdown()
        
        logger.info("Telegram bot stopped")
