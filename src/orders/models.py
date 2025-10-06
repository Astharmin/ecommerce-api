class Order:
    def __init__(self, order_id, user_id, product_ids):
        self.order_id = order_id
        self.user_id = user_id
        self.product_ids = product_ids

    def __repr__(self):
        return f"<Order(order_id={self.order_id}, user_id={self.user_id}, product_ids={self.product_ids})>"