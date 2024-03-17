from flask import Flask,render_template
app = Flask(__name__)

@app.route('/check')
def check():
    return render_template('emplates_inheritance2.html')
@app.route('/')
def hello_world():
    return render_template('emplates_inheritance1.html')


if __name__ == '__main__':
    app.run(debug=True)