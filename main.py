from flask import Flask, request
import requests
from dotenv import find_dotenv, load_dotenv
import os

if find_dotenv():
    load_dotenv()
    API = os.getenv('API')

app = Flask(__name__)
#  /api/rates?from=USD&to=RUB&value=1

@app.route('/api/rates', methods=['GET'])
def convert():
    if request.method == 'GET':
        from_c = request.args.get('from', type=str)
        to_c = request.args.get('to', type=str)
        amount = request.args.get('value', type=int)
        
        if amount == None:
            amount = 1
        
        if from_c is None or from_c == '':
            return 'You have to specify FROM currency'
        elif to_c is None or to_c == '':
            return 'You have to specify TO currency'    
        
        url = f"https://api.apilayer.com/fixer/convert?to={to_c}&from={from_c}&amount={amount}"

        payload = {}
        headers= {
        "apikey": API
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        result = response.json()
        try:
            return {'result':round(result['result'],2)}
        except:
            return result['error']['info']
        
            
if __name__ == '__main__':
    app.run(debug=True)
