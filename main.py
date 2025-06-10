from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# HTML template (you can also put this in a separate file)

@app.route('/')
def index():
    """Render the form page"""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    result = data
    print("this is map: ",request.get_json())
    return render_template('index.html')


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
    app.run(port=5500,debug=True)