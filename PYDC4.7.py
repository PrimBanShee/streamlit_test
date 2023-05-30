class Product:
  def __init__(self, name, price, description, quantity):
    self.name = name
    self.price = price
    self.description = description
    self.quantity = quantity

class ProductManager:
  def __init__(self):
    self.products = []

  def add_product(self, product):
    self.products.append(product)

  def remove_product(self, product):
    self.products.remove(product)

  def get_product(self, name):
    for product in self.products:
      if product.name == name:
        return product
    return None

  def get_all_products(self):
    return self.products

# Khởi tạo một đối tượng ProductManager
manager = ProductManager()

# Thêm một số sản phẩm mẫu để kiểm tra
manager.add_product(Product("iPhone 13", 999, "A new iPhone", 10))
manager.add_product(Product("MacBook Air", 1299, "A thin and light laptop", 5))

import streamlit as st

# Cho phép người dùng thêm sản phẩm mới
name = st.text_input("Product name", key=1)
price = st.number_input("Price")
description = st.text_input("Description")
quantity = st.number_input("Quantity")

if st.button("Add"):
  manager.add_product(Product(name, price, description, quantity))

name = st.text_input("Product name", key=2)
if st.button("Remove"):
  product = manager.get_product(name)
  if product:
    manager.remove_product(product)

# Hiển thị danh sách sản phẩm
products = manager.get_all_products()
for product in products:
  st.write(product.name, product.price, product.description, product.quantity)