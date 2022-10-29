from flask import Flask,render_template,request
app= Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('register.html')

@app.route("/confirm",methods=['POST','GET'])
def register():
    if request.method=='POST':
        n = request.form.get('uname')
        a = request.form.get('email')
        c = request.form.get('contact')
        return render_template('confirm.html',uname=n,email=a,contact=c)
if __name__=="__main__":
    app.run(debug=True)