from google import genai
import os

# Kết nối API
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Gửi câu hỏi cho Gemini 1.5 Flash
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Chào bạn, mình là Bot vừa được nâng cấp. Hãy gửi một lời chúc mừng mình nhé!"
)

print("--- Kết quả từ Gemini ---")
print(response.text)
