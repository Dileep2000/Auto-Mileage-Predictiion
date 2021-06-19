from MPG_Prediction import MPG_Prediction as MPG
import pandas as pd
from flask import Flask, session, redirect, url_for, request,render_template

app = Flask(__name__)
app.secret_key = 'hello world'


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('loggedin.html',username=username)
    return render_template('frontpage.html')

car=''
car_details=dict()
@app.route('/',methods=['POST'])
def Milage():
    car=request.form.get("car")
    car_details['Cylinders'] = request.form.get("Cylinders")
    car_details['Displacement'] = request.form.get("Displacement")
    car_details['Horsepower'] = request.form.get("Horsepower")
    car_details['Weight'] = request.form.get("Weight")
    car_details['Acceleration'] = request.form.get("Acceleration")
    car_details['Model Year'] = request.form.get("Model Year")
    car_details['Origin'] = request.form.get("Origin")
    Mileage=MPG.predict(pd.DataFrame(car_details,index=[0]))
    return render_template('home.html', Milage=Mileage, car=car)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return render_template('home.html')
    return render_template('login.html')



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)