from flask import current_app as app
from flask import Flask, render_template, send_from_directory, request
import os

MEDIA_FOLDER = './medias'
app.config['MEDIA_FOLDER'] = MEDIA_FOLDER

@app.route("/")
@app.route("/<search>")
def home(search=''):
	search_string = request.args.get('search')
	abs_path = os.path.join(app.config['MEDIA_FOLDER'])
	 # Return 404 if path doesn't exist
	if not os.path.exists(abs_path):
		return abort(404)

	# Check if path is a file and serve
	if os.path.isfile(abs_path):
		return send_file(abs_path)

	# Show directory contents
	files = os.listdir(abs_path)

	if search_string:
		files = [s for s in files if search_string in s]

	return render_template('index.html', files=files, search=search_string)

@app.route("/media/<filename>")
def media(filename=None):
	return render_template('media.html', filename=filename)

@app.route("/media_url/<filename>")
def media_url(filename):
	return send_from_directory(app.config['MEDIA_FOLDER'],filename)

@app.route('/service-worker.js')
def sw():
	return app.send_static_file('service-worker.js')