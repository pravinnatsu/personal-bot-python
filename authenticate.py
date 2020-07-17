import pyrebase

config = {
    "apiKey": "AIzaSyDOUI-nKfhSTfvYTd8CHyehsbyOE48vGEc",
    "authDomain": "personal-bot-14b45.firebaseapp.com",
    "databaseURL": "https://personal-bot-14b45.firebaseio.com",
    "projectId": "personal-bot-14b45",
    "storageBucket": "personal-bot-14b45.appspot.com",
}

# initialise
firebase = pyrebase.initialize_app(config)

# Auth Instance
auth = firebase.auth()


class Authentication:

    @staticmethod
    def create_user_account(email, password):
        print('Authentication - Create User')
        auth.create_user_with_email_and_password(email, password)

    @staticmethod
    def log_user_account(email, password):
        print('Authentication - Log User')
        auth.sign_in_with_email_and_password(email, password)

    # decorators
    @staticmethod
    def check_for_password_length(password):
        if len(password) >= 7:
            return True
        else:
            return False
