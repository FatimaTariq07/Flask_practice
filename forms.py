from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('forms.html')
@app.route('/signup_form')
def signup_form():
    return render_template('singup_form.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_not_found.html'),404

@app.route('/thanku')
def thanku():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thanku.html', first=first,last=last)

if __name__ == '__main__':
    app.run(debug=True)