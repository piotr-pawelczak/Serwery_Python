import unittest
from collections import Counter

from servers import ListServer, Product, Client, MapServer, TooManyProductsFoundError

server_types = (ListServer, MapServer)


class ServerTest(unittest.TestCase):

    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))

    def test_get_entries_returns_sorted_list(self):
        products = [Product('PP234', 3), Product('PP235', 1), Product('PP236', 2)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            sorted_products = [products[1], products[2], products[0]]
            self.assertEqual(sorted_products, entries)

    def test_get_entries_raises_exception(self):
        products = [Product('PP234', 2), Product('PP235', 3), Product('PP236', 4), Product('PP237', 5)]
        for server_type in server_types:
            server = server_type(products)

            with self.assertRaises(TooManyProductsFoundError):
                server.get_entries(2)


class ClientTest(unittest.TestCase):

    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5, client.get_total_price(2))

    def test_total_price_for_problematic_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3), Product('PP236', 4), Product('PP237', 5)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(2))   # Too many products
            self.assertEqual(None, client.get_total_price(3))   # No products found


if __name__ == '__main__':
    unittest.main()

