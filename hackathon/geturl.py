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
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    user_url = input("Enter the URL to scan: ")
    scan_url(user_url)

def clickjack(url):
    try:
        response = requests.get(url)
        if "Strict-Transport-Security" in response.headers:
            return True
        elif "X-Content-Type-Options" in response.headers:
            return True
        elif "Content-Security-Policy" in response.headers:
            return True
        elif "X-Frame-Options" in response.headers:
            return True
        elif "X-XSS-Protection" in response.headers:
            return True
        elif "Referrer-Policy" in response.headers:
            return True
        elif "Feature-policy" in response.headers:
            return True
        
    except:
        return False
    
print(clickjack(user_url))