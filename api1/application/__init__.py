from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/animal/noise', methods=['GET'])
def get_noise():
    animal = requests.get('http://service2:5001/get/animal')
    animal_text = animal.text
    if animal_text == 'Dog':
        noise = 'Bark'
    elif animal_text == 'Cow':
        noise = 'Moove'
    elif animal_text == 'Cat':
        noise = 'Sigh'
    else:
        noise = 'I am a horse'
    return render_template('home.html', title='Animal Noise', animal=animal_text, noise=noise)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
