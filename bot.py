name: Run Gemini Bot

on:
  workflow_dispatch: # Cho phép bạn bấm nút chạy thủ công để kiểm tra

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: pip install google-generativeai

      - name: Run bot
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }} # Lấy key từ Secrets ra
        run: python bot.py
