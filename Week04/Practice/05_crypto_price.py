import requests

crypto = input("Enter cryptocurrency name (example: bitcoin): ").lower()

url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd,inr"

try:
    response = requests.get(url)
    data = response.json()

    if crypto in data:
        usd_price = data[crypto]["usd"]
        inr_price = data[crypto]["inr"]

        print("\n--- Cryptocurrency Price ---")
        print("Cryptocurrency:", crypto.capitalize())
        print("Price in USD: $", usd_price)
        print("Price in INR: ₹", inr_price)

    else:
        print("Cryptocurrency not found")

except Exception as error:
    print("Error:", error)