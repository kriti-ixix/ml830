#Importing the libraries
import pickle
from flask import Flask, render_template, request

#Global Variables
app = Flask(__name__)
loadedModel = pickle.load(open('ecommerce model.pkl', 'rb'))

#User-defined functions/ API Routes
@app.route('/', methods=['GET'])
def Home():
    return render_template('ecom.html')

@app.route('/prediction', methods=['POST'])
def predict():
    session = float(request.form['session'])
    app_time = float(request.form['app'])
    website_time = float(request.form['website'])
    membership = float(request.form['membership'])

    prediction = loadedModel.predict([[session, app_time, website_time, membership]])[0]

    prediction = "$ " + str(round(prediction, 2))

    return render_template('ecom.html', output=prediction)

#Main function
if __name__ == '__main__':
    app.run(debug=True)