import pyrebase
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, firestore
from SendEmail import SendEmail

# Initialize Firebase Admin SDK

load_dotenv()

collection = "blog_website_user_data"

config = {
    "apiKey": os.getenv("YOUR_API_KEY"),
    "authDomain": "internship-project-9ca48.firebaseapp.com",
    "projectId": "internship-project-9ca48",
    "storageBucket": "internship-project-9ca48.firebasestorage.app",
    "messagingSenderId": "257811255847",
    "appId": "1:257811255847:web:e69d42ae6fde2de5b33402",
    "measurementId": "G-NNZ6DLBRE7",
    "databaseURL" : ""
}
cred = credentials.Certificate(os.getenv("private_key_path"))
firebase_admin.initialize_app(cred)
firebase = pyrebase.initialize_app(config)

class CreateFirebaseUser:
    def __init__(self,data):
        self.db = firestore.client()
        self.auth = firebase.auth()
        self.data = data
    
    def createUser(self):
        if self.ifUserExists() == True:
            return 
        self.auth.sign_in_anonymous()
        self.writeDataToDb()
        sendEmail = SendEmail(self.data["email"])
        sendEmail.send_email()
    
    def writeDataToDb(self):
        # setting the user email as the document id
        doc_ref = self.db.collection(collection).document(self.data['email'])
        doc_ref.set(self.data)

    
    def ifUserExists(self):
        for userEmail in self.db.collection(collection).get():
            print(userEmail)
            if self.data["email"] == userEmail.get('email'):
                print("within if : ",userEmail)
                return True
        return False
    
        



'''
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

'''

'''
idToken
eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg3NzQ4NTAwMmYwNWJlMDI2N2VmNDU5ZjViNTEzNTMzYjVjNThjMTIiLCJ0eXAiOiJKV1QifQ.eyJwcm92aWRlcl9pZCI6ImFub255bW91cyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9pbnRlcm5zaGlwLXByb2plY3QtOWNhNDgiLCJhdWQiOiJpbnRlcm5zaGlwLXByb2plY3QtOWNhNDgiLCJhdXRoX3RpbWUiOjE3NTEzNDk3NzIsInVzZXJfaWQiOiJqVzJHVUpablM3WTRyaU1LTW5vQlVMSElDOFgyIiwic3ViIjoialcyR1VKWm5TN1k0cmlNS01ub0JVTEhJQzhYMiIsImlhdCI6MTc1MTM0OTc3MiwiZXhwIjoxNzUxMzUzMzcyLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7fSwic2lnbl9pbl9wcm92aWRlciI6ImFub255bW91cyJ9fQ.g1H_ByupwsVl-3swl7SW4otP8YEoHGzS6Rtg4_aG9543opVX9R6GVfb3c3YVKUNMhLJEA7bbI0SIySkJkEigRlfWXkSUStnU8lwqsl8StNyQdEAOvYj4lYRLjvke5ZBCnCG7WcM1ovpcihy30sGAGtD30B_wG6SaYQ0mQ-DXha3jhXdlHZq_KgWl3Ibc-7i1M0nqHS81x2bhYPL6ebrZ59SBKcSnb3G-vIFbERfG_cEuoo3zQPAHfxJuaktFJDXGU81kD8ouqqXPidT5CiGtBWwnmz-gY9B6I-5MSSS5UoGXme7P80o5xN30h7P3KLt8W9q5Ky2ZBqP_iXEo1RbOog


refreshToken
AMf-vBwTTBKjxLyhXqeWzYaAElhPhQCf7KESklVrEdTAlQ-raQd87GZ5_ZnXVyX1NHzrUObILAFBqyk4ZppoiShDvyfn-4_UoZ-ug2HvgSrj6DDOuQmdFO3PVoDj2Hjb4MaVKQ-SfELBsD4ulafxTSAr7fH1ytKKMx6yLsGKEvIUGG9VwT78pqmJ5gDv4-GcHVHarEYq2JvnUyUpYqj16aZBEU-qmxB96Q


expiresIn
3600


localId
jW2GUJZnS7Y4riMKMnoBULHIC8X2

'''

'''
kind
identitytoolkit#GetAccountInfoResponse


users
[{'localId': 'yW3WNBMJAzafHrrBIqDTvFbpOTt1', 'lastLoginAt': '1751349952655', 
'createdAt': '1751349952655', 'lastRefreshAt': '2025-07-01T06:05:52.655Z'}]
'''

#info = auth.get_account_info(user['idToken'])



'''

for i in info:
    print(i)
    print(info[i])
    print("\n")

'''