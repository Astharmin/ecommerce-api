from flask import Blueprint, request, jsonify
from .models import Order
from ..database.connection import db

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    new_order = Order(
        user_id=data['user_id'],
        product_ids=data['product_ids']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created', 'order_id': new_order.order_id}), 201

@orders_bp.route('/orders/<int:user_id>', methods=['GET'])
def get_orders(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([order.to_dict() for order in orders]), 200