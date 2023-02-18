from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
model=pickle.load(open("heart.pkl","rb"))

@app.route('/',methods=['GET'])
def home():
	return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
	if request.method=='POST':
		age=int(request.form['age'])
		Anaemia=request.form['Anaemia']
		if Anaemia=='Yes':
			Anaemia=1
		else:
			Anaemia=0
		Creatinine=int(request.form['Creatinine'])
		Diabetes=request.form['Diabetes']
		Ejection_Fraction=int(request.form['Ejection_Fraction'])
		High_Blood_Pressure=request.form['High_Blood_Pressure']
		if High_Blood_Pressure=='Yes':
			High_Blood_Pressure=1
		else:
			High_Blood_Pressure=0
		Platelets=int(request.form['Platelets'])
		Serum_Creatinine=request.form['Serum_Creatinine']
		Serum_Sodium=int(request.form['Serum_Sodium'])
		Gender=request.form['sex']
		if Gender=='Male':
			Gender=1
		else:
			Gender=0
		Smoking=request.form['Smoking']
		if Smoking=='Yes':
			Smoking=1
		else:
			Smoking=0
		Time=int(request.form['Time'])
		output=model.predict([[age,Anaemia,Creatinine,Diabetes,Ejection_Fraction,High_Blood_Pressure,Platelets,Serum_Creatinine,Serum_Sodium,Gender,Smoking,Time]])
		if output==0:
			return render_template("dead.html")
		else:
			return render_template('pass.html')
if __name__=="__main__":
    app.run(debug=True)

