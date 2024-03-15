import requests

def convert_currency(amount, source_currency, target_currency):
    api_key = '2166410a282cf1b36725893e'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{source_currency}/{target_currency}'

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print("Error:", data.get('error', 'Unknown error'))
            return None
        
        if 'conversion_rate' not in data:
            print("Error: Conversion rate not found in response")
            return None

        conversion_rate = data['conversion_rate']
        converted_amount = amount * conversion_rate
        
        return converted_amount
        
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def main():
    try:
        amount_str = input("Enter the amount to convert: ")
        amount = float(amount_str)
        source_currency = input("Enter the source currency code: ").upper()
        target_currency = input("Enter the target currency code: ").upper()

        converted_amount = convert_currency(amount, source_currency, target_currency)

        if converted_amount is not None:
            print(f"{amount} {source_currency} is equivalent to {converted_amount:.2f} {target_currency}")

    except ValueError:
        print("Error: Please enter a valid number for the amount.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
