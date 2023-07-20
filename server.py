from flask import *
from currency import get_currency
from waitress import serve
import urllib.request


app = Flask(__name__)


def getResponseCode(url):
    conn = urllib.request.urlopen(url)
    return conn.getcode()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/currency')
def currency():
    currency1 = request.args.get('currency1')
    currency2 = request.args.get('currency2')
    amount = request.args.get('amount')

    final_data = get_currency(currency1, currency2, amount)

    base_code = final_data['base_code']
    target_code = final_data['target_code']
    conversion_result = final_data['conversion_result']

    return render_template(
        'currency.html',
        amount=amount,
        currency1=base_code,
        currency2=target_code,
        conversion_result=conversion_result
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
