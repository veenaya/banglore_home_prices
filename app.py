from flask import Flask, request, jsonify , render_template
import util

app = Flask(__name__)

# @app.route('/get_location_names', methods=['GET'])
# def get_location_names():
#     list = None
#     response = {
#         'locations': util.get_location_names()
#     }
#     for key in response:
#         list = response[key]

#     return render_template('index.html' ,responses=list)

# @app.route('/app', methods=['GET'])
# def get_location_names_real():
#     list = None
#     response = {
#         'locations': util.get_location_names()
#     }
#     for key in response:
#         list = response[key]

#     return render_template('app.html' ,responses=list)

@app.route('/', methods=['GET', 'POST'])
def predict_home_price():
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

        #return print(list)
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
    util.load_saved_artifacts()
    app.run(debug=True) 



    