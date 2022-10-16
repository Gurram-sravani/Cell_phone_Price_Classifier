from flask import Flask, render_template, request, jsonify # importing library
import pickle # it helps to load the model
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__) # Creating app

model = pickle.load(open(r"Cell_Phone_Price_SVM.pkl","rb")) # open model in read mode
@app.route('/',methods=['GET']) # If someone hitting the webside that time method will be get
def Home():
    return render_template('index.html') #Pushing the UI or html code

#Start Preprocessing
standard_to = StandardScaler()
@app.route("/predict",methods=['POST']) # Collect the inputs
def predict():
    if request.method == 'POST':
        ram = int(request.form['ram'])
        px_height = int(request.form['px_height'])
        battery_power= int(request.form['battery_power'])
        px_width = int(request.form['px_width'])
        mobile_wt = int(request.form['mobile_wt'])
        int_memory = int(request.form['int_memory'])
        sc_w = int(request.form['sc_w'])
        talk_time = float(request.form['talk_time'])
        sc_h= float(request.form['sc_h'])
        pc = int(request.form['pc'])
        n_cores = float(request.form['n_cores'])
        touch_screen = float(request.form['touch_screen'])
        fc = int(request.form['fc'])
        four_g = int(request.form['four_g'])
        m_dep = float(request.form['m_dep'])
        blue = int(request.form['blue'])
        clock_speed = float(request.form['clock_speed'])
        dual_sim = int(request.form['dual_sim'])
        wifi = int(request.form['wifi'])
        three_g = int(request.form['three_g'])


        prediction = model.predict(np.array([[ram,px_height,battery_power,px_width,mobile_wt,int_memory,sc_w,talk_time,sc_h,pc,n_cores,touch_screen,fc,
                       four_g,m_dep,blue,clock_speed,dual_sim,wifi,three_g]]).reshape(1,13))

        output = round(prediction[0],2) # Predict the model with condition

        if output == 0: # Condition for output
            return render_template('index.html',pred="The Phone is Low Cost") # Connect ot html page and app
        elif output == 1:
            pred = "The Phone is Medium Cost  ".format(output)
            return render_template('index.html', pred=pred)
        elif output == 2:
            pred = "The Phone is High Cost  ".format(output)
            return render_template('index.html', pred=pred)
        else:
            pred = "The Phone is Very High Cost  ".format(output)
            return render_template('index.html', pred=pred)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000,debug=True)