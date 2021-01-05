import pandas as pd
from flask import Flask, jsonify, request
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier

# load model
model = pickle.load(open('model.pkl','rb'))
for i in model:
    print (i) 
app
app = Flask(__name__)
def get_prediction_for_passenger(passenger):
    passenger_representation = pd.DataFrame(passenger[explanatory_vars].to_dict(), index=[0])
    return classifier.predict(passenger_representation)[0]


def annotate_passenger_with_survival_prediction(passenger):
    preprocessed_passenger = pre_process_single_passenger_data(passenger, passengers)
    passenger['SurvivalChance'] = get_prediction_for_passenger(preprocessed_passenger)

 #routes
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
	form = PredictorsForm(request.form)

def predict():
# get data
data = request.get_json(force=True)

@app.route('/api/survival/', methods=['GET'])
def get_passenger():

    serializer_fields = [
        'Name',
        'SurvivalChance',
    ] + explanatory_vars

    closest_passenger = find_closest_passenger(q_name=clean_text(request.args.get('name', '')))
    annotate_passenger_with_survival_prediction(closest_passenger)

    return app.response_class(
        response=closest_passenger[serializer_fields].to_json(),
        status=200,
        mimetype='application/json'
    )

   # convert data into dataframe
data.update((x, [y]) for x, y in data.items())
data_df = pd.DataFrame.from_dict(data)

    # predictions
results = model.predict(data_df)

    # send back to browser
output = {'results': int(results[0])}

    # return data
    return jsonify(results=output)

    if __name__ == '__main__':
    app.run(port = 5000, debug=True)