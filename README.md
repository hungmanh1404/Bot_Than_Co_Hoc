# Thiên Cơ Đại Tướng Quân 🔮

Hệ thống AI chuyên về **Phong Thủy Bát Tự** và **Thần Số Học**, được thiết kế riêng cho **Nguyễn Hùng Mạnh**.

## ✨ Tính năng

- 🤖 **4-Agent AI System** chạy tuần tự để phân tích năng lượng từng ngày
- 📅 **Tự động gửi Telegram** mỗi ngày lúc 8:00 PM (dự báo cho ngày mai)
- 🔮 **Phân tích Bát Tự**: Tính Can Chi, Xung/Khắc, Ngũ Hành
- 🔢 **Thần số học**: Personal Day Number dựa trên ngày sinh
- 💻 **Developer Context**: Lời khuyên cụ thể cho lập trình viên
- ☁️ **Deploy-ready**: Chạy được trên Render.com (free tier)

## 📦 Cài đặt

### 1. Clone hoặc tải project
```bash
cd /Users/manh.nguyen/Desktop/tuongphongthuy
```

### 2. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 3. Cấu hình môi trường
File `.env` đã được tạo sẵn với thông tin của bạn. Nếu cần chỉnh sửa:
```bash
nano .env
```

## 🚀 Chạy ứng dụng

### Chạy local
```bash
python main.py
```

Bot sẽ:
- ✅ Khởi động Telegram bot
- ✅ Lên lịch gửi tin tự động lúc 8:00 PM mỗi ngày
- ✅ Lắng nghe các commands từ Telegram

### Kiểm tra
1. Mở Telegram
2. Tìm bot của bạn
3. Gửi `/start` để xem hướng dẫn
4. Thử `/dubao 08/01/2026` để xem dự báo

## 📱 Telegram Commands

| Command | Mô tả |
|---------|-------|
| `/start` | Xem hướng dẫn |
| `/help` | Xem chi tiết cách dùng |
| `/dubao DD/MM/YYYY` | Xem dự báo cho ngày cụ thể |
| `/ngaymai` | Xem dự báo cho ngày mai |

## 🎯 Cấu trúc hệ thống

### 4 Agents chạy tuần tự:

1. **Agent 1 - Thám Tử Thời Gian**
   - Chuyển đổi Dương lịch → Âm lịch
   - Tính Can Chi ngày
   - Tính Personal Day Number

2. **Agent 2 - Thầy Phán Bát Tự**
   - Kiểm tra Xung/Hợp với mệnh Tân Tỵ
   - Phân tích Ngũ Hành (Sinh/Khắc)
   - Xác định Hoàng Đạo/Hắc Đạo
   - Tính điểm may mắn (1-10)

3. **Agent 3 - Quân Sư Code Dạo**
   - Dịch tín hiệu phong thủy sang ngôn ngữ Developer
   - Gợi ý: NÊN LÀM / NÊN TRÁNH
   - Tạo "Lời nhắn vũ trụ" hài hước

4. **Agent 4 - Sứ Giả Telegram**
   - Format tin nhắn đẹp với Markdown
   - Chọn màu may mắn theo ngũ hành
   - Gửi lên Telegram

## ☁️ Deploy lên Render.com

### 1. Push code lên GitHub
```bash
git init
git add .
git commit -m "Initial commit - Thiên Cơ Đại Tướng Quân"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

### 2. Tạo Web Service trên Render
- Đăng nhập [Render.com](https://render.com)
- Click **New** → **Web Service**
- Connect GitHub repository
- Cấu hình:
  - **Name**: `tuongphongthuy`
  - **Runtime**: Python 3
  - **Build Command**: `pip install -r requirements.txt`
  - **Start Command**: `python main.py`
  - **Instance Type**: Free

### 3. Thêm Environment Variables
Trong Render dashboard, thêm các biến:
- `TELEGRAM_BOT_TOKEN`: `8246910964:AAHaIYkqy9pWwnDEXP5VBmNXU4WDhn7udRA`
- `TELEGRAM_CHAT_ID`: `8270116773`
- `PORT`: `8080` (tự động set bởi Render)

### 4. Deploy
Click **Create Web Service** và đợi deploy xong!

### 5. Anti-Sleep (Quan trọng!)
Render free tier sẽ sleep sau 15 phút không hoạt động. Để tránh:
1. Vào [cron-job.org](https://cron-job.org)
2. Tạo cron job ping `https://<your-app>.onrender.com/health` mỗi 10 phút

## 🔧 Tùy chỉnh

### Thay đổi giờ gửi tin tự động
Mở file `.env`, sửa:
```
SCHEDULE_HOUR=20  # 8 PM (24h format)
```

### Thay đổi thông tin user
Chỉnh sửa trong `.env`:
```
USER_BIRTH_DAY=14
USER_BIRTH_MONTH=4
USER_BIRTH_YEAR=2001
USER_ELEMENT=Kim
USER_BRANCH=Tỵ
```

## 📖 Giải thích thuật toán

### Can Chi (天干地支)
Hệ thống sử dụng chu kỳ 60 năm (Sexagenary cycle):
- 10 Thiên Can (Giáp, Ất, Bính...)
- 12 Địa Chi (Tý, Sửu, Dần...)

### Ngũ Hành (Five Elements)
- **Sinh**: Mộc → Hỏa → Thổ → Kim → Thủy → Mộc
- **Khắc**: Mộc → Thổ → Thủy → Hỏa → Kim → Mộc

### Xung (Clash)
12 cặp đối xung:
- Tý ↔ Ngọ
- Sửu ↔ Mùi
- Tỵ ↔ Hợi (quan trọng với Mạnh)
- ...

## 🐛 Troubleshooting

### Bot không phản hồi
1. Kiểm tra `TELEGRAM_BOT_TOKEN` đúng chưa
2. Xem logs: `python main.py`

### Không nhận tin tự động
1. Kiểm tra timezone: phải là `Asia/Ho_Chi_Minh`
2. Xem logs lúc 8 PM xem có lỗi gì

### Lỗi "Module not found"
```bash
pip install -r requirements.txt
```

## 📜 License

Hệ thống được xây dựng riêng cho Nguyễn Hùng Mạnh. Phiêu!

---

*Powered by 4-Agent AI • Bát Tự × Thần Số Học × Developer Life* 🔮✨
