from flask import Blueprint, request, jsonify
from .models import Cart
from ..database.connection import db

carts_bp = Blueprint('carts', __name__)

@carts_bp.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    
    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        cart = Cart(user_id=user_id, product_ids=[])
    
    if product_id not in cart.product_ids:
        cart.product_ids.append(product_id)
        db.session.add(cart)
        db.session.commit()
        return jsonify({'message': 'Product added to cart'}), 201
    return jsonify({'message': 'Product already in cart'}), 400

@carts_bp.route('/cart', methods=['DELETE'])
def remove_from_cart():
    data = request.json
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    
    cart = Cart.query.filter_by(user_id=user_id).first()
    if cart and product_id in cart.product_ids:
        cart.product_ids.remove(product_id)
        db.session.commit()
        return jsonify({'message': 'Product removed from cart'}), 200
    return jsonify({'message': 'Product not found in cart'}), 404

@carts_bp.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    cart = Cart.query.filter_by(user_id=user_id).first()
    if cart:
        return jsonify({'user_id': cart.user_id, 'product_ids': cart.product_ids}), 200
    return jsonify({'message': 'Cart not found'}), 404