from flask import Flask, render_template, request
import numpy as np
import joblib



app = Flask(__name__)

model = joblib.load('fashion-mnist-train-2.csv_trained_model.joblib')
labels = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_data = request.form['image_data']

        pixels = np.array([int(pixel) for pixel in image_data.split(',')])

        if len(pixels) != 784:
            return 'Error: Input data must contain 784 pixels (28x28), {} given'.format(len(pixels))

        pixels = pixels.reshape(1, 784)

        prediction = model.predict(pixels)

        class_label_index = prediction[0]
        class_label = labels[class_label_index]

        return str(class_label)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

