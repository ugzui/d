from flask import Flask, request, jsonify
from crawler import crawl_shop_products

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Douyin API is running!"

@app.route('/get_shop_products', methods=['GET'])
def get_products():
    shop_id = request.args.get('shop_id')
    if not shop_id:
        return jsonify({"error": "shop_id is required"}), 400
    try:
        result = crawl_shop_products(shop_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
