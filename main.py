# Nozimabonu Hamidova N42

# Masala-1

# import psycopg2
#
# from colorama import Fore
#
# conn = psycopg2.connect(dbname='n42',
#                         user='postgres',
#                         password='0905',
#                         host='localhost',
#                         port=5432
#                         )
# cur = conn.cursor()
#
# create_table_query = '''
#     create table if not exists Product(
#         id serial primary key,
#         name varchar(20) not null,
#         price varchar(50) not null,
#         color varchar(10) not null,
#         image_url varchar(200) not null
#
#     );
#
# '''
#
# cur.execute(create_table_query)
# conn.commit()
#
# # Masala-2
#
# def print_response(message: str):
#     print(Fore.Red + message + Fore.RESET)
#
#
# def isert_product():
#     name = str(input('Enter product name: '))
#     price = int(input('Enter product price : '))
#     color = str(input('Enter product color: '))
#     image = str(input('Enter product image: '))
#     insert_into_query = "insert into products (name, price, color, image) values (%s, %s, %s, %s);"
#     insert_into_parms = (name, price, color, image)
#     cur.execute(insert_into_query, insert_into_parms)
#     conn.commit()
#     print_response('Product inserted successfully! 0 1')
#
#
# def select_all_products():
#     select_query = 'select * from products;'
#     cur.execute(select_query)
#     rows = cur.fetchall()
#     for row in rows:
#         print_response(str(row))
#
#
# def select_one_product():
#     _id = int(input('Enter product id: '))
#     select_query = 'select * from products where id = %s'
#     cur.execute(select_query, (_id,))
#     product = cur.fetchall()
#     if product:
#         print_response('No such product found!')
#
#
# def update_product():
#     select_all_products()
#     _id = int(input('Enter product id: '))
#     name = str(input('Enter product name: '))
#     price = int(input('Enter product price : '))
#     color = str(input('Enter product color: '))
#     image = str(input('Enter product image: '))
#     update_query = 'update products set name = %s, price= %s, color = %s, image = %s where id = %s;'
#     update_query_parms = (name, price, color, image, _id)
#     cur.execute(update_query, update_query_parms)
#     conn.commit()
#     print_response('Product updated successfully!')
#
#
#
# def delete_product():
#     select_all_products()
#     _id = int(input('Enter product id: '))
#
#     delete_query = 'delete from products where id = %s;'
#     cur.execute(delete_query, (_id,))
#     conn.commit()
#     print_response('Product deleted successfully!')
#
#
# def menu():
#     try:
#         print('Insert product => 1')
#         print('Select all products => 2')
#         print('Delete product => 3')
#         print('Select one product => 4')
#         print('Update product => 5')
#         choice = int(input('Enter your choice: '))
#
#     except ValueError as error:
#
#         choice = -1
#
#     return choice
#
#
# def run():
#     while True:
#         choice = menu()
#         match choice:
#             case '1':
#                 isert_product()
#             case '2':
#                 select_all_products()
#             case '3':
#                 delete_product()
#             case '4':
#                 select_one_product()
#             case '5':
#                 update_product()
#             case _:
#                 break
#
# if __name__ == '__main__':
#     run()
#

# Misol-3

# class Alphabet():
#     def __init__(self, alphabet):
#         self.alphabet = alphabet
#         self.index = 0
#         super().__init__()
#         for letter in alphabet:
#             self.index += 1
#             self.alphabet.append(letter)
#             self.index += 1
#             self.alphabet.append(self.alphabet[self.index])
#         print(self.alphabet)
#

# Misol-4

# import threading
# import time
#
#
# def print_number():
#     for number in range(6):
#         print(f'NUMBER => {number}')
#         time.sleep(1)
#
#
# def print_leters():
#     for alphabet in 'ABCDE':
#         print(f'Character => {alphabet}')
#         time.sleep(1)
#
#
# thread1 = threading.Thread(target=print_number)
# thread2 = threading.Thread(target=print_leters)
#
# start_time = time.time()
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# end_time = time.time()
# print(f'Total time => {end_time - start_time}')
# print('Process finished')


# Misol-5

# class Product():
#     def __init__(self, name, price, color, image):
#         self.name = name
#         self.price = price
#         self.color = color,
#         self.image = image
# def save():
#     conn = psycopg2.connect("dbname=n42",
#                             user="postgres",
#                             password="0509",
#                             host="localhost",
#                             port="5432")
#     cur = conn.cursor()
#     insert_into_quary = "insert into products(name, price, color, image) values (%s, %s, %s, %s)"
#     cur.execute(insert_into_quary)
#     conn.commit()
#     conn.close()
#
# phone = Product('Xiomi Redmi Note', 50, 'blue', 'https://images.uzum.uz/cmnk0q1s99ouqbfrk2k0/original.jpg')
# print(save())
#
# # Misol-6
#
# class DbConnect:
#     def __init__(self, db_params):
#         self.db_params = db_params
#         self.conn = psycopg2.connect(**self.db_params)
# 
#     def __enter__(self):
#         self.cur = self.conn.cursor()
#         return self.cur
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.conn.commit()
#         self.conn.close()
#
#https://images.uzum.uz/cmnk0q1s99ouqbfrk2k0/original.jpg