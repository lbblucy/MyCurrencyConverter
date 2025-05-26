class CurrencyConverter: # Currency converter class

    #class attribute # base value dollar
    exchange_rates = {
        "USD": 1.0,        # Base currency
        "BDT": 121.60,     # Bangladeshi Taka
        "EUR": 0.88,       # Euro
        "GBP": 0.74,       # British Pound Sterling
        "AUD": 1.55,       # Australian Dollar
        "JPY": 142.63,     # Japanese Yen
        "CAD": 1.37,       # Canadian Dollar
        "CHF": 0.91,       # Swiss Franc
        "CNY": 7.12,       # Chinese Yuan
        "INR": 83.25,      # Indian Rupee
        "BRL": 5.27,       # Brazilian Real
        "ZAR": 18.45,      # South African Rand
        "RUB": 96.50,      # Russian Ruble
        "KRW": 1345.00,    # South Korean Won
        "SGD": 1.36,       # Singapore Dollar
        "MXN": 17.85,      # Mexican Peso
        "NOK": 10.85,      # Norwegian Krone
        "TRY": 27.50,      # Turkish Lira
        "SAR": 3.75,       # Saudi Riyal
        "AED": 3.67,       # UAE Dirham
        "HKD": 7.85,       # Hong Kong Dollar
        "MYR": 4.70,       # Malaysian Ringgit
        "THB": 35.20,      # Thai Baht
        "EGP": 30.90,      # Egyptian Pound
        "PKR": 278.00,     # Pakistani Rupee
        "IDR": 15600.00,   # Indonesian Rupiah
        "PHP": 56.00,      # Philippine Peso
        "PLN": 4.15,       # Polish Zloty
        "DKK": 6.60,       # Danish Krone
        "HUF": 350.00,     # Hungarian Forint
        "CZK": 22.50,      # Czech Koruna
        "ILS": 3.75,       # Israeli New Shekel
        "CLP": 900.00,     # Chilean Peso
        "COP": 4000.00,    # Colombian Peso
        "ARS": 350.00,     # Argentine Peso
        "VND": 24000.00,   # Vietnamese Dong
        "NGN": 780.00,     # Nigerian Naira
        "KZT": 470.00,     # Kazakhstani Tenge
        "UAH": 36.50,      # Ukrainian Hryvnia
        "QAR": 3.64,       # Qatari Riyal
        "KWD": 0.31,       # Kuwaiti Dinar
        "BHD": 0.38,       # Bahraini Dinar
        "OMR": 0.38,       # Omani Rial
        "MAD": 10.00,      # Moroccan Dirham
        "TND": 3.10,       # Tunisian Dinar
        "JOD": 0.71,       # Jordanian Dinar
        "LBP": 15000.00,   # Lebanese Pound
        "SDG": 600.00,     # Sudanese Pound
        "DZD": 135.00,     # Algerian Dinar
        "IQD": 1460.00,    # Iraqi Dinar
        "IRR": 42000.00,   # Iranian Rial
        "AFN": 86.00,      # Afghan Afghani
        "NPR": 132.00,     # Nepalese Rupee
        "LKR": 320.00,     # Sri Lankan Rupee
        "MMK": 2100.00,    # Myanmar Kyat
        "MNT": 3450.00,    # Mongolian Tugrik
        "UZS": 11600.00,   # Uzbekistani Som
        "AZN": 1.70,       # Azerbaijani Manat
        "GEL": 2.70,       # Georgian Lari
        "AMD": 385.00,     # Armenian Dram
        "BYN": 2.50,       # Belarusian Ruble
    }

    def __init__(self, amount, from_currency, to_currency): # Instance attribute by init function
        self.amount = amount
        self.from_currency = from_currency.upper() # upper() is used for "lower case converted into upper case"
        self.to_currency = to_currency.upper()
    
    # Instance method which handles conversion
    def convert(self):        
        base_amount = self.amount / CurrencyConverter.exchange_rates[self.from_currency]
        converted_amount = base_amount * CurrencyConverter.exchange_rates[self.to_currency]
        return round(converted_amount, 2)
    
    @classmethod # Which will update exchange rate
    def update_rate(cls, currency, new_rate):
        cls.exchange_rates[currency] = new_rate

    @staticmethod # Check whether the currency code valid or not
    def is_valid_currency(code):
        return code.upper() in CurrencyConverter.exchange_rates
    
class Logger: # Association demonstration, It's a completely different class.
    # Instance method
    def log(self, user, converter):
        result = converter.convert()
        print(f"Hello {user}, {converter.amount} {converter.from_currency} = {result} {converter.to_currency}")

if __name__ == "__main__" :

    CurrencyConverter.update_rate("BDT", 127.06) # For update currency
    CurrencyConverter.update_rate("JPY", 145.84) # For update currency
    
    amount = float(input("Enter amount to convert: "))
    from_curr = input("Enter source currency code (e.g., USD): ")
    to_curr = input("Enter your desired currency code in which you want to convert (e.g., GBP): ")
    user = input("Enter your name: ")

    converter = CurrencyConverter(amount, from_curr, to_curr) # Object created

    if not CurrencyConverter.is_valid_currency(from_curr) or not CurrencyConverter.is_valid_currency(to_curr):
        print("Invalid currency, we don't have this currency.")
    else:
        Logger_object = Logger()
        Logger_object.log(user, converter)