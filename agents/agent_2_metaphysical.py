"""
Agent 2: Thầy Phán Bát Tự (The Metaphysical Analyst)
Analyzes metaphysical compatibility and energy patterns
"""

from core.can_chi import check_xung, check_hop, check_element_relationship
from core.constants import (
    HOANG_DAO, HAC_DAO, ELEMENT_STATE_BY_SEASON,
    NGU_HANH_SINH, NGU_HANH_KHAC
)
from core.numerology import get_number_meaning, check_number_compatibility


class MetaphysicalAnalystAgent:
    """Agent responsible for Bát Tự and metaphysical analysis"""
    
    def __init__(self, user_element: str, user_branch: str, user_life_path: int):
        """
        Initialize the Metaphysical Analyst Agent
        
        Args:
            user_element: User's element (e.g., "Kim")
            user_branch: User's earthly branch (e.g., "Tỵ")
            user_life_path: User's life path number
        """
        self.user_element = user_element
        self.user_branch = user_branch
        self.user_life_path = user_life_path
    
    def analyze(self, data_collector_result: dict) -> dict:
        """
        Perform metaphysical analysis on the collected data
        
        Args:
            data_collector_result: Output from Agent 1
            
        Returns:
            Complete metaphysical analysis
        """
        # Extract key data
        day_chi = data_collector_result["chi"]
        day_can = data_collector_result["can"]
        day_element_can = data_collector_result["element_can"]
        day_element_chi = data_collector_result["element_chi"]
        truc = data_collector_result["truc"]
        personal_day_number = data_collector_result["personal_day_number"]
        season = data_collector_result["season"]
        
        # Check Xung (Clash)
        has_xung = check_xung(day_chi, self.user_branch)
        
        # Check Hợp (Harmony)
        has_hop = check_hop(day_chi, self.user_branch)
        
        # Analyze element relationships (Can vs User element)
        element_relationship_can = check_element_relationship(
            day_element_can, 
            self.user_element
        )
        
        # Analyze element relationships (Chi vs User element)
        element_relationship_chi = check_element_relationship(
            day_element_chi,
            self.user_element
        )
        
        # Determine if Hoàng Đạo or Hắc Đạo
        is_hoang_dao = truc in HOANG_DAO
        is_hac_dao = truc in HAC_DAO
        
        # Get element state based on season
        menh_state = ELEMENT_STATE_BY_SEASON[season].get(self.user_element, "Hưu")
        
        # Calculate luck score (1-10)
        luck_score = self._calculate_luck_score(
            has_xung=has_xung,
            has_hop=has_hop,
            is_hoang_dao=is_hoang_dao,
            element_relationship_can=element_relationship_can,
            element_relationship_chi=element_relationship_chi,
            menh_state=menh_state
        )
        
        # Get numerology insights
        number_meaning = get_number_meaning(personal_day_number)
        number_compatibility = check_number_compatibility(
            self.user_life_path,
            personal_day_number
        )
        
        # Compile result
        result = {
            # Branch analysis
            "has_xung": has_xung,
            "has_hop": has_hop,
            "xung_description": f"Ngày {day_chi} XUNG với {self.user_branch} của bạn" if has_xung else None,
            "hop_description": f"Ngày {day_chi} HỢP với {self.user_branch} của bạn" if has_hop else None,
            
            # Element analysis
            "element_relationship_can": element_relationship_can,
            "element_relationship_chi": element_relationship_chi,
            
            # Hoàng Đạo / Hắc Đạo
            "is_hoang_dao": is_hoang_dao,
            "is_hac_dao": is_hac_dao,
            "truc_type": "Hoàng Đạo" if is_hoang_dao else "Hắc Đạo",
            
            # Element state
            "menh_state": menh_state,
            "menh_description": self._get_menh_description(menh_state),
            
            # Luck score
            "luck_score": luck_score,
            
            # Numerology
            "number_meaning": number_meaning,
            "number_compatibility": number_compatibility,
            
            # Dominant element of the day
            "dominant_element": self._get_dominant_element(day_element_can, day_element_chi),
            
            # Metadata
            "agent": "MetaphysicalAnalystAgent"
        }
        
        return result
    
    def _calculate_luck_score(
        self,
        has_xung: bool,
        has_hop: bool,
        is_hoang_dao: bool,
        element_relationship_can: dict,
        element_relationship_chi: dict,
        menh_state: str
    ) -> int:
        """
        Calculate overall luck score from 1-10
        
        Args:
            Various metaphysical indicators
            
        Returns:
            Luck score (1-10)
        """
        score = 5  # Base score
        
        # Xung penalty
        if has_xung:
            score -= 3
        
        # Hợp bonus
        if has_hop:
            score += 2
        
        # Hoàng Đạo / Hắc Đạo
        if is_hoang_dao:
            score += 2
        else:
            score -= 1
        
        # Element relationships
        if element_relationship_can["type"] in ["sinh", "duoc_sinh"]:
            score += 1
        elif element_relationship_can["type"] in ["khac", "bi_khac"]:
            score -= 1
        
        if element_relationship_chi["type"] in ["sinh", "duoc_sinh"]:
            score += 1
        elif element_relationship_chi["type"] in ["khac", "bi_khac"]:
            score -= 1
        
        # Element state bonus/penalty
        state_modifiers = {
            "Vượng": 2,
            "Tướng": 1,
            "Hưu": 0,
            "Tù": -1,
            "Tử": -2
        }
        score += state_modifiers.get(menh_state, 0)
        
        # Clamp to 1-10
        return max(1, min(10, score))
    
    def _get_menh_description(self, state: str) -> str:
        """Get description for element state"""
        descriptions = {
            "Vượng": "Mệnh đang rất vượng, năng lượng dồi dào",
            "Tướng": "Mệnh đang phát triển, trạng thái tốt",
            "Hưu": "Mệnh đang nghỉ ngơi, trạng thái trung bình",
            "Tù": "Mệnh bị giam hãm, cần cẩn thận",
            "Tử": "Mệnh yếu nhất, nên tránh quyết định lớn"
        }
        return descriptions.get(state, "Trạng thái bình thường")
    
    def _get_dominant_element(self, element_can: str, element_chi: str) -> str:
        """
        Determine the dominant element of the day
        Can (Heavenly Stem) is usually more influential
        """
        if element_can == element_chi:
            return f"{element_can} (mạnh)"
        else:
            return f"{element_can} (chủ đạo), {element_chi} (phụ)"
    
    def get_summary(self, data: dict) -> str:
        """
        Generate a human-readable summary
        
        Args:
            data: Result from analyze()
            
        Returns:
            Formatted summary string
        """
        warnings = []
        blessings = []
        
        if data["has_xung"]:
            warnings.append(f"⚠️ {data['xung_description']}")
        
        if data["has_hop"]:
            blessings.append(f"✅ {data['hop_description']}")
        
        if data["is_hac_dao"]:
            warnings.append("⚠️ Ngày Hắc Đạo - cẩn thận")
        else:
            blessings.append("✅ Ngày Hoàng Đạo - thuận lợi")
        
        summary = f"""
🎯 Độ may mắn: {data['luck_score']}/10
🔮 Trạng thái mệnh {self.user_element}: {data['menh_state']} - {data['menh_description']}
⚡ Ngũ hành ngày: {data['dominant_element']}
"""
        
        if blessings:
            summary += "\n✨ Tốt:\n" + "\n".join(blessings) + "\n"
        
        if warnings:
            summary += "\n⚠️ Lưu ý:\n" + "\n".join(warnings) + "\n"
        
        return summary.strip()
