import requests
from bs4 import BeautifulSoup

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

def get_forms(url):
    soup = BeautifulSoup(s.get(url).content, "html.parser")
    return soup.find_all("form")

def form_details(form):
    detailsOfForm = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get")
    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({
            "type": input_type, 
            "name" : input_name,
            "value" : input_value,
        })
        
    detailsOfForm['action'] = action
    detailsOfForm['method'] = method
    detailsOfForm['inputs'] = inputs
    return detailsOfForm

def vulnerable(response):
<<<<<<< HEAD
    errors = {"quoted string not properly terminated", 
              "unclosed quotation mark after charachter string",
              "you have an error in you SQL syntax" 
             }
=======
    errors = {
        "quoted string not properly terminated", 
        "unclosed quotation mark after the charachter string",
        "you have an error in you SQL syntax" 
    }
>>>>>>> 106cbc1ec31ea2bdca35a7093a459cbb9fe56d54
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False

<<<<<<< HEAD
def sql_injection_scan(url):
    forms = get_forms(url)
    print(f"Detected {len(forms)} forms on {url}.")
=======
def sql_injection_scan(urlToBeChecked):
    forms = get_forms(urlToBeChecked)
    print(f"[+] Detected {len(forms)} forms on {urlToBeChecked}.")
    
    score = 12  # set score=0
>>>>>>> 106cbc1ec31ea2bdca35a7093a459cbb9fe56d54
    
    for form in forms:
        details = form_details(form)
        
        for i in "\"'":
            data = {}
            for input_tag in details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    data[input_tag['name']] = input_tag["value"] + i
                elif input_tag["type"] != "submit":
                    data[input_tag['name']] = f"test{i}"
    
<<<<<<< HEAD
            form_details(form)

=======
>>>>>>> 106cbc1ec31ea2bdca35a7093a459cbb9fe56d54
            if details["method"] == "post":
                res = s.post(urlToBeChecked, data=data)
            elif details["method"] == "get":
                res = s.get(urlToBeChecked, params=data)
            if vulnerable(res):
                print("SQL injection attack vulnerability in link: ", urlToBeChecked)
                score -= 2 
            else:
                print("No SQL injection attack vulnerability detected")
                break
    
    print("Score:", score)

if __name__ == "__main__":
<<<<<<< HEAD
    url = input("Enter the URL: ")
    sql_injection_scan(url)
=======
    urlToBeChecked = input("Enter the URL to test for SQL Injection: ")
    sql_injection_scan(urlToBeChecked)
>>>>>>> 106cbc1ec31ea2bdca35a7093a459cbb9fe56d54
