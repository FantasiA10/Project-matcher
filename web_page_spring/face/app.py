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
    return render_template('capture.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    img_data = data['image'].split(',', 1)[1]
    img_bytes = base64.b64decode(img_data)

    with open('temp.jpg', 'wb') as f:
        f.write(img_bytes)

    unknown_img = face_recognition.load_image_file('temp.jpg')
    unknown_encoding = face_recognition.face_encodings(unknown_img)

    if len(unknown_encoding) > 0:
        unknown_encoding = unknown_encoding[0]

        for name, encoding in known_faces.items():
            matches = face_recognition.compare_faces([encoding], unknown_encoding)
            if True in matches:
                return jsonify(success=True, name=name)

    return jsonify(success=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        img_data = request.form['image'].split(',', 1)[1]
        img_bytes = base64.b64decode(img_data)
        name = request.form['name']

        # Save the image to known_faces folder
        img_path = os.path.join(face_folder, f'{name}.jpg')
        with open(img_path, 'wb') as f:
            f.write(img_bytes)

        # Load the image and save its encoding to known_faces dictionary
        img = face_recognition.load_image_file(img_path)
        encodings = face_recognition.face_encodings(img)
        if len(encodings) > 0:
            known_faces[name] = encodings[0]

        return jsonify(success=True)

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
