#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List
from abc import ABC, abstractmethod


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class TooManyProductsFoundError(Exception):
    def __init__(self):
        super().__init__('Too many products!')


# FIXME: Każada z poniższych klas serwerów powinna posiadać: (1) metodę inicjalizacyjną przyjmującą listę obiektów typu
#  `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#  (3) możliwość odwołania się do metody `get_entries(self, n_letters)`
#  zwracającą listę produktów spełniających kryterium wyszukiwania


class Server(ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    def get_entries(self, n_letters: int):
        pass


class ListServer(Server):
    def __init__(self, products: List[Product], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = products

    def get_entries(self, n_letters: int):
        pass


class MapServer(Server):
    def __init__(self, products: List[Product], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = {}
        for elem in products:
            self.products[elem.name] = elem

    def get_entries(self, n_letters: int):
        pass


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()