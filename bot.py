import google.generativeai as genai
import os

api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

print("--- ĐANG KIỂM TRA CÁC MÔ HÌNH KHẢ DỤNG ---")
available_models = []
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available_models.append(m.name)
            print(f"Tìm thấy: {m.name}")
    
    # Chọn mô hình đầu tiên tìm thấy để chạy thử
    if not available_models:
        print("LỖI: Không tìm thấy mô hình nào hỗ trợ tạo nội dung trong tài khoản này!")
    else:
        target_model = available_models[0]
        print(f"\n--- ĐANG CHẠY THỬ VỚI: {target_model} ---")
        model = genai.GenerativeModel(target_model)
        response = model.generate_content("Chào bạn, hãy xác nhận bạn đang hoạt động.")
        print("KẾT QUẢ:", response.text)

except Exception as e:
    print(f"LỖI HỆ THỐNG: {e}")
