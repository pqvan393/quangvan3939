import google.generativeai as genai
from google.generativeai.types import GenerationConfig

class GeminiBot:
    def __init__(self, api_key: str, model_name: str = 'gemini-1.5-flash'):
        """Khởi tạo Bot với API Key và cấu hình model."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=self._get_config()
        )
        self.chat_session = self.model.start_chat(history=[])

    def _get_config(self):
        """Cấu hình tham số phản hồi (tùy chỉnh độ sáng tạo)."""
        return GenerationConfig(
            temperature=0.7,
            top_p=0.95,
            top_k=64,
            max_output_tokens=2048,
        )

    def ask(self, prompt: str) -> str:
        """Gửi tin nhắn và nhận phản hồi từ Bot."""
        try:
            response = self.chat_session.send_message(prompt)
            return response.text
        except Exception as e:
            return f"❌ Lỗi khi gọi Gemini: {str(e)}"

    def reset_chat(self):
        """Xóa lịch sử trò chuyện."""
        self.chat_session = self.model.start_chat(history=[])
