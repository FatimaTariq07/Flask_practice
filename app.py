from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DateTimeField,BooleanField,RadioField,SelectField,TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'

class FormInfo(FlaskForm):
    breed = StringField("What breed do you have?",validators=[DataRequired()])
    
    nutrient = BooleanField("Have Your puppy is nutreinted?")
    
    mood = RadioField("Please choose your moood?",choices=[('mood_one','happy'),('moood_two','excited'),('moood_three','angery')])
    
    food_choices = SelectField("Please choose your Food?",choices=[('chi','chicken'),('bf','Beaf')])
    feedback = TextAreaField()
    
    submit = SubmitField("Click me")

@app.route('/',methods=['GET','POST'])
def index():
    form = FormInfo()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['nutrient'] = form.nutrient.data
        session['mood'] = form.mood.data
        session['food_choices'] = form.food_choices.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thankyou'))
    return render_template('index.html',form=form)
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

# this is necessaary when you want to run this app only from this file
if __name__ == '__main__':
    app.run(debug=True)