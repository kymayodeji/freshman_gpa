# Import flask
from old_app import Flask, render_template, request
from sklearn.externals import joblib

# Instantiate Flask object and load model
app = Flask(__name__)
loaded_model = joblib.load('model.pkl')

# Direct app to url index.html
@app.route("/")
def root():
    return render_template("index.html")
@app.route("/predict", methods=['POST'])

# Set up inference results
def make_prediction():

    if request.method == 'POST':
        sex = request.args.get("sex")
        sat_m =request.args.get("sat_m")
        sat_v =request.args.get("sat_v")
        hs_gpa =request.args.get("hs_gpa")
        X = [[float(sex), float(sat_m), float(sat_v), float(hs_gpa)]]
       
        [prediction] = loaded_model.predict(X)
        gpa = round(prediction, 2)
        if sex == 1:
            gender = "Male"
        else:
            gender="Female"
    msg = "Expected first year college gpa is " + str(gpa) + " for a " + gender + \
            " with a SAT Math score of " + str(sat_m) + \
            ", SAT Verbal score " + str(sat_v) + \
            ", and high school GPA of " + str(hs_gpa) + \
            ", would be:  " + str(gpa) + "/-- "

    return render_template("index.html", prediction_text= msg)
if __name__ == '__main__':
    app.run(  debug=True)