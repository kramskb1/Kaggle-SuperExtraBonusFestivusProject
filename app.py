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