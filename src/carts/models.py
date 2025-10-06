class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.product_ids = []

    def add_product(self, product_id):
        if product_id not in self.product_ids:
            self.product_ids.append(product_id)

    def remove_product(self, product_id):
        if product_id in self.product_ids:
            self.product_ids.remove(product_id)

    def clear_cart(self):
        self.product_ids.clear()