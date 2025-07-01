from flask import Flask, request, render_template, jsonify
from firebase_setup_py import CreateFirebaseUser

app = Flask(__name__)

# path/to/serviceAccountKey.json

@app.route('/')
def index():
    """Render the form page"""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()

    user = CreateFirebaseUser(data = data)
    user.createUser()
    
    return render_template("index.html")


# Error handling
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Enable debug mode for development
    app.run(port = 5500, debug = True)


# {'name': 'Shashwat', 'email': 'sh10ashwat@gmail.com', 
# 'phone': '654738', 'experience': 'beginner', 'goal': 'reyyrthfg'}


# todo
'''
send user data to the firebase file
have it check and return if the user already has a account based on the email
if yes then do not create another user or send an email to him again
possibly tell him that you already have signed up

'''