from flask import Flask, render_template , jsonify

app = Flask(__name__)

openings = [
  {
    'id': 1,
    'Title': 'Data Analyst',
    'Location': 'Chennai',
    'salary': 1000000
  },
  {
    'id': 2,
    'Title': 'Software Engg',
    'Location': 'Pune',
    'salary': 5000000
  },
  {
    'id': 3,
    'Title': 'Machine Learning',
    'Location': 'Delhi',
  },
]


@app.route('/')
def fun():
  return render_template('home.html', jobs=openings)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(openings)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
