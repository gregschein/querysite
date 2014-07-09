from flask.ext.wtf import Form
from wtforms import TextField

class Query(Form):
	query = TextField('query')