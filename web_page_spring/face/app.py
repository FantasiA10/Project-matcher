import os
from flask import Flask, render_template, request, jsonify
import base64
import face_recognition

app = Flask(__name__)

# save folder
known_faces = {}

# set location
face_folder = './known_faces'

for filename in os.listdir(face_folder):
    img_path = os.path.join(face_folder, filename)
    img = face_recognition.load_image_file(img_path)
    encodings = face_recognition.face_encodings(img)
    if len(encodings) > 0:
        known_faces[filename] = encodings[0]

@app.route('/')
def index():
    return render_template('capture.html', title='Register', action='/register_user')

@app.route('/login_page')
def login_page():
    return render_template('capture.html', title='Login', action='/login')

@app.route('/login', methods=['POST'])
def login():
    img_data = request.form['image'].split(',', 1)[1]
    img_bytes = base64.b64decode(img_data)

    with open('temp.jpg', 'wb') as f:
        f.write(img_bytes)

    unknown_img = face_recognition.load_image_file('temp.jpg')
    unknown_encoding = face_recognition.face_encodings(unknown_img)

    if len(unknown_encoding) > 0:
        unknown_encoding = unknown_encoding[0]

        # Find the best match for the unknown face
        best_match = None
        best_distance = 1.0
        for name, encoding in known_faces.items():
            distance = face_recognition.face_distance([encoding], unknown_encoding)[0]
            if distance < best_distance:
                best_distance = distance
                best_match = name

        # Check if the best match is below the threshold
        threshold = 0.6
        if best_distance < threshold:
            return jsonify(success=True, name=best_match)

    return jsonify(success=False)

@app.route('/register')
def register():
    return render_template('capture.html', title='Register', action='/register_user')

@app.route('/register_user', methods=['POST'])
def register_user():
    img_data = request.form['image'].split(',', 1)[1]
    img_bytes = base64.b64decode(img_data)
    name = request.form['name']

    # Check if the user already exists
    if f'{name}.jpg' in known_faces:
        return jsonify(success=False, message="User with this name already exists. Please choose a different name.")

    # Save the image to known_faces folder
    img_path = os.path.join(face_folder, f'{name}.jpg')
    with open(img_path, 'wb') as f:
        f.write(img_bytes)

    # Load the image and save its encoding to known_faces dictionary
    img = face_recognition.load_image_file(img_path)
    encodings = face_recognition.face_encodings(img)
    if len(encodings) > 0:
        known_faces[f'{name}.jpg'] = encodings[0]

    return jsonify(success=True)
if __name__ == '__main__':
    app.run(debug=True)
