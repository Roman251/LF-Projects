import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

model_internship = pickle.load(open('model/internship.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    For rendering results on HTML GUI
    """

    input_features = [float(val) for val in request.form.values()]
    final_features = [np.array(input_features)]
    prediction = model_internship.predict(final_features)

    sale = round(prediction[0], 2)

    return render_template('index.html', prediction_text="The Estimated Sale is : {}".format(sale))

# is the file being directly run or imported
if __name__=='__main__':
    app.run(debug=True)

