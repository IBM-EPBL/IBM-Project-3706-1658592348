from flask import Flask,render_template,request
app= Flask(__name__,template_folder='templates',static_folder='staticFiles')

@app.route('/')
def home():
    return render_template('objects.html')

if __name__=="__main__":
    app.run(debug=True)