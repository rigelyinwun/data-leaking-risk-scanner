import requests

def scan_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("URL is accessible and returns a 200 OK status code.")
            # Optionally, you can analyze the response content here
            # For example, check for specific keywords or patterns in the HTML content
        else:
            print(f"URL is accessible but returns a {response.status_code} status code.")
        print(response.headers)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    user_url = input("Enter the URL to scan: ")
    scan_url(user_url)