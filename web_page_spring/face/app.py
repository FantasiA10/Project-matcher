from flask import Flask, request, jsonify
import face_recognition
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Simulate user database
USER_DATABASE = {
    "user1": {
        "name": "John Doe",
        "face_encoding": [-0.0980, 0.0632, 0.0265, ..., 0.0639, -0.0294, -0.0087]
    },
    "user2": {
        "name": "Jane Smith",
        "face_encoding": [0.0123, -0.0456, 0.0674, ..., -0.0345, 0.0229, -0.0671]
    }
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or "image" not in data:
        return jsonify({"success": False, "message": "Image data missing"}), 400

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

    # Iterate through the user database to find a user that matches the extracted facial features
    for user_id, user_data in USER_DATABASE.items():
        match = face_recognition.compare_faces([user_data["face_encoding"]], face_encodings[0], tolerance=0.6)
        if match[0]:
            return jsonify({"success": True, "user": {"id": user_id, "name": user_data["name"]}})

    return jsonify({"success": False, "message": "Login failed"}), 401

if __name__ == "__main__":
    app.run(debug=True)
