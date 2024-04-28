import requests
from collections import Counter

def check_for_cookies(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Print information about the cookies
        cookies = response.cookies
        
        if cookies:
            print("Cookies found:")
            for cookie in cookies:
                print(cookie)
        else:
            print("No cookies found.")
        
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the URL:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Get user input for the URL to check
    url = input("Enter the URL to check for cookies: ")
    
    # Call the check_for_cookies function with the user-provided URL
    check_for_cookies(url)

def count_normal_cookies(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Extract the domain of the URL
        domain = response.url.split('//')[1].split('/')[0]
        
        # Get the cookies set by the response
        cookies = response.cookies
        
        # Count the number of normal (first-party) cookies
        normal_cookie_count = Counter(cookie.domain == domain for cookie in cookies)
        
        if normal_cookie_count[True] > 0:
            print(f"Number of normal (first-party) cookies found: {normal_cookie_count[True]}")
        else:
            print("No normal (first-party) cookies found.")
        
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the URL:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Get user input for the URL to check
    url = input("Enter the URL to check for normal (first-party) cookies: ")
    
    # Call the count_normal_cookies function with the user-provided URL
    count_normal_cookies(url)
