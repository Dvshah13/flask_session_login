from flask import Flask, session, render_template, request, redirect
import pg

db = pg.DB(host="localhost", user="postgres", passwd="rockets", dbname="users")
db.debug = True

app = Flask('MyLogin')
app.secret_key = "asdfasdf"

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'Logged Out!'

@app.route('/new_user', methods=['GET'])
def new_user():
    return render_template("new_user.html")

@app.route('/new_user_submit', methods=['GET', 'POST'])
def new_user_submit():
    username=request.form.get('username')
    password=request.form.get('password')
    password1=request.form.get('password1')
    if password == password1:
        db.insert('users', username = username, password = password)
        return redirect('/')
    else:
        return redirect("/new_user")

@app.route('/submit_login', methods=['POST'])
def submit_login():
    username = request.form.get('username')
    password = request.form.get('password')
    query = db.query("select * from users where username = '%s'" % username)
    result_list = query.namedresult()
    if len(result_list) > 0:
        user = result_list[0]
        if user.password == password:
            session['username'] = user.username
            session['logged in'] = True
            return render_template("sucess.html")
        else:
            return redirect('/')
    else:
        return render_template("login_fail.html")

if __name__ == '__main__':
    app.run(debug=True)
