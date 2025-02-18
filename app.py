from dotenv import load_dotenv

load_dotenv()
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Hàm gọi API của Hugging Face để tạo bài viết
def generate_content(topic):
    API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-1.3B"
    import os

headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

    data = {"inputs": f"Viết một bài chuẩn SEO về: {topic}"}
    
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()[0]["generated_text"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        content = generate_content(topic)
        return render_template("index.html", topic=topic, content=content)
    return render_template("index.html", topic="", content="")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
