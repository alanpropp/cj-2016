from flask import Flask
from flask import render_template
from datafoo import get_data
app = Flask(__name__)
recalls_data = get_data()
@app.route("/")
def homepage():
    return render_template('homepage.html',
            recalls=recalls_data,
            recalls_count=len(recalls_data))
    
if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
