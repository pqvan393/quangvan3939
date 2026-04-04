from google import genai
from google.genai import types
import os
import asyncio
from typing import Optional

class GeminiBot:
    def __init__(self, api_key: Optional[str] = None):
        # Ưu tiên lấy API key từ biến môi trường
        self.api_key = api_key or os.getenv("GOOGLE_GENAI_API_KEY")
        if not self.api_key:
            raise ValueError("Vui lòng cung cấp GOOGLE_GENAI_API_KEY hoặc truyền api_key vào constructor")

        self.client = genai.Client(api_key=self.api_key)

        # Model khuyến nghị hiện tại (tháng 4/2026)
        self.model_name = "gemini-2.5-flash"      # Nhanh, thông minh, chi phí tốt
        # Các lựa chọn khác:
        # "gemini-2.5-pro"     # Mạnh hơn, phù hợp task phức tạp
        # "gemini-3-flash-preview"  # Nếu muốn thử phiên bản mới nhất (preview)

    def generate_response(self, prompt: str, temperature: float = 0.7, max_tokens: int = 2048) -> str:
        """Gọi Gemini đồng bộ (sync)"""
        try:
            config = types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
                # Bạn có thể thêm safety_settings nếu cần
            )

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=config
            )

            return response.text.strip() if response.text else "Xin lỗi, tôi không nhận được phản hồi từ mô hình."

        except Exception as e:
            return f"Lỗi khi gọi Gemini: {str(e)}"

    async def generate_response_async(self, prompt: str, temperature: float = 0.7, max_tokens: int = 2048) -> str:
        """Gọi Gemini bất đồng bộ (async) - khuyến nghị dùng nếu bot của bạn chạy async"""
        try:
            config = types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
            )

            response = await self.client.models.generate_content_async(
                model=self.model_name,
                contents=prompt,
                config=config
            )

            return response.text.strip() if response.text else "Xin lỗi, tôi không nhận được phản hồi từ mô hình."

        except Exception as e:
            return f"Lỗi khi gọi Gemini: {str(e)}"


# Nếu bạn muốn hỗ trợ chat có lịch sử (conversation)
class GeminiChatBot(GeminiBot):
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(api_key)
        self.history = []   # Lưu lịch sử hội thoại

    def chat(self, user_message: str) -> str:
        self.history.append({"role": "user", "parts": [user_message]})

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=self.history
            )

            bot_reply = response.text.strip()
            self.history.append({"role": "model", "parts": [bot_reply]})
            return bot_reply

        except Exception as e:
            return f"Lỗi: {str(e)}"

    def clear_history(self):
        self.history.clear()
