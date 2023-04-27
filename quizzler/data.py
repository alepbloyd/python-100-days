import requests

trivia_api_params = {
    "amount": 10,
    "type": "boolean"
}

trivia_api_response = requests.get(url="https://opentdb.com/api.php", params=trivia_api_params)

question_data = trivia_api_response.json()['results']