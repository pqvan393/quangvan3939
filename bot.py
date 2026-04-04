from google import genai
import os

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("LỖI: Không tìm thấy API Key!")
else:
    try:
        client = genai.Client(api_key=api_key)
        
        # Thử sử dụng tên mô hình đầy đủ hơn
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents="Chào bạn, hãy xác nhận bạn đã hoạt động bằng cách nói: 'Tôi đã sẵn sàng!'"
        )
        
        print("--- KẾT QUẢ ---")
        print(response.text)
    except Exception as e:
        # Nếu vẫn lỗi 404, đoạn này sẽ giúp bạn biết bạn có những mô hình nào
        print(f"Lỗi: {e}")
        print("\nMẹo: Hãy kiểm tra xem API Key của bạn đã được kích hoạt trong Google AI Studio chưa nhé.")
