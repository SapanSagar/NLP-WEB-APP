from flask import Flask,render_template,request,redirect,session
from db import Database
from nlp import code_nlp
app = Flask(__name__)   #creating object

dbo = Database()
nlpo=code_nlp()

app.secret_key="abcd"

@app.route('/')   #index Route
def index():
    #return "Welcome to my first Web App"
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html',message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html',message="Email already exists")
@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.search(email, password)

    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email/password')
@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/langdet')
def langdet():
    if session:
        return render_template('langdet.html')
    else:
        return redirect('/')



@app.route('/perform_langdetect',methods=['post'])
def perform_langdetect():
    if session:
        text = request.form.get('langdetect_text')
        response = nlpo.lang_detect(text)
        #print(response)


        return render_template('langdet.html',response=response)
    else:
        return redirect('/')
@app.route('/translation')
def translation():
    if session:
        return render_template('translation.html')
    else:
        return redirect('/')



@app.route('/perform_translation',methods=['post'])
def perform_translation():
    if session:
        text = request.form.get('translation_text')
        dest = request.form.get('translation_language')

        response = nlpo.translation(text,dest)
        #print(response)

       
        return render_template('translation.html',response=response)
    else:
        return redirect('/')

@app.route('/sentiment')
def sentiment():
    if session:
        return render_template('sentiment.html')
    else:
        return redirect('/')



@app.route('/perform_sentiment',methods=['post'])
def perform_sentiment():
    if session:
        text = request.form.get('sentiment_text')
        

        response = nlpo.sentiment(text)
        #print(response)

       
        return render_template('sentiment.html',response=response)
    else:
        return redirect('/')
    

@app.route('/logout')
def logout():
    
    return render_template('login.html')

if __name__=='__main__':
    #app.run(host='127.0.0.1',port=8080,debug=True)
    app.run(host='0.0.0.0',port=8080)
    