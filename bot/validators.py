def validate_symbol(symbol):
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string")
    return symbol.upper()


def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side


def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type


def validate_quantity(quantity):
    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError
        return quantity
    except:
        raise ValueError("Quantity must be a positive number")


def validate_price(price):
    try:
        price = float(price)
        if price <= 0:
            raise ValueError
        return price
    except:
        raise ValueError("Price must be a positive number")