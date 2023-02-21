
from flask import Flask, render_template
from datetime import datetime

application = Flask(__name__)

@application.route('/')
def index():
    curentTimeAndDate = datetime.now()
    todaysDate = curentTimeAndDate.strftime("The date currently is %A, %B %d %Y")
    appOpenTime = curentTimeAndDate.strftime("%I:%M:%S %p")
    return render_template("index.html", date=todaysDate, time=appOpenTime)

if __name__ == "__main__":
    application.run(debug=True)