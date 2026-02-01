from flask import Flask, request, send_from_directory
import base64, os, webbrowser

app = Flask(__name__)

# 🔹 Отдаёт index.html
@app.route("/")
def index():
    return send_from_directory(".", "pay2.html")

# 🔹 Получает данные от index.html


if __name__ == "__main__":
    app.run(port=8000)

