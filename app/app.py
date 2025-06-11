import os
from flask import Flask, jsonify, send_from_directory, render_template

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_DIRECTORY = os.path.join(BASE_DIR, 'files')

@app.route('/')
def index():
    files = os.listdir(FILES_DIRECTORY)
    return render_template('index.html', files=files)

@app.route('/api/files')
def list_files():
    files = os.listdir(FILES_DIRECTORY)
    return jsonify(files)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(FILES_DIRECTORY, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
