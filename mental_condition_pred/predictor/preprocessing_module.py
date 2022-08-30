from pipeline_modules import PipelineModule
from sklearn import preprocessing
import pandas as pd

class PreprocessingModule(PipelineModule):
    """wrapper for Preprocessing module"""

    def __init__(self):
        super().__init__()

    def predict(self):
        """
        function that is called from API to enrich request with particular field

        :return:
        self.request object
        """
        self.request.preprocessed_input = self.process_input(self.request.HeartDisease,
                                                             self.request.BMI,
                                                             self.request.Smoking,
                                                             self.request.AlcoholDrinking,
                                                             self.request.Stroke,
                                                             self.request.PhysicalHealth,
                                                             self.request.DiffWalking,
                                                             self.request.Sex,
                                                             self.request.AgeCategory,
                                                             self.request.Race,
                                                             self.request.Diabetic,
                                                             self.request.PhysicalActivity,
                                                             self.request.GenHealth,
                                                             self.request.SleepTime,
                                                             self.request.Asthma,
                                                             self.request.KidneyDisease,
                                                             self.request.SkinCancer
                                                             )
        return self.request


    def process_input(self, HeartDisease, BMI, Smoking, AlcoholDrinking, Stroke,
                      PhysicalHealth, DiffWalking, Sex, AgeCategory, Race,
                      Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma,
                      KidneyDisease, SkinCancer):
        all_col = self.config['model']['data']['all_col']
        data = pd.DataFrame([[HeartDisease, BMI, Smoking, AlcoholDrinking, Stroke,
                             PhysicalHealth, DiffWalking, Sex, AgeCategory, Race,
                             Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma,
                             KidneyDisease, SkinCancer]], columns=all_col)
        # Label encoder
        lbl = preprocessing.LabelEncoder()
        cat_columns = self.config['model']['data']['cat_columns']

        data[cat_columns] = data[cat_columns].apply(lbl.fit_transform)

        # Scaling
        scaler = preprocessing.StandardScaler()
        data[all_col] = scaler.fit_transform(data[all_col])
        return data
