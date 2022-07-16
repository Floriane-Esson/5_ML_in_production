{{floriane.esson@gmail.com}}

{{https://share.vidyard.com/watch/8qKu5TnmiV6ubbhfZ5MMa6?}}

# ML in production

URL adress of the Heroku app : https://wine-o-meter-fess.herokuapp.com

**Wine-o-meter** is a future unicorn application. It allows wine producers to predict the quality score of their wine based on physicochemical inputs. The startup behind this innovation is convinced about its ability to disrupt the world of wine. 🍷

## Project 🚧

The data-science team has worked together on creating the best model predicting the quality score (from 0 to 10) of multiple wines. The next step is to include this model into the mobile application. The development team is expecting an API endpoint in order to request the model and display the result inside the application.

## ENDPOINT / PREDICTION

expected input : json file with "input" in key and array of values. 

Output : json with prediction of quality (from 0 to 10)

### Test the app 

1.on shell 
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]}' https://wine-o-meter-fess.herokuapp.com/predict
```

2. Or Python:

```python
import requests

response = requests.post("https://wine-o-meter-fess.herokuapp.com/predict", json={
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
})
print(response.json())
```

3. Or, other tips. You can POST your request on Postman https://web.postman.co in the Workspace

POST URL : ```https://wine-o-meter-fess.herokuapp.com/predict```

content on body : 
```{"input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]}```

## Create your own API Wine-O-Meter 🍷

1. Clone the repo GitHub with command on your directory :
    ``` $ git clone https://github.com/Floriane-Esson/5_ML_in_production.git ```

2. Create your virtual env with :
    ``` $ pip install virtualenv ```
    ``` $ virtual env virt ```
    ``` $ source virt/bin/activate ```

3. Install all requirements with :
    ```$ pip install -r requirements.txt ```

4. Run the app server :
    ```$ python app.py ```

5. On an other command shell, run the test :
    ```$ python test.py ```

6. You can try to push it on Heroku 😉. 

GOOD LUCK ! 😃
