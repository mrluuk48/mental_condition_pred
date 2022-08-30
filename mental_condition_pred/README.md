# Mental condition classifier FLASK API

### Overview
Classifier serves a random forest model to predict mental condition of a person based on input data

 0   HeartDisease      
 1   BMI               
 2   Smoking           
 3   AlcoholDrinking   
 4   Stroke            
 5   PhysicalHealth     
 7   DiffWalking       
 8   Sex               
 9   AgeCategory       
 10  Race              
 11  Diabetic          
 12  PhysicalActivity  
 13  GenHealth         
 14  SleepTime         
 15  Asthma             
 16  KidneyDisease     
 17  SkinCancer        

Output: 1 (mental condition predicted) or 0 (healthy mental predicted)
### How to read the project:
- Start with: The EDA and training script  in jupyter notebook **Mental_health_condition_training.html**, the original notebook is also in the same folder
- After that: Comeback here and continue the following instruction for model deployment.

### Structure of project:
model/: random forest model trained
config.json: config file
prreprocessing_module: preprocessing module for incoming data including encoder and scaling
pipeline_modules: module to define fields in input and output request and the object req which contains all the features that can be passed among modules
model_module: use trained random forest model, predict mental_condition either 1 or 0
model_serve: calling model_module and preprocessing_module to process input and do prediction
predictor: Flask interface that calls model_serve to process input and return output

### To run the project, run following in terminal:
Start with docker build and run docker image and expose it to a local port
```bash
docker build .

docker run -p 8080:8080  <Image name just get created>
```

Fire off requests with the following curl command format: (In case text with single quotation, wrap it around escape char)
```bash
curl --header "Content-Type: application/json" --request POST --data '{"HeartDisease":"No","BMI":16.6,"Smoking":"Yes","AlcoholDrinking":"No","Stroke":"No","PhysicalHealth":3.0,"DiffWalking":"No","Sex":"Female","AgeCategory":"55-59","Race":"White","Diabetic":"Yes","PhysicalActivity":"Yes","GenHealth":"Verygood","SleepTime":5.0,"Asthma":"Yes","KidneyDisease":"No","SkinCancer":"Yes","Mental_condition":1}' http://0.0.0.0:8080/invocations | python -m json.tool
```
