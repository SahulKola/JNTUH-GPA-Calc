from flask import Flask,render_template,url_for,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def dashboard():
    return render_template('home.html')
@app.route('/results')
def results():
    return render_template('results.html')
    
@app.route('/calc-gpa')
def calcgpa():
    return render_template('calc-gpa.html')
    
@app.route('/target-gpa-calc')
def gpaplanner():
    return render_template('target-gpa-calc.html')
    
@app.route('/how-it-works')
def howitworks():
    return render_template('how-it-works.html')

if __name__ == "__main__":
    app.run(debug=True,port=8080)
