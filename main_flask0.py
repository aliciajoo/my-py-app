from flask import Flask , render_template, request
from tweets import getTweets

app = Flask("Test")

@app.route("/")
def default():
	m = "Brexit Watcher"
	return render_template("index.html", message=m)

@app.route("/brexit")
def handle_tweets():
	data = getTweets()
	print data
	return render_template("brexit.html", data=data)

if __name__ == "__main__":
	app.run()
