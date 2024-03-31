from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    if request.method == 'POST':
        source_currency = request.form['source_currency']
        target_currency = request.form['target_currency']
        amount = float(request.form['amount'])

        conversion_rate = fetch_conversion_rate(source_currency, target_currency)
        converted_amount = round(amount * conversion_rate, 2)

        return render_template('result.html', source_currency=source_currency,
                               target_currency=target_currency, amount=amount,
                               converted_amount=converted_amount)

    return render_template('converter.html', currencies=get_currencies())

def get_currencies():
    return ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY', 'INR']

def fetch_conversion_rate(source_currency, target_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{source_currency}"
    response = requests.get(api_url)
    data = response.json()
    return data['rates'][target_currency]

if __name__ == '__main__':
    app.run(debug=True)
