from flask import Flask ,render_template,request
import requests
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/wheather',methods=['POST'])
def wheather_api():
    location = request.form.get('Location')

    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    location = location
    querystring = {"q": location}  # Change to "Hyderabad"

    headers = {
        "x-rapidapi-key": "f7d72d2b2cmsh101a3a0f4ef24bdp109fafjsn0b175e4ccd08",
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        res = response.json()
        return render_template('index.html', response=res)
    except Exception as e:
        # Handle API or network errors gracefully
        error_message = f"An error occurred: {str(e)}"
        return render_template('index.html', error=error_message)

if __name__ == "__main__":
    app.run(debug=True)