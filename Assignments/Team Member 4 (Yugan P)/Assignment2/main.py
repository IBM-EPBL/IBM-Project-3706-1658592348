from flask import Flask, redirect, render_template, request, url_for,session
import ibm_db
import re
app=Flask(__name__,template_folder='templates',static_folder='static')
app.secret_key = 'a'
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=21fecfd8-47b7-4937-840d-d791d0218660.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31864;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt; UID=rnb47287;PWD=FVzMWkFKvvqhHQwR;",'','')

@app.route('/login',methods=['GET','POST'])
def login():
    global userid
    msg="  "
       
    
    if request.method == 'POST' :
        username = request.form['username']
        passwd = request.form['passwd']
        sql = "SELECT * FROM USER WHERE username =? AND passwd=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,passwd)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account['USERNAME']
            userid=  account['USERNAME']
            session['username'] = account['USERNAME']
            msg = 'Logged in successfully !'
            return render_template('wel.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)


@app.route('/register', methods =['GET', 'POST'])
def register():
    msg =" "
    if request.method == 'POST' :
        username = request.form['username']
        roll_no = request.form['roll_no']
        email = request.form['email']
        passwd = request.form['passwd']
        sql = "SELECT * FROM USER WHERE username =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            insert_sql = "INSERT INTO  USER VALUES (?, ?, ?, ?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, roll_no)
            ibm_db.bind_param(prep_stmt, 2, username)
            
            ibm_db.bind_param(prep_stmt, 3, email)
            ibm_db.bind_param(prep_stmt, 4, passwd)
            ibm_db.execute(prep_stmt)
            msg = 'You have successfully registered !'
            return render_template('register.html',msg=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

    
if __name__ == '__main__':
   app.run()
