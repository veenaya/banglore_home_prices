from flask import Flask, request , render_template
import util


import pickle
import json
import numpy as np

app = Flask(__name__)
util.load_saved_artifacts()
# __locations = []
# __data_columns = None
# __model = None


# def get_estimated_price(location, sqft, bhk, bath):
#     try:
#         loc_index = __data_columns.index(location.lower())  # .index() = get index location in ()
#     except:
#         loc_index = -1

#     x = np.zeros(len(__data_columns))
#     x[0] = sqft
#     x[1] = bath
#     x[2] = bhk
#     if loc_index >= 0:
#         x[loc_index] = 1

#     return round(__model.predict([x])[0], 2)


# def load_saved_artifacts():
    
#     print("loading saved artifacts...done")


# def get_location_names():
#     return __locations


# def get_data_columns():
#      return __data_columns



@app.route('/', methods=['GET', 'POST'])

def predict_home_price():

    # print("loading saved artifacts...start")
    # global __data_columns
    # global __locations

    # with open("./artifacts/columns.json", "r") as f:
    #     __data_columns = json.load(f)['data_columns'] # convert from json to dic and store in data_columns variable
    #     __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    # global __model
    # if __model is None:
    #     with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f: # open binary format for reading
    #         __model = pickle.load(f) # load pickle file and store in model variable

    if request.method == 'POST':
        total_sqft = float(request.form['uiSqft'])
        location = str(request.form['responses'])
        bhk = int(request.form['radio_bhk'])
        bath = int(request.form['radio_bath'])

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

        return render_template('app.html', post=lists, responses=place)
    else:
            response = {
            'locations': util.get_location_names()
            }
            for key in response:
                place = response[key]
                
            return render_template('app.html' ,responses=place)

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run(debug=True) 
    util.load_saved_artifacts()



    