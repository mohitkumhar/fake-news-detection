from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)


model = pickle.load(open('model code/model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['newsInput']
    
    input_data = pd.DataFrame(
        {
            'text': [text]
        }
    )
    
    predict = model.predict(input_data)
    
    print(predict)
    
    
    return render_template('index.html', result='Fake News' if predict == 0 else 'True News')



if __name__ == '__main__':
    app.run(debug=True)