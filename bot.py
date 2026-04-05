import google.generativeai as genai
import os

# 1. Cấu hình API Key
# Thay 'YOUR_API_KEY' bằng mã thực tế của bạn hoặc thiết lập biến môi trường
API_KEY = "YOUR_API_KEY"
genai.configure(api_key=API_KEY)

def generate_gemini_content():
    try:
        # 2. Sử dụng tên model chuẩn: 'gemini-1.5-flash' 
        # (Bỏ đuôi '-latest' nếu gặp lỗi 404 vì alias này đôi khi không khớp với endpoint v1beta)
        model_name = 'gemini-1.5-flash'
        
        # Khởi tạo model
        model = genai.GenerativeModel(model_name)
        
        # 3. Gọi hàm generate_content
        prompt = "Viết một lời chào ngắn gọn và hài hước bằng tiếng Việt."
        
        print(f"--- Đang gửi yêu cầu tới model: {model_name} ---")
        response = model.generate_content(prompt)
        
        # 4. Xuất kết quả
        print("Kết quả phản hồi:")
        print(response.text)

    except Exception as e:
        # Bắt lỗi và hướng dẫn xử lý
        print(f"Đã xảy ra lỗi: {e}")
        print("\nGợi ý sửa lỗi:")
        print("- Kiểm tra lại API Key xem đã chính xác chưa.")
        print("- Chạy 'pip install -U google-generativeai' để cập nhật thư viện.")
        print("- Sử dụng lệnh 'genai.list_models()' để xem danh sách model khả dụng.")

if __name__ == "__main__":
    generate_gemini_content()
