from servers import *

product_1 = Product('AB12', 10)
product_2 = Product('ab123', 15)
product_3 = Product('A12', 20)
product_4 = Product('ab1', 20)
product_5 = Product('Ab1234', 25)
product_6 = Product('Abc12', 30)

product_list = [product_1, product_2, product_3, product_4, product_5, product_6]

server_list = ListServer(product_list)
server_dict = MapServer(product_list)

print('ListServer: ')
for elem in server_list.products:
    print(f'Name: {elem.name}, Price: {elem.price}')

print('\nMapServer: ')
for k, v in server_dict.products.items():
    print(f'Name: {k}, Price: {v.price}')


print('\n_________ListServer Match Test_____________')
result_list = server_list.get_entries(2)
for elem in result_list:
    print(f'Name: {elem.name}, Price: {elem.price}')


print('\n__________MapServer Match Test____________')
result_dict = server_list.get_entries(2)
for elem in result_dict:
    print(f'Name: {elem.name}, Price: {elem.price}')


