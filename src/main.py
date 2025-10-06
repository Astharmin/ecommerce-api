from flask import Flask
from flask_jwt_extended import JWTManager
from src.auth.routes import auth_bp
from src.products.routes import products_bp
from src.carts.routes import carts_bp
from src.orders.routes import orders_bp
from src.payments.routes import payments_bp
from src.users.routes import users_bp
from src.admin_panel.routes import admin_panel_bp
from src.database.connection import init_db

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    jwt = JWTManager(app)

    init_db(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(carts_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(admin_panel_bp)  # Usa el nombre correcto aquí

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)