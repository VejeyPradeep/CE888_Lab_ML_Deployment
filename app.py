from flask import Flask, request, render_template
import os
import pickle

print(os.getcwd())
path = os.getcwd()

with open('Trained_Random_class_model.pkl', 'rb') as f:
    logistic = pickle.load(f)

def get_predictions(price, Tax, Driver_Age, Licence_Length_Years, req_model):
    mylist = [Driver_Age, Tax, price, Licence_Length_Years]
    mylist = [float(i) for i in mylist]
    vals = [mylist]

   if req_model == 'RandomForest':
        #print(req_model)
        return randomforest.predict(vals)[0]
    else:
        return "Cannot Predict"


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    price = request.form['price']
    Tax = request.form['Tax']
    Driver_Age = request.form['Driver_Age']
    Licence_Length_Years = request.form['Licence_Length_Years']
    req_model = request.form['req_model']

    target = get_predictions(price, Tax, Driver_Age, Licence_Length_Years, req_model)

    if target==1:
        sale_making = 'Customer is likely to buy the insurance'
    else:
        sale_making = 'Customer is unlikely to buy the insurance'

    return render_template('home.html', target = target, sale_making = sale_making)


if __name__ == "__main__":
    app.run(debug=True)
