import pyrebase
import json

firebaseConfig = {
  "apiKey" : "AIzaSyCkSrcM_uaRXIgv28kWY87GtO-INPKV50Q",
  "authDomain": "nalaya-thiran.firebaseapp.com",
  "projectId": "nalaya-thiran",
  "storageBucket": "nalaya-thiran.appspot.com",
  "messagingSenderId": "459550695630",
   "databaseURL": "https://nalaya-thiran-default-rtdb.firebaseio.com",
  "appId": "1:459550695630:web:1034ea2149c05701ae309f",
  "measurementId": "G-8LJT4YBKYZ"
}


firebase = pyrebase.initialize_app(firebaseConfig)

def signing_up(email, password):
    auth = firebase.auth()
    try:
        auth.create_user_with_email_and_password(email, password)
        print('Created user ', email)
        return 1
    except Exception:
        traceback.print_exc()
        return 0


def signing_in(email, password):
    auth = firebase.auth()
    try:
        auth.sign_in_with_email_and_password(email, password)
        print('Signed in as ', email)
        return 1
    except Exception:
        traceback.print_exc()
        return 0
        
def addUserToDatabase(userObj):
    jsonObj = json.loads(json.dumps(userObj))
    ref = firebase.database().child("users")
    ref.push(jsonObj)
    return jsonObj

