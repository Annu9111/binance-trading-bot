from bot.client import BinanceClient


class OrderService:
    def __init__(self):
        self.client = BinanceClient().get_client()