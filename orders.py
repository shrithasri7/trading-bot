import logging
from bot.client import get_client

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        # ✅ ADD THIS LINE
        client.futures_change_leverage(symbol=symbol, leverage=10)

        logging.info(f"Placing {order_type} order: {symbol} {side}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Order response: {order}")
        return order

    except Exception as e:
        print("❌ ERROR:", str(e))   # ✅ ADD THIS
        logging.error(f"Error placing order: {str(e)}")
        return None