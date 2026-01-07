"""
Agent 1: Thám Tử Thời Gian (The Data Collector)
Converts Gregorian date to Lunar calendar, calculates Can Chi, and Personal Day Number
"""

from datetime import datetime
from core.lunar_calendar import get_lunar_date, format_lunar_date, get_season_from_lunar_month
from core.can_chi import get_can_chi_day, get_truc
from core.numerology import calculate_personal_day_number


class DataCollectorAgent:
    """Agent responsible for collecting and converting temporal data"""
    
    def __init__(self, user_birth_day: int, user_birth_month: int):
        """
        Initialize the Data Collector Agent
        
        Args:
            user_birth_day: User's birth day
            user_birth_month: User's birth month
        """
        self.user_birth_day = user_birth_day
        self.user_birth_month = user_birth_month
    
    def analyze(self, target_date: datetime) -> dict:
        """
        Collect all temporal data for the target date
        
        Args:
            target_date: The date to analyze
            
        Returns:
            Complete temporal analysis including lunar date, Can Chi, and numerology
        """
        # Convert to lunar calendar
        lunar_info = get_lunar_date(target_date)
        lunar_formatted = format_lunar_date(lunar_info)
        season = get_season_from_lunar_month(lunar_info["lunar_month"])
        
        # Get Can Chi for the day
        can_chi_info = get_can_chi_day(target_date)
        
        # Calculate Trực (Duty God)
        truc = get_truc(lunar_info["lunar_month"], can_chi_info["chi_index"])
        
        # Calculate Personal Day Number
        personal_day_number = calculate_personal_day_number(
            target_date,
            self.user_birth_day,
            self.user_birth_month
        )
        
        # Compile result
        result = {
            # Solar date info
            "solar_date": target_date,
            "solar_formatted": target_date.strftime("%d/%m/%Y"),
            "weekday": target_date.strftime("%A"),
            "weekday_vn": self._get_weekday_vietnamese(target_date.weekday()),
            
            # Lunar date info
            "lunar_day": lunar_info["lunar_day"],
            "lunar_month": lunar_info["lunar_month"],
            "lunar_year": lunar_info["lunar_year"],
            "lunar_formatted": lunar_formatted,
            "season": season,
            "is_leap_month": lunar_info["is_leap_month"],
            
            # Can Chi info
            "can": can_chi_info["can"],
            "chi": can_chi_info["chi"],
            "can_chi": can_chi_info["can_chi"],
            "element_can": can_chi_info["element_can"],
            "element_chi": can_chi_info["element_chi"],
            "animal": can_chi_info["animal"],
            "chi_index": can_chi_info["chi_index"],
            
            # Trực (Duty God)
            "truc": truc,
            
            # Numerology
            "personal_day_number": personal_day_number,
            
            # Metadata
            "agent": "DataCollectorAgent",
            "timestamp": datetime.now().isoformat()
        }
        
        return result
    
    def _get_weekday_vietnamese(self, weekday: int) -> str:
        """
        Convert weekday number to Vietnamese name
        
        Args:
            weekday: 0=Monday, 6=Sunday
            
        Returns:
            Vietnamese weekday name
        """
        days = {
            0: "Thứ Hai",
            1: "Thứ Ba",
            2: "Thứ Tư",
            3: "Thứ Năm",
            4: "Thứ Sáu",
            5: "Thứ Bảy",
            6: "Chủ Nhật"
        }
        return days.get(weekday, "Unknown")
    
    def get_summary(self, data: dict) -> str:
        """
        Generate a human-readable summary of collected data
        
        Args:
            data: Result from analyze()
            
        Returns:
            Formatted summary string
        """
        summary = f"""
📅 Ngày Dương: {data['solar_formatted']} ({data['weekday_vn']})
🌙 Ngày Âm: {data['lunar_formatted']}
🎋 Can Chi: {data['can_chi']} (Ngày {data['animal']})
⛩️ Trực: {data['truc']}
🔢 Số ngày cá nhân: {data['personal_day_number']}
🌿 Ngũ hành ngày: {data['element_can']} (Can) - {data['element_chi']} (Chi)
"""
        return summary.strip()
