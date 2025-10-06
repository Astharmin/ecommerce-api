from flask import Blueprint, request, jsonify
from src.products.models import Product
from src.database.connection import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/products', methods=['POST'])
def admin_add_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        stock=data['stock']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully', 'product_id': new_product.id}), 201

@admin_bp.route('/admin/products/<int:product_id>', methods=['PUT'])
def admin_update_product(product_id):
    data = request.get_json()
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)

    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})