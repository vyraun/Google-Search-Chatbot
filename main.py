from flask import Flask, render_template, request, jsonify
import os
from google import google

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
	message = str(request.form['messageText'])

	# kernel now ready for use
	while True:
	    if message == "quit":
	        exit()
	    else:
			search_results = google.search(message)
			bot_response = search_results[1].description
			print(bot_response)
			# print bot_response
			return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run(debug=True)