# 🔄 Vòng lặp `while` trong Python

Trong Python, vòng lặp `while` được sử dụng khi ta **chưa biết trước số lần lặp**, mà chỉ muốn lặp **cho đến khi điều kiện còn đúng**.

---

## 1. `while` cơ bản
Lặp lại khi điều kiện còn đúng.

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

## 2. `while ... else`
Khối `else` chạy khi vòng lặp kết thúc bình thường (không bị `break`).

```python
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Kết thúc vòng lặp")
```

---

## 3. `while True` (vòng lặp vô hạn)
Dùng khi chưa biết số lần lặp, thoát bằng `break`.

```python
while True:
    x = input("Nhập 'q' để thoát: ")
    if x == "q":
        break
```

---

## 4. `while` với `break`
Thoát vòng lặp ngay lập tức khi gặp điều kiện.

```python
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
```

---

## 5. `while` với `continue`
Bỏ qua bước hiện tại, nhảy sang lần lặp kế tiếp.

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```

---

## 6. `while` lồng nhau
Dùng `while` trong `while`.

```python
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
```

---

## 7. `while` với điều kiện logic phức tạp
Kết hợp nhiều điều kiện (`and`, `or`, `not`).

```python
i = 0
j = 3
while i < 5 and j > 0:
    print(i, j)
    i += 1
    j -= 1
```

---

# ✅ Tổng kết
Các dạng `while` phổ biến trong Python:
1. `while` cơ bản  
2. `while ... else`  
3. `while True` (vô hạn)  
4. `while` với `break`  
5. `while` với `continue`  
6. `while` lồng nhau  
7. `while` với điều kiện logic phức tạp  
