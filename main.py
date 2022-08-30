from flask import Flask, render_template
import datetime
import random
# initialize object
app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", year = current_year)





# run app, turn on debug
if __name__=="__main__":
    app.run(debug=True)