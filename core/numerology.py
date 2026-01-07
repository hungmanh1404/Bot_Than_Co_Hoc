"""
Numerology calculations for Personal Day Number
Based on Pythagorean numerology system
"""

from datetime import datetime
from .constants import NUMEROLOGY_MEANINGS


def reduce_to_single_digit(num: int) -> int:
    """
    Reduce a number to a single digit (1-9) by summing its digits
    Master numbers 11, 22, 33 are NOT reduced in this system
    
    Args:
        num: Number to reduce
        
    Returns:
        Single digit (1-9)
    """
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num


def calculate_life_path_number(birth_day: int, birth_month: int, birth_year: int) -> int:
    """
    Calculate Life Path Number (Đường đời)
    
    Args:
        birth_day: Day of birth
        birth_month: Month of birth
        birth_year: Year of birth
        
    Returns:
        Life Path Number (1-9)
    """
    day_sum = reduce_to_single_digit(birth_day)
    month_sum = reduce_to_single_digit(birth_month)
    year_sum = reduce_to_single_digit(sum(int(d) for d in str(birth_year)))
    
    total = day_sum + month_sum + year_sum
    return reduce_to_single_digit(total)


def calculate_personal_day_number(
    date: datetime,
    birth_day: int,
    birth_month: int
) -> int:
    """
    Calculate Personal Day Number
    Formula: (Current Day + Current Month + Current Year) + (Birth Day + Birth Month)
    All reduced to single digits and summed
    
    Args:
        date: The date to calculate for
        birth_day: User's birth day
        birth_month: User's birth month
        
    Returns:
        Personal Day Number (1-9)
    """
    # Current date components
    current_day = reduce_to_single_digit(date.day)
    current_month = reduce_to_single_digit(date.month)
    current_year = reduce_to_single_digit(sum(int(d) for d in str(date.year)))
    
    # Birth components
    birth_day_reduced = reduce_to_single_digit(birth_day)
    birth_month_reduced = reduce_to_single_digit(birth_month)
    
    # Sum all components
    total = current_day + current_month + current_year + birth_day_reduced + birth_month_reduced
    
    return reduce_to_single_digit(total)


def get_number_meaning(number: int) -> dict:
    """
    Get the meaning and interpretation of a numerology number
    
    Args:
        number: Numerology number (1-9)
        
    Returns:
        dict with name, traits, and dev_context
    """
    return NUMEROLOGY_MEANINGS.get(number, {
        "name": "Unknown",
        "traits": [],
        "dev_context": ""
    })


def get_number_energy_description(number: int) -> str:
    """
    Get a brief energy description for a number
    
    Args:
        number: Numerology number (1-9)
        
    Returns:
        Brief description string
    """
    descriptions = {
        1: "Năng lượng độc lập, quyết đoán, bắt đầu mới",
        2: "Năng lượng hợp tác, hòa hợp, nhạy cảm",
        3: "Năng lượng sáng tạo, giao tiếp, lạc quan",
        4: "Năng lượng ổn định, xây dựng, kỷ luật",
        5: "Năng lượng thay đổi, tự do, linh hoạt",
        6: "Năng lượng trách nhiệm, chăm sóc, hài hòa",
        7: "Năng lượng phân tích, suy ngẫm, tìm kiếm",
        8: "Năng lượng quyền lực, thành công, vật chất",
        9: "Năng lượng hoàn thiện, nhân đạo, từ bỏ"
    }
    
    return descriptions.get(number, "Năng lượng trung lập")


def check_number_compatibility(user_life_path: int, day_number: int) -> dict:
    """
    Check compatibility between user's life path number and day number
    
    Args:
        user_life_path: User's life path number
        day_number: The personal day number
        
    Returns:
        dict with compatibility score and description
    """
    # Simplified compatibility matrix
    # Same number = very harmonious
    # Adjacent numbers = somewhat compatible
    # Opposite numbers (differ by 5) = challenging
    
    diff = abs(user_life_path - day_number)
    
    if diff == 0:
        return {
            "score": 9,
            "description": "Rất hợp - Năng lượng ngày đồng điệu với bản chất bạn"
        }
    elif diff in [1, 2]:
        return {
            "score": 7,
            "description": "Khá hợp - Năng lượng ngày hỗ trợ tốt"
        }
    elif diff in [3, 4]:
        return {
            "score": 5,
            "description": "Trung bình - Cần điều chỉnh nhẹ để thích ứng"
        }
    elif diff >= 5:
        return {
            "score": 3,
            "description": "Thách thức - Năng lượng ngày khác biệt, cần linh hoạt"
        }
    
    return {"score": 5, "description": "Bình thường"}
