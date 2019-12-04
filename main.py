from servers import *

product_1 = Product('AB12', 421)
product_2 = Product('ab123', 333)
product_3 = Product('Aa12', 111)
product_4 = Product('ab11', 999)
product_5 = Product('Abd134', 123)
product_6 = Product('Addr12', 211)
product_7 = Product('Aaa123', 111)
product_8 = Product('has99', 10)

product_list = [product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8]

# server_list = ListServer(product_list)
# server_dict = MapServer(product_list)
#
# print('ListServer: ')
# for elem in server_list.products:
#     print(f'Name: {elem.name}, Price: {elem.price}')
#
# print('\nMapServer: ')
# for k, v in server_dict.products.items():
#     print(f'Name: {k}, Price: {v.price}')
#
#
# print('\n__________ListServer Match Test____________')
# try:
#     result_list = server_list.get_entries(3)
#     for elem in result_list:
#         print(f'Name: {elem.name}, Price: {elem.price}')
# except TooManyProductsFoundError:
#     print('Too many products!')
#
#
# print('\n__________MapServer Match Test____________')
# try:
#     result_dict = server_dict.get_entries(3)
#     for elem in result_dict:
#         print(f'Name: {elem.name}, Price: {elem.price}')
# except TooManyProductsFoundError:
#     print('Too many products!')

server_list = ListServer(product_list)
client = Client(server_list)







