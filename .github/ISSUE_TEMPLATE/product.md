---
title: "Bảng thông tin sản phẩm"
name: "Danh sách sản phẩm công nghệ"
about: "Thông tin chi tiết về giá và tồn kho của các mẫu laptop"
products:
  - name: Laptop A
    price: 1500
    stock: 20
  - name: Laptop B
    price: 1200
    stock: 15
  - name: Laptop C
    price: 1000
    stock: 10
---

# {{ page.title }}

**Người tạo:** {{ page.name }}  
**Giới thiệu:** {{ page.about }}

## Danh sách sản phẩm

| Tên sản phẩm | Giá (USD) | Tồn kho |
|--------------|-----------|---------|
{% for product in page.products %}
| {{ product.name }} | {{ product.price }} | {{ product.stock }} |
{% endfor %}
