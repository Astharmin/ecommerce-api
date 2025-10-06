from datetime import datetime, timedelta
import jwt
from flask import current_app

def create_token(user_id):
    expiration = datetime.utcnow() + timedelta(days=1)
    token = jwt.encode({'sub': user_id, 'exp': expiration}, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None