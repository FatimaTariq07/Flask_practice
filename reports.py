from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('forms_exercise.html')

@app.route('/report')
def report():
    lower_letter = False
    upper_letter = False
    num_ends = False
    
    user_name = request.args.get('username')
    lower_letter = any(i.islower() for i in user_name)
    upper_letter = any(i.isupper() for i in user_name)
    num_ends = user_name[-1].isdigit()
    report = lower_letter and upper_letter and num_ends
    return render_template('reportss.html',report=report,lower_letter=lower_letter,upper_letter=upper_letter,num_ends=num_ends)


if __name__ == '__main__':
    app.run(debug=True)
