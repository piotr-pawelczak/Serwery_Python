#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, TypeVar
from abc import ABC, abstractmethod
import re


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __hash__(self):
        return hash((self.name, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


class TooManyProductsFoundError(Exception):
    def __init__(self):
        super().__init__('Too many products!')


class Server(ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    n_max_returned_entries: int = 3

    @staticmethod
    def matched(name: str, n_letters: int) -> bool:
        pattern: str = r'^[a-zA-Z]{' + str(n_letters) + r'}\d{2,3}$'
        match = re.match(pattern, name)
        return True if match else False

    @abstractmethod
    def get_entries(self, n_letters: int = 1):
        raise NotImplementedError()

    def product_number_validator(self, result):
        if len(result) > self.n_max_returned_entries:
            raise TooManyProductsFoundError()


class ListServer(Server):
    def __init__(self, products: List[Product], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = products

    def get_entries(self, n_letters: int = 1):
        result: List[Product] = []

        for elem in self.products:
            if self.matched(elem.name, n_letters):
                result.append(elem)

        result = sorted(result, key=lambda product: product.price)
        self.product_number_validator(result)
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
        self.product_number_validator(result)
        return result


ServerType = TypeVar('ServerType', bound=Server)


class Client:
    def __init__(self, server: ServerType):
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            total_price: float = 0
            product_list: List[Product] = self.server.get_entries(n_letters)

            for elem in product_list:
                total_price += elem.price
        except TooManyProductsFoundError:
            return None

        if len(product_list) == 0:
            return None

        return total_price
