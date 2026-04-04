import google.generativeai as genai
import os

# Kết nối với chìa khóa bạn đã lưu trong Secrets
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Chọn mô hình Gemini
model = genai.GenerativeModel('gemini-1.5-flash')

# Thử nghiệm gửi một câu hỏi
prompt = "Chào bạn, mình là Bot mới tạo. Hãy gửi một lời chào mừng mình đến với thế giới nhé!"
response = model.generate_content(prompt)

print("--- Kết quả từ Gemini ---")
print(response.text)
