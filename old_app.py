# Import flask
from old_app import flask, render_template, request, redirect, url_for
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
        exp = request.form['exp']
        X = [[float(exp)]]
        [prediction] = loaded_model.predict(X)
        gpa = round(prediction, 2)
    if sex == 1:
        gender = "Male"
    else:
        gender="Female"    
    msg = "Expected first year college gpa for a " + gender + \
    " with a SAT Math score of " + str(sat_m) + \
    ", SAT Verbal score " + str(sat_v) + \
    ", and high school GPA of " + str(hs_gpa) + \
    ", would be:  " + str(gpa) + "/-- "

    return render_template("index.html", prediction_text= msg)
if __name__ == '__main__':
    app.run(  debug=True)