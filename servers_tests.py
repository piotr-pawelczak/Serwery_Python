import unittest
from collections import Counter

from servers import ListServer, Product, Client, MapServer

server_types = (ListServer, MapServer)


class ServerTest(unittest.TestCase):
    pass
# TODO: Czy wyniki zwrócone przez serwer przechowujący dane w liście są poprawnie posortowane?

# TODO: Czy przekroczenie maksymalnej liczby znalezionych produktów powoduje rzucenie wyjątku?


class ClientTest(unittest.TestCase):
    pass
# TODO: Czy funkcja obliczająca łączną cenę produktów zwraca poprawny wynik w przypadku rzucenia wyjątku oraz braku
#  produktów pasujących do kryterium wyszukiwania?


if __name__ == '__main__':
    unittest.main()

