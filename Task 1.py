class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0
        self.wrapped_as_gift = False

    def calculate_total_amount(self):
        return self.quantity * self.price


class ShoppingCart:
    def __init__(self):
        self.products = {
            "Product A": Product("Product A", 20),
            "Product B": Product("Product B", 40),
            "Product C": Product("Product C", 50),
        }

    def get_user_input(self):
        for product_name, product in self.products.items():
            product.quantity = int(input(f"Enter quantity for {product_name}: "))
            product.wrapped_as_gift = input(f"Is {product_name} wrapped as a gift? (yes/no): ").lower() == "yes"

    def calculate_subtotal(self):
        return sum(product.calculate_total_amount() for product in self.products.values())

    def apply_discount(self, subtotal):
        discounts = {
            "flat_10_discount": 10 if subtotal > 200 else 0,
            "bulk_5_discount": 0,
            "bulk_10_discount": 0,
            "tiered_50_discount": 0,
        }

        total_quantity = sum(product.quantity for product in self.products.values())

        if total_quantity > 20:
            discounts["bulk_10_discount"] = subtotal * 0.1

            
        if total_quantity > 30:
            for product in self.products.values():
                if product.quantity > 15:
                    discounts["tiered_50_discount"] = (
                        product.price * (product.quantity - 15) * 0.5
                    )

        
        eligible_products = [product for product in self.products.values() if product.quantity > 10]
        if eligible_products:
            discounts["bulk_5_discount"] = max(
                product.price * product.quantity * 0.05
                for product in eligible_products
            )

        return max(discounts, key=discounts.get), max(discounts.values())

    def calculate_shipping_fee(self):
        total_quantity = sum(product.quantity for product in self.products.values())
        return (total_quantity // 10) * 5

    def calculate_gift_wrap_fee(self):
        return sum(product.quantity for product in self.products.values() if product.wrapped_as_gift)

    def display_receipt(self):
        print("\nProduct Details:")
        for product in self.products.values():
            if product.quantity > 0:
                print(
                    f"{product.name}: Quantity - {product.quantity}, Total - ${product.calculate_total_amount()}"
                )

        subtotal = self.calculate_subtotal()
        discount_name, discount_amount = self.apply_discount(subtotal)
        shipping_fee = self.calculate_shipping_fee()
        gift_wrap_fee = self.calculate_gift_wrap_fee()
        total = subtotal - discount_amount + shipping_fee + gift_wrap_fee

        print("\nSubtotal: $", subtotal)
        print(f"Discount Applied: {discount_name}, Amount: ${discount_amount}")
        print(f"Shipping Fee: ${shipping_fee}")
        print(f"Gift Wrap Fee: ${gift_wrap_fee}")
        print("\nTotal: $", total)



shopping_cart = ShoppingCart()
shopping_cart.get_user_input()
shopping_cart.display_receipt()

