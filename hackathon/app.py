from flask import Flask, render_template

from geturl import scan_url,clickjack
from hostname import valid_hostname,valid_scheme
from authentication import analyze_authentication_layers,check_authorization_meta_tags,check_authentication_meta_tags,calculate_authentication_score
from sqlinjection import sql_injection_scan
from thirdParty import analyze_website
from cookies import check_for_cookies

app = Flask(__name__)

@app.route('/')
def index():
    name = ['Joe','John','Jim','Paul','Niall','Tom']
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)