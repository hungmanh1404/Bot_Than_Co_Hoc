"""
Core constants for Phong Thủy (Feng Shui) calculations
Includes Ngũ Hành (Five Elements), Can Chi (Heavenly Stems & Earthly Branches)
"""

# Thiên Can (Heavenly Stems) - 10 stems
THIEN_CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]

# Địa Chi (Earthly Branches) - 12 branches
DIA_CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

# Mapping Thiên Can to Elements
CAN_TO_ELEMENT = {
    "Giáp": "Mộc", "Ất": "Mộc",
    "Bính": "Hỏa", "Đinh": "Hỏa",
    "Mậu": "Thổ", "Kỷ": "Thổ",
    "Canh": "Kim", "Tân": "Kim",
    "Nhâm": "Thủy", "Quý": "Thủy"
}

# Mapping Địa Chi to Elements
CHI_TO_ELEMENT = {
    "Tý": "Thủy", "Sửu": "Thổ", "Dần": "Mộc", "Mão": "Mộc",
    "Thìn": "Thổ", "Tỵ": "Hỏa", "Ngọ": "Hỏa", "Mùi": "Thổ",
    "Thân": "Kim", "Dậu": "Kim", "Tuất": "Thổ", "Hợi": "Thủy"
}

# Mapping Địa Chi to Animals (Chinese Zodiac)
CHI_TO_ANIMAL = {
    "Tý": "Chuột", "Sửu": "Trâu", "Dần": "Hổ", "Mão": "Mèo",
    "Thìn": "Rồng", "Tỵ": "Rắn", "Ngọ": "Ngựa", "Mùi": "Dê",
    "Thân": "Khỉ", "Dậu": "Gà", "Tuất": "Chó", "Hợi": "Heo"
}

# Xung (Clash) pairs - opposing branches
XUNG_PAIRS = [
    ("Tý", "Ngọ"),
    ("Sửu", "Mùi"),
    ("Dần", "Thân"),
    ("Mão", "Dậu"),
    ("Thìn", "Tuất"),
    ("Tỵ", "Hợi")
]

# Hợp (Harmony) pairs - compatible branches
HOP_PAIRS = [
    ("Tý", "Sửu"),
    ("Dần", "Hợi"),
    ("Mão", "Tuất"),
    ("Thìn", "Dậu"),
    ("Tỵ", "Thân"),
    ("Ngọ", "Mùi")
]

# Tam Hợp (Triple Harmony) groups
TAM_HOP = [
    ("Thân", "Tý", "Thìn"),  # Water group
    ("Hợi", "Mão", "Mùi"),   # Wood group
    ("Dần", "Ngọ", "Tuất"),  # Fire group
    ("Tỵ", "Dậu", "Sửu")     # Metal group
]

# Ngũ Hành (Five Elements) relationships
# Sinh (Generation): Element A generates Element B
NGU_HANH_SINH = {
    "Mộc": "Hỏa",   # Wood feeds Fire
    "Hỏa": "Thổ",   # Fire creates Earth (ash)
    "Thổ": "Kim",   # Earth bears Metal
    "Kim": "Thủy",  # Metal collects Water
    "Thủy": "Mộc"   # Water nourishes Wood
}

# Khắc (Control/Domination): Element A controls Element B
NGU_HANH_KHAC = {
    "Mộc": "Thổ",   # Wood parts Earth
    "Thổ": "Thủy",  # Earth dams Water
    "Thủy": "Hỏa",  # Water quenches Fire
    "Hỏa": "Kim",   # Fire melts Metal
    "Kim": "Mộc"    # Metal chops Wood
}

# 12 Trực (12 Duty Gods) - rotate based on month and day
TRUC_12 = [
    "Kiến", "Trừ", "Mãn", "Bình", "Định", "Chấp",
    "Phá", "Nguy", "Thành", "Thu", "Khai", "Bế"
]

# Hoàng Đạo (Auspicious) and Hắc Đạo (Inauspicious) days
HOANG_DAO = ["Kiến", "Trừ", "Mãn", "Bình", "Định", "Thành"]
HAC_DAO = ["Chấp", "Phá", "Nguy", "Thu", "Khai", "Bế"]

