import requests
from collections import defaultdict

def find_external_requests(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Get the base URL of the provided URL
        base_url = response.url.split('//')[1].split('/')[0]
        
        # Get the list of requests to external domains
        external_requests = []
        for request in response.history + [response]:
            request_url = request.url.split('//')[1].split('/')[0]
            if request_url != base_url:
                external_requests.append(request_url)
        
        if external_requests:
            print("Requests to external domains found:")
            for request_url in external_requests:
                print(request_url)
        else:
            print("No requests to external domains found.")
        
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the URL:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Get user input for the URL to check
    url = input("Enter the URL to check for requests to external domains: ")
    
    # Call the find_external_requests function with the user-provided URL
    find_external_requests(url)

def count_external_requests(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Get the base URL of the provided URL
        base_url = response.url.split('//')[1].split('/')[0]
        
        # Initialize a dictionary to store the counts of requests to external domains
        external_requests_count = defaultdict(int)
        
        # Count the number of requests to external domains
        for request in response.history + [response]:
            request_url = request.url.split('//')[1].split('/')[0]
            if request_url != base_url:
                external_requests_count[request_url] += 1
        
        if external_requests_count:
            print("Requests to external domains:")
            for domain, count in external_requests_count.items():
                print(f"{domain}: {count} times")
        else:
            print("No requests to external domains found.")
        
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the URL:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Get user input for the URL to check
    url = input("Enter the URL to check for requests to external domains: ")
    
    # Call the count_external_requests function with the user-provided URL
    count_external_requests(url)

def find_third_party_cookies(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Extract the domain of the URL
        domain = response.url.split('//')[1].split('/')[0]
        
        # Get the cookies set by the response
        cookies = response.cookies
        
        # Find third-party cookies
        third_party_cookies = [cookie for cookie in cookies if cookie.domain != domain]
        
        if third_party_cookies:
            print("Third-party cookies found:")
            for cookie in third_party_cookies:
                print(cookie)
        else:
            print("No third-party cookies found.")
        
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the URL:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Get user input for the URL to check
    url = input("Enter the URL to check for third-party cookies: ")
    
    # Call the find_third_party_cookies function with the user-provided URL
    find_third_party_cookies(url)
