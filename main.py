#!/usr/bin/env python3

from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route("/")
def getHome():
	return render_template('template.html')

@app.route("/postes")
def getPostes():
	postes = {
		1: {
			"company": "SuperDuperCool Corp",
			"title": "Support IT",
			"description": "Support informatique, expérience sur Windows et Active Directory préférable",
			"start": "16-09-2022",
			"length": 0.5
 		},
 		2: {
 			"company": "XPLT Inc",
 			"title": "Consultant sécurité",
 			"description": "Consultant sécurité avec une expérience de 5 ans mini",
 			"start": "18-07-2022",
 			"length": "CDI"
 		}
	}

	return render_template('postes.html', postes=postes)

@app.route("/uploadcv", methods=["GET", "POST"])
def sendCV():
	error = False
	if request.method == 'POST':
		file = request.files['file']
		file.save(f'./uploads/{secure_filename(file.filename)}')
		if ": PDF document, version" not in os.popen(f'file ./uploads/{secure_filename(file.filename)}').read():
			os.system(f'rm ./uploads/{secure_filename(file.filename)}')
			error = True
	return render_template('template.html', error=error)

if __name__ == '__main__':
	app.run(debug=True)
