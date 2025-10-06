from flask import Blueprint, jsonify

admin_panel_bp = Blueprint('admin_panel', __name__)

@admin_panel_bp.route('/dashboard', methods=['GET'])
def admin_dashboard():
    return jsonify({"message": "Welcome to the admin dashboard!"})