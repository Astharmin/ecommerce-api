from flask import Blueprint, request, jsonify
from .stripe_service import create_payment, verify_payment

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/create_payment', methods=['POST'])
def process_payment():
    data = request.json
    try:
        payment_intent = create_payment(data['amount'], data['currency'], data['payment_method'])
        return jsonify({'success': True, 'payment_intent': payment_intent}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@payments_bp.route('/verify_payment/<payment_id>', methods=['GET'])
def check_payment(payment_id):
    try:
        payment_status = verify_payment(payment_id)
        return jsonify({'success': True, 'status': payment_status}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400