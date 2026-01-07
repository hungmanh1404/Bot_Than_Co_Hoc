"""
Agent 3: Quân Sư Code Dạo (The Dev Strategist)
Translates metaphysical signals into developer-specific advice
"""

from typing import List, Tuple


class DevStrategistAgent:
    """Agent responsible for mapping Feng Shui to developer context"""
    
    def __init__(self):
        """Initialize the Dev Strategist Agent"""
        pass
    
    def analyze(
        self,
        data_collector_result: dict,
        metaphysical_result: dict
    ) -> dict:
        """
        Translate metaphysical analysis into developer-specific recommendations
        
        Args:
            data_collector_result: Output from Agent 1
            metaphysical_result: Output from Agent 2
            
        Returns:
            Developer-specific recommendations
        """
        # Extract key indicators
        luck_score = metaphysical_result["luck_score"]
        has_xung = metaphysical_result["has_xung"]
        is_hoang_dao = metaphysical_result["is_hoang_dao"]
        dominant_element = data_collector_result["element_can"]
        personal_day_number = data_collector_result["personal_day_number"]
        menh_state = metaphysical_result["menh_state"]
        
        # Generate recommendations
        should_do = self._generate_should_do(
            luck_score=luck_score,
            is_hoang_dao=is_hoang_dao,
            dominant_element=dominant_element,
            personal_day_number=personal_day_number,
            menh_state=menh_state
        )
        
        should_avoid = self._generate_should_avoid(
            luck_score=luck_score,
            has_xung=has_xung,
            is_hoang_dao=is_hoang_dao,
            dominant_element=dominant_element,
            personal_day_number=personal_day_number
        )
        
        # Generate mystical message
        cosmic_message = self._generate_cosmic_message(
            data_collector_result=data_collector_result,
            metaphysical_result=metaphysical_result
        )
        
        # Compile result
        result = {
            "should_do": should_do,
            "should_avoid": should_avoid,
            "cosmic_message": cosmic_message,
            "agent": "DevStrategistAgent"
        }
        
        return result
    
    def _generate_should_do(
        self,
        luck_score: int,
        is_hoang_dao: bool,
        dominant_element: str,
        personal_day_number: int,
        menh_state: str
    ) -> List[str]:
        """Generate list of recommended actions"""
        recommendations = []
        
        # Based on luck score
        if luck_score >= 7:
            recommendations.append("Deploy production code (ngày tốt)")
            recommendations.append("Refactor hệ thống lớn")
            recommendations.append("Pitch ideas mới với sếp")
        elif luck_score >= 5:
            recommendations.append("Code features mới")
            recommendations.append("Review PR của đồng đội")
        
        # Based on element
        element_advice = {
            "Hỏa": "Code với nhiệt huyết, brainstorm sáng tạo",
            "Thủy": "Viết thuật toán phức tạp, logic flow tốt",
            "Mộc": "Học công nghệ mới, đọc documentation",
            "Kim": "Cắt giảm code thừa, tối ưu performance",
            "Thổ": "Xây dựng foundation vững chắc, viết tests"
        }
        if dominant_element in element_advice:
            recommendations.append(element_advice[dominant_element])
        
        # Based on personal day number
        number_advice = {
            1: "Bắt đầu dự án mới, làm PoC",
            2: "Pair programming, code review",
            3: "Viết docs, tạo demo presentation",
            4: "Fix bugs, stabilize system",
            5: "Thử framework mới, experiment",
            6: "Support junior devs, maintain legacy code",
            7: "Deep dive vào problem khó, research",
            8: "Plan architecture lớn, meeting với stakeholders",
            9: "Contribute open source, dọn dẹp technical debt"
        }
        if personal_day_number in number_advice:
            recommendations.append(number_advice[personal_day_number])
        
        # Based on menh state
        if menh_state in ["Vượng", "Tướng"]:
            recommendations.append("Mặc áo màu trắng/vàng (tương sinh với Kim)")
        
        # Always include one lifestyle recommendation
        if is_hoang_dao:
            recommendations.append("Meeting quan trọng vào buổi sáng")
        
        return recommendations[:4]  # Limit to 4 recommendations
    
    def _generate_should_avoid(
        self,
        luck_score: int,
        has_xung: bool,
        is_hoang_dao: bool,
        dominant_element: str,
        personal_day_number: int
    ) -> List[str]:
        """Generate list of things to avoid"""
        warnings = []
        
        # Based on luck score
        if luck_score <= 3:
            warnings.append("Deploy production (rủi ro cao)")
            warnings.append("Tranh cãi với PM/Tester")
            warnings.append("Quyết định technical lớn")
        
        # Based on xung
        if has_xung:
            warnings.append("Họp hành căng thẳng, dễ conflict")
            warnings.append("Push code lúc cuối ngày (dễ bug)")
        
        # Based on element
        element_warnings = {
            "Hỏa": "Nóng tính khi debug, máy dễ nóng/lag",
            "Thủy": "Overthinking, analysis paralysis",
            "Mộc": "Quá nhiều ideas, mất focus",
            "Kim": "Quá cứng nhắc, không flexible",
            "Thổ": "Làm việc chậm, đừng commit deadlines gấp"
        }
        if dominant_element in element_warnings:
            warnings.append(element_warnings[dominant_element])
        
        # Based on personal day number
        if personal_day_number == 5:
            warnings.append("Thay đổi nhiều thứ cùng lúc")
        elif personal_day_number == 7:
            warnings.append("Làm việc nhóm lớn (thích làm solo hơn)")
        
        # Based on Hắc Đạo
        if not is_hoang_dao:
            warnings.append("Backup code trước khi thử nghiệm")
        
        return warnings[:4]  # Limit to 4 warnings
    
    def _generate_cosmic_message(
        self,
        data_collector_result: dict,
        metaphysical_result: dict
    ) -> str:
        """
        Generate a mystical yet developer-relevant message
        Combines numerology and element analysis with humor
        """
        luck_score = metaphysical_result["luck_score"]
        personal_day_number = data_collector_result["personal_day_number"]
        dominant_element = data_collector_result["element_can"]
        has_xung = metaphysical_result["has_xung"]
        menh_state = metaphysical_result["menh_state"]
        
        # Message templates based on different conditions
        if luck_score >= 8:
            messages = [
                f"Ngày số {personal_day_number}, {dominant_element} khí vượng - Vũ trụ mở đường cho code của bạn. Deploy thôi!",
                "Các vì sao sắp hàng, Git merge conflict sẽ tự giải quyết... (maybe 😄)",
                "Hôm nay là ngày của bạn. Nhớ commit message có dấu sao nhé ⭐"
            ]
        elif luck_score <= 3:
            messages = [
                f"{dominant_element} khí loạn, mệnh {menh_state}. Bug nhiều như rác trong node_modules. Hãy giữ bình tĩnh!",
                "Ngày Hắc Đạo dày đặc năng lượng âm. Ctrl+S thường xuyên, backup mọi thứ!",
                "Vũ trụ đang test khả năng debug của bạn. Đừng rage quit nhé!"
            ]
        elif has_xung:
            messages = [
                f"Tứ hành xung! Code review sẽ harsh. Comment kỹ, giải thích rõ ràng.",
                "Xung khí mạnh - Tránh meeting lúc 2-4h chiều, lúc đó conflict max.",
                "Ngày xung nhưng bạn là Dev số 3 (sáng tạo) - Dùng humor để hóa giải căng thẳng!"
            ]
        else:
            messages = [
                f"Năng lượng số {personal_day_number} hòa hợp với {dominant_element}. Code flow nhẹ nhàng như stream processing.",
                "Mệnh Kim của bạn cần Thủy để mài giũa. Hãy học thêm, code nhiều hơn!",
                "Ngày ổn định - Thích hợp refactor, viết test, và uống cà phê ☕"
            ]
        
        # Select random message from pool
        import random
        return random.choice(messages)
    
    def get_summary(self, data: dict) -> str:
        """
        Generate formatted summary
        
        Args:
            data: Result from analyze()
            
        Returns:
            Formatted summary string
        """
        summary = "✅ NÊN LÀM:\n"
        for item in data["should_do"]:
            summary += f"  • {item}\n"
        
        summary += "\n❌ NÊN TRÁNH:\n"
        for item in data["should_avoid"]:
            summary += f"  • {item}\n"
        
        summary += f"\n💡 LỜI NHẮN VŨ TRỤ:\n  \"{data['cosmic_message']}\"\n"
        
        return summary.strip()
