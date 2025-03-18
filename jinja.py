from flask import Flask, render_template,request
           #Creates an instance of the Flask class, WSGI application

#WSGI Application
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/success/<score>')
def success(score):
    return "your score:"+score

if __name__=="__main__":
    app.run(debug=True)