from dotenv import load_dotenv
import requests
import os

load_dotenv()


def get_currency(main_currency, to_currency, amount):
    request_url = f'https://v6.exchangerate-api.com/v6/{os.getenv("API_KEY")}/pair/{main_currency}/{to_currency}/{amount}'

    currency_data = requests.get(request_url).json()

    return currency_data


if __name__ == "__main__":
    print("\n***Currency exchange! ***\n")

    main_currency = input("enter the main currency: ")
    to_currency = input("enter the conversion currency: ")
    amount = input("enter the amount to convert: ")

    final = get_currency(main_currency, to_currency, amount)

    print(final)
