import pickle
import json
# import config
import numpy as np

class Admission():

    def __init__(self,GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA):
        self.GRE_Score = GRE_Score
        self.TOEFL_Score = TOEFL_Score
        self.University_Rating = University_Rating
        self.SOP = SOP
        self.LOR = LOR
        self.CGPA = CGPA

    def load_model(self):
        with open(r'C:\PYTHON\Lecture files\12_09_Linear_Regression_Model\project_app\Linear Model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        
        with open(r'C:\PYTHON\Lecture files\12_09_Linear_Regression_Model\project_app\Project Data.json', 'r') as f:
            self.json_data = json.load(f)

    def get_admission(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data['Columns']))
        test_array[0] = self.GRE_Score
        test_array[1] = self.TOEFL_Score
        test_array[2] = self.University_Rating
        test_array[3] = self.SOP
        test_array[4] = self.LOR
        test_array[5] = self.CGPA

        print('Test Array :', test_array)

        admission_pred = np.around(self.model.predict([test_array])[0],2)
        
        return admission_pred

if __name__ == '__main__':
    GRE_Score = 304
    TOEFL_Score = 97
    University_Rating = 4
    SOP = 3.0
    LOR = 4.0
    CGPA = 8.55
    admin = Admission(GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA)
    admin.get_admission()