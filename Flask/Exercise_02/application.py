from flask import Flask, render_template, request, url_for

application = Flask(__name__)

@application.route('/')
def home():
    return render_template('home.html')

@application.route('/result')
def results(): 
    try:
        number = int(request.args.get('Number'))
        if number % 2 > 0:
            return render_template('result.html', results=f"{number} is an odd number.")
        else:
            return render_template('result.html', results=f"{number} is an even number.")
    except ValueError:
        return render_template('result.html', results=f"Error! Please enter a number")
if __name__ == '__main__':
    application.run(debug=True)