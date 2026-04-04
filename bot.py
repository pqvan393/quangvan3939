from google import genai
import os

# Kiểm tra xem Key có tồn tại không
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("LỖI: Bạn chưa cài đặt GEMINI_API_KEY trong mục Secrets của GitHub!")
else:
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents="Hãy nói 'Kết nối thành công!' bằng tiếng Việt."
        )
        print("--- KẾT QUẢ ---")
        print(response.text)
    except Exception as e:
        print(f"Lỗi khi kết nối với Gemini: {e}")
