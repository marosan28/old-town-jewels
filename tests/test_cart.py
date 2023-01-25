from django.test import TestCase
from decimal import Decimal
from django.conf import settings
from shop.models import Product
from cart.cart import Cart

class CartTestCase(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(name='product1', price=10)
        self.product2 = Product.objects.create(name='product2', price=20)
        self.cart = Cart(self.client.session)
    
    def test_add_to_cart(self):
        # add product1 to cart
        self.cart.add(self.product1, 2)
        self.assertEqual(self.cart.cart[str(self.product1.id)]['quantity'], 2)
        self.assertEqual(self.cart.cart[str(self.product1.id)]['price'], '10')

        # add product2 to cart
        self.cart.add(self.product2)
        self.assertEqual(self.cart.cart[str(self.product2.id)]['quantity'], 1)
        self.assertEqual(self.cart.cart[str(self.product2.id)]['price'], '20')

    def test_remove_from_cart(self):
        # add product1 to cart
        self.cart.add(self.product1, 2)

        # remove product1 from cart
        self.cart.remove(self.product1)
        self.assertNotIn(str(self.product1.id), self.cart.cart)

    def test_cart_iter(self):
        # add product1 and product2 to cart
        self.cart.add(self.product1, 2)
        self.cart.add(self.product2)

        items = list(self.cart)
        self.assertEqual(
