from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Coffee Menu
menu = [
    Coffee("South Indian Filter Coffee", 99),
    Coffee("Bella Kaapi", 89),
    Coffee("Sukku Kaapi", 79),
    Coffee("Tandoori Coffee", 69),
    Coffee("Araku Coffee", 59),
    Coffee("Blue Tokai Coffee", 49),
    Coffee("Bhava Coffee", 59),
    Coffee("Bili Hu Coffee", 59),
    Coffee("Bru Coffee", 19),
    Coffee("Continental Coffee", 29),
    Coffee("Country Bean Coffee", 59),
    Coffee("Davidoff Coffee", 49),
    Coffee("Kings Coffee", 59),
    Coffee("Nescafe Coffee", 59),
    Coffee("Rage Coffee", 79),
]

order = []

@app.route('/')
def index():
    total = sum(item.price for item in order)
    # Pass `message` explicitly, avoids KeyError if message not set
    return render_template('index.html', menu=menu, order=order, total=total, message=request.args.get('message'))

@app.route('/add/<int:item_id>')
def add_item(item_id):
    coffee = menu[item_id]
    order.append(coffee)
    return redirect(url_for('index'))

@app.route('/clear')
def clear_order():
    order.clear()
    return redirect(url_for('index'))

@app.route('/checkout')
def checkout():
    if not order:
        return redirect(url_for('index'))
    total = sum(item.price for item in order)
    message = f"Order confirmed! Total: ₹{total}. Thanks for your order! ☕"
    order.clear()
    # Pass the message as a query parameter for simple display on index
    return redirect(url_for('index', message=message))

@app.route("/healthz")
def health_check():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

