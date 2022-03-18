from flask import Flask
from flask import render_template
import random
from datetime import date
import requests


app = Flask(__name__)


@app.route("/")
def hello_world():
    c_year = date.today().year

    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, year=c_year)


@app.route("/guess/<some_name>")
def guess(some_name):

    # Age API
    age_url = "https://api.agify.io"
    age_parameters = {
        "name": some_name
    }
    age_response = requests.get(url=age_url, params=age_parameters)
    age_response.raise_for_status()
    age_data = age_response.json()
    age_guess = age_data["age"]

    # Gender API
    gender_url = "https://api.genderize.io"
    gender_parameter = {
        "name": some_name
    }
    gender_response = requests.get(url=gender_url, params=gender_parameter)
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender_guess = gender_data["gender"]

    return render_template("guess.html", name=some_name, gender=gender_guess, age=age_guess)





if __name__ == "__main__":
    app.run()
