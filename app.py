from flask import (Flask, redirect, make_response, request, redirect, url_for, render_template)
import os
from py2neo import Graph, Node, Relationship

url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')
graph = Graph(url + '/db/data/')

app = Flask(__name__)
app.secret_key= 'some_secret_key'

def get_data(q = None):
    if q == None or  q == "*":
        query = """
        MATCH (m:Movie) RETURN m.released as year, m.title as title, m.tagline as tagline order by year desc
        """
        return graph.cypher.execute(query)
    else:
        query = """
        MATCH (m:Movie) where toString(m.released+" "+m.title+" "+ m.tagline) =~ { s } RETURN m.released as year, m.title as title, m.tagline as tagline order by year desc
        """
        return graph.cypher.execute(query, s="(?i).*" + q + ".*")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        data = get_data()
        return render_template('index.html', data=data)
    elif request.method == 'POST':
        data = get_data(request.form['search'])
        return render_template('index.html', data=data)

if __name__ == '__main__':
	app.run(
		debug = True,
		host = '0.0.0.0',
		port = 8080
	)
