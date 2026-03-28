from bot.client import BinanceClient


class OrderService:
    def __init__(self):
        self.client = BinanceClient().get_client()
        
        def place_market_order(self, symbol, side, quantity):
            try:
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )
                return order
            except Exception as e:
                print("Error placing market order:", str(e))
                return None    