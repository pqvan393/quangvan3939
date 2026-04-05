import google.generativeai as genai
import os

# Cấu hình
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

try:
    # Thử gọi model với tên chuẩn nhất
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    response = model.generate_content("Trả lời ngắn gọn: Bạn đã sẵn sàng chưa?")
    
    print("--- KẾT QUẢ TỪ GEMINI ---")
    print(response.text)
    print("-------------------------")
except Exception as e:
    print(f"Lỗi rồi: {e}")
