import requests
from collections import Counter

def check_for_cookies(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Print information about the cookies
        cookies = response.cookies
        
        
        # Initialize score
        total_score = 17
        
        # Count the number of normal (first-party) cookies
        normal_cookie_count = Counter(cookie.domain == response.url.split('//')[1].split('/')[0] for cookie in cookies)
        
        if normal_cookie_count[True] > 0:
            print(f"Number of normal (first-party) cookies found: {normal_cookie_count[True]}")
            total_score -= 1  # Deduct 1 if any first-party cookie found
        else:
            print("No normal (first-party) cookies found.")
            total_score = 17

        return total_score
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the URL:", e)
        return 0
    except Exception as e:
        print("An error occurred:", e)
        return 0

if __name__ == "__main__":
    # Get user input for the URL to check
    url = input("Enter the URL to check for first-party cookies: ")
    
    # Call the check_for_cookies function with the user-provided URL
    final_deducted_score = check_for_cookies(url)
    
    # Print the final deducted score
    print("Final Score:", final_deducted_score)
