from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    datasets = [
        {'filename': 'foo.csv',
         'keywords': ['fish', 'eggs']},
        {'filename': 'bar.csv',
         'keywords': ['jellyfish', 'babies']}
    ]
    return render_template('index.html',
                           title='Home',
                           datasets=datasets)

if __name__ == '__main__':
  app.run(debug=True)
