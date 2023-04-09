from flask import Flask, render_template, request, jsonify, redirect, url_for
import face_recognition
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Simulate user database
USER_DATABASE = {
    # Existing user data
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register_user', methods=['POST'])
def register_user():
    data = request.get_json()

    if not data or "image" not in data or "name" not in data:
        return jsonify({"success": False, "message": "Image or name data missing"}), 400

    # Decode image data from Base64
    image_data = base64.b64decode(data["image"].split(',')[1])
    image = Image.open(BytesIO(image_data))
    image = image.convert("RGB")

    # Convert the image to a format that face_recognition library can handle
    face_image = face_recognition.load_image_file(BytesIO(image_data))

    # Locate facial features in the image
    face_locations = face_recognition.face_locations(face_image)
    if not face_locations:
        return jsonify({"success": False, "message": "No face detected"}), 400

    # Extract facial features
    face_encodings = face_recognition.face_encodings(face_image, face_locations)

    # Save the user's facial features and name in the database
    user_id = f"user{len(USER_DATABASE) + 1}"
    USER_DATABASE[user_id] = {
        "name": data["name"],
        "face_encoding": face_encodings[0]
    }

    return jsonify({"success": True, "message": "User registered successfully"})

# Existing login() function

if __name__ == "__main__":
    app.run(debug=True)
