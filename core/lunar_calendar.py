"""
Lunar Calendar utilities for converting between Solar and Lunar dates
Using LunarDate library for accurate conversion
"""

from datetime import datetime
from lunardate import LunarDate
import pytz


def get_lunar_date(solar_date: datetime) -> dict:
    """
    Convert solar (Gregorian) date to lunar date
    
    Args:
        solar_date: datetime object in solar calendar
        
    Returns:
        dict with lunar_day, lunar_month, lunar_year, is_leap_month
    """
    lunar = LunarDate.fromSolarDate(
        solar_date.year,
        solar_date.month,
        solar_date.day
    )
    
    return {
        "lunar_day": lunar.day,
        "lunar_month": lunar.month,
        "lunar_year": lunar.year,
        "is_leap_month": lunar.isLeapMonth
    }


def format_lunar_date(lunar_info: dict) -> str:
    """
    Format lunar date to Vietnamese string
    
    Args:
        lunar_info: dict from get_lunar_date()
        
    Returns:
        Formatted string like "15/08 Âm lịch"
    """
    day = lunar_info["lunar_day"]
    month = lunar_info["lunar_month"]
    leap = " (nhuận)" if lunar_info["is_leap_month"] else ""
    
    return f"{day:02d}/{month:02d} Âm lịch{leap}"


def get_season_from_lunar_month(lunar_month: int) -> str:
    """
    Get season based on lunar month
    
    Args:
        lunar_month: Lunar month (1-12)
        
    Returns:
        Season name: Xuân/Hạ/Thu/Đông
    """
    if 1 <= lunar_month <= 3:
        return "Xuân"
    elif 4 <= lunar_month <= 6:
        return "Hạ"
    elif 7 <= lunar_month <= 9:
        return "Thu"
    else:
        return "Đông"


def get_vietnam_datetime() -> datetime:
    """
    Get current datetime in Vietnam timezone
    
    Returns:
        Current datetime in Asia/Ho_Chi_Minh timezone
    """
    vn_tz = pytz.timezone('Asia/Ho_Chi_Minh')
    return datetime.now(vn_tz)


def parse_date_string(date_str: str) -> datetime:
    """
    Parse date string in DD/MM/YYYY format to datetime
    
    Args:
        date_str: Date string like "08/01/2026"
        
    Returns:
        datetime object
        
    Raises:
        ValueError: If format is invalid
    """
    try:
        return datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError as e:
        raise ValueError(f"Invalid date format. Use DD/MM/YYYY. Error: {e}")
