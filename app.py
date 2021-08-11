from flask import Flask, request , render_template
import sys
import util

import logging



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict_home_price():

    if request.method == 'POST':
        total_sqft = float(request.form.get('uiSqft', False))
        location = str(request.form.get('responses', False))
        bhk = int(request.form.get('radio_bhk', False))
        bath = int(request.form.get('radio_bath', False))

        list = {
            'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
        }
        for key in list:
                lists = list[key]
                lists = str(lists) + "Lakh"
        
        response = {
            'locations': util.get_location_names()
            }
        for key in response:
                place = response[key]

        #return print(list)
        return render_template('app.html', post=lists, responses=place)
    elif request.method == 'GET':
            response = {
            'locations': util.get_location_names()
            }
            for key in response:
                place = response[key]
                
            return render_template('app.html' ,responses=place)

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True) 


app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)



    