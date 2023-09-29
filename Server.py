from flask import Flask, send_from_directory

app = Flask(__name__)

# Définir le répertoire où les images sont stockées
IMAGE_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

# Définir la route pour afficher une image
@app.route('/<image_name>')
def display_image(image_name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], image_name)

if __name__ == '__main__':
    app.run(debug=True)
