#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List
from abc import ABC, abstractmethod
import re


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class TooManyProductsFoundError(Exception):
    def __init__(self):
        super().__init__('Too many products!')


# TODO: dodać do klasy Server logikę rzucania wyjątku
class Server(ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def matched(name: str, n_letters: int) -> bool:
        pattern: str = r'^[a-zA-Z]{' + str(n_letters) + r'}\d{2,3}$'
        match = re.match(pattern, name)
        return True if match else False

    @abstractmethod
    def get_entries(self, n_letters: int = 1):
        pass

    n_max_returned_entries: int = 3


class ListServer(Server):
    def __init__(self, products: List[Product], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = products

    def get_entries(self, n_letters: int = 1):
        pattern: str = r'^[a-zA-Z]{' + str(n_letters) + r'}\d{2,3}$'
        result: List[Product] = []

        for elem in self.products:
            if self.matched(elem.name, n_letters):
                result.append(elem)

        result = sorted(result, key=lambda product: product.price)
        if len(result) > self.n_max_returned_entries:
            raise TooManyProductsFoundError()

        return result


class MapServer(Server):
    def __init__(self, products: List[Product], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = {}
        for elem in products:
            self.products[elem.name] = elem

    def get_entries(self, n_letters: int = 1):
        result: List[Product] = []

        for k, v in self.products.items():
            if self.matched(k, n_letters):
                result.append(v)

        result = sorted(result, key=lambda product: product.price)
        if len(result) > self.n_max_returned_entries:
            raise TooManyProductsFoundError()

        return result


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()
