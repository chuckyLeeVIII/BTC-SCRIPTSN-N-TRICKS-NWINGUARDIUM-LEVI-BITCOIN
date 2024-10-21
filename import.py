import requests

#portable btc address extractor = value import

def extract_btc(portable_address, amount):
    try:
        # Retrieve the balance of the portable address
        balance = get_balance(portable_address)
        
        if balance is None:
            raise ValueError("Failed to retrieve balance.")
        
        # Check if the balance is sufficient
        if balance < amount:
            raise ValueError("Insufficient balance.")
        
        # Perform the extraction transaction
        # (This part depends on the specific wallet implementation and API)
        # You would need to integrate with your wallet and perform the transaction
        # using the appropriate API calls.
        
        # Example API call for a hypothetical wallet
        # Replace the URL and parameters with your actual wallet API endpoint
        url = "https://wallet.example.com/api/extract"
        params = {
            "portable_address": portable_address,
            "amount": amount
        }
        response = requests.post(url, json=params)
        
        if response.status_code != 200:
            raise ValueError("Extraction transaction failed.")
        
        print("Extraction successful. Amount extracted:", amount)
    except Exception as e:
        print("An error occurred during the extraction:", str(e))

def withdraw_btc(portable_address, amount):
    try:
        # Perform the withdrawal transaction
        # (This part depends on the specific wallet implementation and API)
        # You would need to integrate with your wallet and perform the transaction
        # using the appropriate API calls.
        
        # Example API call for a hypothetical wallet
        # Replace the URL and parameters with your actual wallet API endpoint
        url = "https://wallet.example.com/api/withdraw"
        params = {
            "portable_address": portable_address,
            "amount": amount
        }
        response = requests.post(url, json=params)
        
        if response.status_code != 200:
            raise ValueError("Withdrawal transaction failed.")
        
        print("Withdrawal successful. Amount withdrawn:", amount)
    except Exception as e:
        print("An error occurred during the withdrawal:", str(e))

# Example usage
portable_address = "1234abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
extract_amount = 1.5  # Amount to extract in BTC
withdraw_amount = 0.7  # Amount to withdraw in BTC

extract_btc(portable_address, extract_amount)
withdraw_btc(portable_address, withdraw_amount)
