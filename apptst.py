from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/")

def hello():
	return "hi hesam"

@app.route("/index<path>")
def hell(path):
	num = 2
	return f"hiogujg {path}ghjjjjjjf{num}"

@app.route("/weather")

def helli():
	return render_template (
		'tst2.html')

if (__name__ =="__main__"):
    app.run(debug=True)
