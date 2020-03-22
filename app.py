from flask import Flask, render_template, send_from_directory
import os

MEDIA_FOLDER = './medias'

app = Flask(__name__)

app.config['MEDIA_FOLDER'] = MEDIA_FOLDER 

@app.route("/")
def home():
	abs_path = os.path.join(app.config['MEDIA_FOLDER'])
	 # Return 404 if path doesn't exist
	if not os.path.exists(abs_path):
		return abort(404)

	# Check if path is a file and serve
	if os.path.isfile(abs_path):
		return send_file(abs_path)

	# Show directory contents
	files = os.listdir(abs_path)
	return render_template('index.html', files=files)

@app.route("/media/<filename>")
def media(filename=None):
	return render_template('media.html', filename=filename)

@app.route("/get_media/<filename>")
def get_media(filename):
	return send_from_directory(app.config['MEDIA_FOLDER'],filename)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)