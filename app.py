from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    uploaded_image_path = ""

    if request.method == "POST":
        input_text = request.form["input"]
        uploaded_file = request.files["file"]
        image = Image.open(uploaded_file) if uploaded_file else None

        # Save the uploaded image to a temporary file
        if image:
            uploaded_image_path = "static/uploads/uploaded_image.jpg"
            image.save(uploaded_image_path)

        response_text = get_gemini_response(input_text, image)

    return render_template("index.html", response=response_text, uploaded_image_path=uploaded_image_path)

if __name__ == "__main__":
    app.run(debug=True)
