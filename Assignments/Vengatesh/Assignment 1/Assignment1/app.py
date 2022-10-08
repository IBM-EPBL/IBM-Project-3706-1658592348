from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/view', methods = ['POST', 'GET'])
def view():
    if request.method == 'POST':
        view = request.form
        return render_template("view.html", result = view)

if __name__ == '__main__':
    app.run(debug = True)