import argparse
from bot.orders import OrderService
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger


def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Price (required for LIMIT)")

    args = parser.parse_args()

    try:
        # Validate inputs
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        price = None
        if order_type == "LIMIT":
            if not args.price:
                raise ValueError("Price is required for LIMIT orders")
            price = validate_price(args.price)

        # Create order service
        order_service = OrderService()

        # Place order
        if order_type == "MARKET":
            result = order_service.place_market_order(symbol, side, quantity)
        else:
            result = order_service.place_limit_order(symbol, side, quantity, price)

        # Output result
        if result:
            print("Order Successful")
            print(result)
            logger.info(f"Order success: {result}")
        else:
            print("Order Failed")
            logger.error("Order failed")

    except Exception as e:
        print("Error:", str(e))
        logger.error(f"Error: {str(e)}")


if __name__ == "__main__":
    main()