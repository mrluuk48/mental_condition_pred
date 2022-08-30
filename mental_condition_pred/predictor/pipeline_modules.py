from abc import ABC, abstractmethod
import json


class PipelineModule(ABC):
    """abstract class for Pipeline Modules"""
    def __init__(self):
        self.request = None
        self.config = json.load(open('config.json', 'r', encoding='utf-8'))

    @abstractmethod
    def predict(self):
        """function that is called from API and returns enriched request object"""
        return self.request

    def load_request(self, req):
        self.request = req
        return self


class Query(ABC):
    def __init__(self, req, timestamp=''):
        self.id = req.get('id', None)
        self.HeartDisease = req.get('HeartDisease', None)
        self.BMI = req.get('BMI', None)
        self.Smoking = req.get('Smoking', None)
        self.AlcoholDrinking = req.get('AlcoholDrinking', None)
        self.Stroke = req.get('Stroke', None)
        self.PhysicalHealth = req.get('PhysicalHealth', None)
        self.DiffWalking = req.get('DiffWalking', None)
        self.Sex = req.get('Sex', None)
        self.AgeCategory = req.get('AgeCategory', None)
        self.Race = req.get('Race', None)
        self.Diabetic = req.get('Diabetic', None)
        self.PhysicalActivity = req.get('PhysicalActivity', None)
        self.GenHealth = req.get('GenHealth', None)
        self.SleepTime = req.get('SleepTime', None)
        self.Asthma = req.get('Asthma', None)
        self.KidneyDisease = req.get('KidneyDisease', None)
        self.SkinCancer = req.get('SkinCancer', None)
        self.predicted_mental_condition = None
        self.mapping_timestamp = timestamp