# Lucky colors for each element (Hex codes)
ELEMENT_COLORS = {
    "Kim": ["#FFD700", "#C0C0C0", "#F5F5DC"],  # Gold, Silver, Beige
    "Mộc": ["#228B22", "#32CD32", "#90EE90"],  # Forest Green, Lime, Light Green
    "Thủy": ["#000080", "#4169E1", "#87CEEB"],  # Navy, Royal Blue, Sky Blue
    "Hỏa": ["#FF0000", "#FF4500", "#FF6347"],  # Red, Orange Red, Tomato
    "Thổ": ["#8B4513", "#D2691E", "#F4A460"]   # Saddle Brown, Chocolate, Sandy Brown
}

# Element state based on season (Vượng/Tướng/Hưu/Tù/Tử)
# Vượng = Prosperous, Tướng = Growing, Hưu = Resting, Tù = Imprisoned, Tử = Dead
ELEMENT_STATE_BY_SEASON = {
    "Xuân": {  # Spring (months 1-3)
        "Mộc": "Vượng",
        "Hỏa": "Tướng",
        "Thủy": "Hưu",
        "Kim": "Tù",
        "Thổ": "Tử"
    },
    "Hạ": {  # Summer (months 4-6)
        "Hỏa": "Vượng",
        "Thổ": "Tướng",
        "Mộc": "Hưu",
        "Thủy": "Tù",
        "Kim": "Tử"
    },
    "Thu": {  # Autumn (months 7-9)
        "Kim": "Vượng",
        "Thủy": "Tướng",
        "Thổ": "Hưu",
        "Hỏa": "Tù",
        "Mộc": "Tử"
    },
    "Đông": {  # Winter (months 10-12)
        "Thủy": "Vượng",
        "Mộc": "Tướng",
        "Kim": "Hưu",
        "Thổ": "Tù",
        "Hỏa": "Tử"
    }
}

# Numerology meanings (1-9)
NUMEROLOGY_MEANINGS = {
    1: {
        "name": "Người Lãnh Đạo",
        "traits": ["độc lập", "sáng tạo", "quyết đoán"],
        "dev_context": "Thích hợp làm lead, architect, tự chủ về technical decision"
    },
    2: {
        "name": "Người Hợp Tác",
        "traits": ["nhạy cảm", "hòa hợp", "diplomatic"],
        "dev_context": "Giỏi teamwork, code review, pair programming"
    },
    3: {
        "name": "Người Sáng Tạo",
        "traits": ["hoạt ngôn", "lạc quan", "sáng tạo"],
        "dev_context": "Brainstorm tốt, UI/UX design, viết documentation hay"
    },
    4: {
        "name": "Người Xây Dựng",
        "traits": ["thực tế", "kỷ luật", "kiên nhẫn"],
        "dev_context": "Viết code stable, testing kỹ, refactor hệ thống"
    },
    5: {
        "name": "Người Tự Do",
        "traits": ["linh hoạt", "phiêu lưu", "thích thay đổi"],
        "dev_context": "Học công nghệ mới nhanh, nhưng dễ nhảy việc"
    },
    6: {
        "name": "Người Chăm Sóc",
        "traits": ["trách nhiệm", "bảo vệ", "hỗ trợ"],
        "dev_context": "Maintain code tốt, support junior, fix bug tận tâm"
    },
    7: {
        "name": "Người Tìm Kiếm",
        "traits": ["phân tích", "suy ngẫm", "tâm linh"],
        "dev_context": "Giỏi thuật toán phức tạp, research deep, debug khó"
    },
    8: {
        "name": "Người Quyền Lực",
        "traits": ["tham vọng", "quản lý", "thành công"],
        "dev_context": "Build product scale lớn, CTO material, business mindset"
    },
    9: {
        "name": "Người Nhân Đạo",
        "traits": ["rộng lượng", "hoàn thiện", "từ bỏ"],
        "dev_context": "Open source contributor, mentor giỏi, legacy code cleanup"
    }
}
