"""
Can Chi (Heavenly Stems & Earthly Branches) calculations
Implements the 60-year sexagenary cycle used in Vietnamese astrology
"""

from datetime import datetime
from .constants import THIEN_CAN, DIA_CHI, CAN_TO_ELEMENT, CHI_TO_ELEMENT, CHI_TO_ANIMAL, TRUC_12


# Reference date with known Can Chi
# January 1, 1900 was 庚子 (Canh Tý) day
REFERENCE_DATE = datetime(1900, 1, 1)
REFERENCE_CAN_INDEX = 6  # Canh (index in THIEN_CAN)
REFERENCE_CHI_INDEX = 0  # Tý (index in DIA_CHI)


def get_can_chi_day(date: datetime) -> dict:
    """
    Calculate Can Chi (Heavenly Stem + Earthly Branch) for a given day
    
    Args:
        date: datetime object
        
    Returns:
        dict with can, chi, can_chi (combined), element_can, element_chi, animal
    """
    # Convert to naive datetime if timezone-aware
    if date.tzinfo is not None:
        date = date.replace(tzinfo=None)
    
    # Calculate number of days from reference date
    days_diff = (date - REFERENCE_DATE).days
    
    # Calculate Can (repeats every 10 days)
    can_index = (REFERENCE_CAN_INDEX + days_diff) % 10
    can = THIEN_CAN[can_index]
    
    # Calculate Chi (repeats every 12 days)
    chi_index = (REFERENCE_CHI_INDEX + days_diff) % 12
    chi = DIA_CHI[chi_index]
    
    # Combine Can Chi
    can_chi = f"{can} {chi}"
    
    return {
        "can": can,
        "chi": chi,
        "can_chi": can_chi,
        "element_can": CAN_TO_ELEMENT[can],
        "element_chi": CHI_TO_ELEMENT[chi],
        "animal": CHI_TO_ANIMAL[chi],
        "chi_index": chi_index
    }


def get_truc(lunar_month: int, day_chi_index: int) -> str:
    """
    Calculate Trực (12 Duty Gods) for a given day
    
    Args:
        lunar_month: Lunar month (1-12)
        day_chi_index: Index of the day's Chi (0-11)
        
    Returns:
        Trực name (one of 12 TRUC_12)
    """
    # Formula: Trực index = (lunar_month + day_chi_index - 1) % 12
    # Adjusted for Vietnamese system
    truc_index = (lunar_month + day_chi_index + 1) % 12
    return TRUC_12[truc_index]


def get_can_chi_year(year: int) -> dict:
    """
    Calculate Can Chi for a given year
    
    Args:
        year: Year (e.g., 2001)
        
    Returns:
        dict with can, chi, can_chi, element
    """
    # Reference: Year 1984 was Giáp Tý (Giáp = 0, Tý = 0)
    # Can cycles every 10 years, Chi cycles every 12 years
    
    can_index = (year - 4) % 10
    chi_index = (year - 4) % 12
    
    can = THIEN_CAN[can_index]
    chi = DIA_CHI[chi_index]
    can_chi = f"{can} {chi}"
    
    return {
        "can": can,
        "chi": chi,
        "can_chi": can_chi,
        "element": CAN_TO_ELEMENT[can],
        "animal": CHI_TO_ANIMAL[chi]
    }


def check_xung(chi1: str, chi2: str) -> bool:
    """
    Check if two Chi (Earthly Branches) clash (Xung)
    
    Args:
        chi1: First Chi
        chi2: Second Chi
        
    Returns:
        True if they clash, False otherwise
    """
    from .constants import XUNG_PAIRS
    
    for pair in XUNG_PAIRS:
        if (chi1 == pair[0] and chi2 == pair[1]) or (chi1 == pair[1] and chi2 == pair[0]):
            return True
    return False


def check_hop(chi1: str, chi2: str) -> bool:
    """
    Check if two Chi (Earthly Branches) harmonize (Hợp)
    
    Args:
        chi1: First Chi
        chi2: Second Chi
        
    Returns:
        True if they harmonize, False otherwise
    """
    from .constants import HOP_PAIRS
    
    for pair in HOP_PAIRS:
        if (chi1 == pair[0] and chi2 == pair[1]) or (chi1 == pair[1] and chi2 == pair[0]):
            return True
    return False


def check_element_relationship(element1: str, element2: str) -> dict:
    """
    Check the relationship between two elements
    
    Args:
        element1: First element
        element2: Second element
        
    Returns:
        dict with relationship type and description
    """
    from .constants import NGU_HANH_SINH, NGU_HANH_KHAC
    
    if element1 == element2:
        return {
            "type": "same",
            "description": f"{element1} đồng hành {element2}"
        }
    
    # Check if element1 generates element2
    if NGU_HANH_SINH.get(element1) == element2:
        return {
            "type": "sinh",
            "description": f"{element1} sinh {element2} (tốt)"
        }
    
    # Check if element2 generates element1
    if NGU_HANH_SINH.get(element2) == element1:
        return {
            "type": "duoc_sinh",
            "description": f"{element2} sinh {element1} (tốt)"
        }
    
    # Check if element1 controls element2
    if NGU_HANH_KHAC.get(element1) == element2:
        return {
            "type": "khac",
            "description": f"{element1} khắc {element2} (xấu)"
        }
    
    # Check if element2 controls element1
    if NGU_HANH_KHAC.get(element2) == element1:
        return {
            "type": "bi_khac",
            "description": f"{element2} khắc {element1} (xấu)"
        }
    
    return {
        "type": "neutral",
        "description": f"{element1} và {element2} không tương tác mạnh"
    }
