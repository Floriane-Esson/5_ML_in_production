import requests

# We have put the localhost URL as default, feel free to change it
ENDPOINT = "http://127.0.0.1:5000/predict"

# This a simple example of input
input_simple = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
}

# This a example of input with several inputs
input_multiple = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8],
              [5.0, 0.98, 0.32, 18.9, 0.050, 75.0, 122.0, 0.401, 3.1, 0.21, 1.2]]
}

#Test 1
testok1 = requests.post(ENDPOINT, json=input_simple)
assert testok1.status_code == 200
print(testok1, testok1.json())

Test 2
testok2 = requests.post(ENDPOINT, json=input_multiple)
assert testok2.status_code == 200
print(testok2, testok2.json())

#Test 3
test_ko_no_json = requests.post(ENDPOINT, data={"input": 5, "alcohol": "9.5"})
print(test_ko_no_json, test_ko_no_json.json())

#Test 4
test_ko_missing_input = requests.post(ENDPOINT, json={"alcohol": "9.5"})
print(test_ko_missing_input, test_ko_missing_input.json())

