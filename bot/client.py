import os
from binance.client import Client
from dotenv import load_dotenv


class BinanceClient:
    def __init__(self):
        load_dotenv()

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API_KEY or API_SECRET is missing in .env file")

        try:
            self.client = Client(api_key, api_secret)
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        except Exception as e:
            print("Error connecting to Binance:", str(e))
            raise

    def get_client(self):
        return self.client