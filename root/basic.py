from flask import Flask, render_template, request
from pymongo import Connection
import json
from bson import json_util
from forms import Query


app = Flask(__name__)
app.config.from_object('config')
connection = Connection()
db = connection.mydb
collection = db.elements
cursor = collection.find()


@app.route('/')
def main_page(): 
	documents = []
	for document in cursor:
		json_doc = json.dumps(document, default=json_util.default)
		documents.append(json_doc)
	return render_template("main_page.html", dictionary = documents)

@app.route('/query', methods = ['GET', 'POST'])
def query():
	form = Query()
	documents = []
	if request.method == "POST":
		splitData = form.query.data.split()
		if splitData[2].isdigit():
			tempDict= {splitData[0] : int(splitData[2])}
		else:
			tempDict= {splitData[0] : splitData[2]}
		cursor = collection.find(tempDict)
		for document in cursor:
			json_doc = json.dumps(document, default=json_util.default)
			documents.append(json_doc)
		return render_template("main_page.html", dictionary = documents)
	return render_template('query.html', form= form)



if __name__ == '__main__':
	app.run(debug=True)