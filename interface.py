from project_app.utils import Admission
from flask import Flask, jsonify,render_template,request
import config
import numpy as np

app = Flask(__name__)

##########################################################
####################### BASE API #########################
##########################################################

@app.route('/')
def admin_model():
    print('Welcome to admission model')
    return render_template('index.html')

# @app.route('/predict',methods=['POST'])
# def predict(self):
#     '''
#     For rendering results on HTML GUI
#     '''
#     int_features = [float(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = self.model.predict(final_features)

#     output = round(prediction[0]*100, 2)

#     return render_template('admin.html', prediction_text='Expected Probablity of your admission is {}'.format(output))



@app.route('/admission_chance',methods=['POST'])
def abc():
    # '''
    # For direct API calls trought request
    # '''
    # data = request.get_json(force=True)
    # prediction = self.model.predict([np.array(list(data.values()))])

    # output = prediction[0]
    # return jsonify(output)
    data=request.form
    GRE_Score = data['GRE_Score']
    TOEFL_Score = data['TOEFL_Score']
    University_Rating = data['University_Rating']
    SOP = data['SOP']
    LOR = data['LOR']
    CGPA = data['CGPA']
    
    admin1=Admission(GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA)
    result = admin1.get_admission()
    return jsonify({'result': f"Chances of getting admission : {result*100 }"},'%')

if __name__ =='__main__':
    app.run(host='0.0.0.0',port =9000)