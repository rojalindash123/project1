import pyrebase
config = {
    'apiKey': "AIzaSyCf6-bwCFhwlEIUnB9iknsXp5TtvN5AvRU",
    'authDomain': "test3-44aae.firebaseapp.com",
    'databaseURL': "https://test3-44aae.firebaseio.com",
    'projectId': "test3-44aae",
    'storageBucket': "test3-44aae.appspot.com",
    'messagingSenderId': "762001228928",
    'appId': "1:762001228928:web:57fb68b28ca2099a035265",
    'measurementId': "G-LD795LELXW"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password('email','password')
db=firebase.database()