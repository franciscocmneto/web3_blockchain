import requests
import json

def post_request(url,data):
    try:
        # Send the POST request
        response = requests.post(url, json=data)

        # Check the response status code
        if response.status_code == 200:
            # Request successful
            print("POST request successful!")
            print("Response data:", response.json())
        else:
            # Request failed
            print(f"POST request failed with status code {response.status_code}:")
            print(response.text)

    except requests.exceptions.RequestException as e:
        # Request exception (e.g., connection error)
        print("Error sending the POST request:", e)


def populate_api():
    generic_url = r'http://127.0.0.1:5000/add_block_{}'
    data_string = ["popular", "vegetarian", "american", "italian", "chinese", "japanese"]
    encoding = 'utf-8'
    for item in data_string:
        raw_string = r"api-data\{}.txt"
        file_path = raw_string.format(item)
        url_path = generic_url.format(item)
        dict_data = {}
        with open( file_path, 'r', encoding=encoding) as file:
            print(item)
            for line in file:
                key, value = line.strip().split(':')
                dict_data[key.strip()] = value.strip()
                print(dict_data)
            # post_request(url_path, content)


def get_request(url_spoon):

    try:
        response = requests.get(url_spoon)

        # Check the response status code
        if response.status_code == 200:
            # Request successful
            data = response.json()  # Assuming the response is in JSON format
            print("GET request successful!")
            print("Response data:", data)
        else:
            # Request failed
            print(f"GET request failed with status code {response.status_code}:")
            print(response.text)

    except requests.exceptions.RequestException as e:
        # Request exception (e.g., connection error)
        print("Error sending the GET request:", e)


def populate_api2():
    generic_url = r'http://127.0.0.1:5000/add_block_{}'
    cuisine_string = ["american", "italian", "chinese", "japanese"]

    content = get_request('https://api.spoonacular.com/recipes/random?apiKey=edad04879ce74ca68871604be455e04a&number=9')
    post_request('http://127.0.0.1:5000/add_block_popular',content)

    print(content)

    
populate_api2()


