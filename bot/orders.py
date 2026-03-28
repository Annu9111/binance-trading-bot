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


            return {
                "orderId": order.get("orderId"),
                "status": order.get("status"),
                "executedQty": order.get("executedQty"),
                "avgPrice": order.get("avgPrice", "N/A")
            }

        except Exception as e:
            print("Error placing market order:", str(e))
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )


            return {
                "orderId": order.get("orderId"),
                "status": order.get("status"),
                "executedQty": order.get("executedQty"),
                "avgPrice": order.get("avgPrice", "N/A")
            }

        except Exception as e:
            print("Error placing limit order:", str(e))
            return None