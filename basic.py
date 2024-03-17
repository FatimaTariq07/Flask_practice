from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    user_logged_in = False,
    my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
    str_list = ['Dog','Cat','Puppy','Matkii']
    return render_template('basic.html',my_list=my_list,str_list=str_list,user_logged_in=user_logged_in)

if __name__ == '__main__':
    app.run(debug=True)