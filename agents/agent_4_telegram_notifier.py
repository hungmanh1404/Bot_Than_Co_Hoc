"""
Agent 4: Sứ Giả Telegram (The Telegram Notifier)
Formats and sends the final forecast message
"""

import random
from datetime import datetime
from core.constants import ELEMENT_COLORS


class TelegramNotifierAgent:
    """Agent responsible for formatting and preparing Telegram messages"""
    
    def __init__(self):
        """Initialize the Telegram Notifier Agent"""
        pass
    
    def analyze(
        self,
        data_collector_result: dict,
        metaphysical_result: dict,
        dev_strategist_result: dict
    ) -> dict:
        """
        Compile all agent results into a beautiful Telegram message
        
        Args:
            data_collector_result: Output from Agent 1
            metaphysical_result: Output from Agent 2
            dev_strategist_result: Output from Agent 3
            
        Returns:
            Formatted message and metadata
        """
        # Generate lucky color
        dominant_element = data_collector_result["element_can"]
        lucky_color = self._get_lucky_color(dominant_element)
        
        # Format the complete message
        message = self._format_message(
            data_collector_result=data_collector_result,
            metaphysical_result=metaphysical_result,
            dev_strategist_result=dev_strategist_result,
            lucky_color=lucky_color
        )
        
        # Compile result
        result = {
            "message": message,
            "lucky_color": lucky_color,
            "luck_score": metaphysical_result["luck_score"],
            "agent": "TelegramNotifierAgent",
            "timestamp": datetime.now().isoformat()
        }
        
        return result
    
    def _format_message(
        self,
        data_collector_result: dict,
        metaphysical_result: dict,
        dev_strategist_result: dict,
        lucky_color: str
    ) -> str:
        """
        Format the complete Telegram message
        
        Returns:
            Markdown-formatted message string
        """
        # Extract data
        solar_date = data_collector_result["solar_formatted"]
        lunar_date = data_collector_result["lunar_formatted"]
        can_chi = data_collector_result["can_chi"]
        personal_day_number = data_collector_result["personal_day_number"]
        luck_score = metaphysical_result["luck_score"]
        menh_state = metaphysical_result["menh_state"]
        should_do = dev_strategist_result["should_do"]
        should_avoid = dev_strategist_result["should_avoid"]
        cosmic_message = dev_strategist_result["cosmic_message"]
        
        # Build message
        message = f"""🔮 *BẢN TIN THIÊN CƠ CHO NGUYỄN HÙNG MẠNH*
📅 *Dự báo cho ngày:* {solar_date} ({lunar_date} - {can_chi})

📊 *Chỉ số năng lượng:*
• Thần số học ngày cá nhân: Số *{personal_day_number}*
• Độ may mắn: *{luck_score}/10* {"⭐" * min(luck_score, 10)}
• Trạng thái mệnh Kim (Tân Tỵ): *{menh_state}*

✅ *NÊN LÀM (Good Commit):*
"""
        
        for item in should_do:
            message += f"• {item}\n"
        
        message += f"\n❌ *NÊN TRÁNH (Bad Request):*\n"
        
        for item in should_avoid:
            message += f"• {item}\n"
        
        message += f"""
💡 *LỜI NHẮN VŨ TRỤ (Daily Log):*
"{cosmic_message}"

🎯 *Màu may mắn:* `{lucky_color}`
"""
        
        return message.strip()
    
    def _get_lucky_color(self, element: str) -> str:
        """
        Get lucky color hex code based on the dominant element
        
        Args:
            element: Element name (Hỏa, Thủy, Mộc, Kim, Thổ)
            
        Returns:
            Hex color code
        """
        colors = ELEMENT_COLORS.get(element, ["#808080"])  # Default to gray
        return random.choice(colors)
    
    def get_preview(self, data: dict) -> str:
        """
        Get a preview of the message
        
        Args:
            data: Result from analyze()
            
        Returns:
            Message preview
        """
        return data["message"]
