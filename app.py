from flask import Flask, render_template, request
from database import signing_in, signing_up, addUserToDatabase
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    userObj = dict()
    #If an seperate function is required, the below method contains the parrameteric values
    # matter = request.form.listvalues()
    name = request.form.get("name")
    password = request.form.get("password")
    age = request.form.get("age")
    userObj["name"] = name
    userObj["age"] = age
    try:
        signing_up(name, password)
        addUserToDatabase(userObj)
    except Exception as e:
        print(e.__cause__)
        return render_template('error.html')
    return "Success"


if __name__ == '__main__':
    app.run()