import requests
from bs4 import BeautifulSoup

def test_authentication(url):
    try:
        # Send a GET request to a protected endpoint
        response = requests.get(url)
        
        # Check the response status code
        if response.status_code == 401:
            bool==True
            print("Authentication is required. The website has an authentication process.")
        elif response.status_code == 200:
            print("No authentication required. The website does not have an authentication process.")
        else:
            print("Unexpected response status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Get user input for the URL to test
    url = input("Enter the URL to test for authentication: ")
    
    # Call the test_authentication function with the user-provided URL
    test_authentication(url)

def analyze_authentication_layers(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Print the response headers
        print("Response Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        
        # Check for authentication-related headers
        if 'WWW-Authenticate' in response.headers:
            bool==True
            print("The website requires authentication.")
            # You can further analyze the contents of the 'WWW-Authenticate' header
            # to gather information about the authentication mechanism.
        else:
            print("No authentication headers found. The website may not require authentication.")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Get user input for the URL to analyze
    url = input("Enter the URL to analyze for authentication: ")
    
    # Call the analyze_authentication_layers function with the user-provided URL
    analyze_authentication_layers(url)

def check_authentication_meta_tags(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all meta tags in the HTML content
        meta_tags = soup.find_all('meta')
        
        # Check for meta tags containing authentication-related information
        authentication_meta_tags = [tag for tag in meta_tags if 'authentication' in tag.get('name', '').lower()]
        
        # Print the authentication-related meta tags
        if authentication_meta_tags:
            print("Authentication-related meta tags found:")
            for tag in authentication_meta_tags:
                print(tag)
        else:
            print("No authentication-related meta tags found.")
        
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the URL:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Get user input for the URL to check
    url = input("Enter the URL to check for authentication-related meta tags: ")
    
    # Call the check_authentication_meta_tags function with the user-provided URL
    check_authentication_meta_tags(url)

def check_authorization_meta_tags(url):
    authorization_meta_tags = []  # set a default value

    try:
        # Send a GET request to the URL to fetch the HTML content
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all meta tags with name="authorization"
        authorization_meta_tags = soup.find_all('meta', attrs={'name': 'authorization'})

        # Check if any authorization meta tags were found
        if authorization_meta_tags:
            print("Authorization meta tags found:")
            for tag in authorization_meta_tags:
                print(tag)
        else:
            print("No authorization meta tags found")

    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the webpage:", e)
    except Exception as e:
        print("An error occurred:", e)
    
    return authorization_meta_tags

def calculate_authentication_score(url):
    auth_score = 17

    # Test authentication | Analyze authentication layers
    auth_required = test_authentication(url)
    auth_layers=analyze_authentication_layers(url)
    if auth_required or auth_layers != True:
        auth_score -= 12

    # Check authorization meta tags
    authorization_meta_tags = check_authorization_meta_tags(url)
    num_auth_tags = len(authorization_meta_tags)
    if num_auth_tags == 1:
        auth_score -= 2
    elif num_auth_tags >= 2:
        auth_score -= 5

    return auth_score

if __name__ == "__main__":
    # Get user input for the URL to analyze
    url = input("Enter the URL to analyze for authentication and authorization: ")

    # Calculate authentication score
    score = calculate_authentication_score(url)
    print("Authentication and Authorization Score:", score)
