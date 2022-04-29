from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/get/animal', methods =['GET'])
def get_animal():
    animals = ['Dog', 'Cow', 'Cat', 'Horse']
    randomnum = random.randint(0,3)
    return Response(animals[randomnum], mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')