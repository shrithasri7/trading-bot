import argparse
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price", required=False)

args = parser.parse_args()

try:
    validate_order(args.side, args.type, args.quantity, args.price)

    print("\n📌 Order Summary:")
    print(vars(args))

    response = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    if response:
        print("\n✅ Order Success")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))
    else:
        print("\n❌ Order Failed")

except Exception as e:
    print("Error:", e)