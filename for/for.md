# Python For Loops – Các dạng sử dụng

Trong Python, vòng lặp `for` có rất nhiều cách dùng. Đây là tổng hợp các dạng phổ biến nhất.

---

## 1. For với `range()`
- **Duyệt dãy số liên tiếp**.
```python
for i in range(5):   # 0 → 4
    print(i)
```

- **Có start, stop, step**:
```python
for i in range(2, 11, 2):  # 2, 4, 6, 8, 10
    print(i)
```

---

## 2. For với chuỗi (string)
- **Duyệt từng ký tự**:
```python
for ch in "Python":
    print(ch)
```

---

## 3. For với List
```python
nums = [10, 20, 30]
for x in nums:
    print(x)
```

---

## 4. For với Tuple
```python
t = (1, 2, 3)
for x in t:
    print(x)
```

---

## 5. For với Set
```python
s = {1, 2, 3}
for x in s:
    print(x)
```

---

## 6. For với Dictionary
- **Duyệt key**:
```python
d = {"a": 1, "b": 2}
for k in d:
    print(k)
```

- **Duyệt value**:
```python
for v in d.values():
    print(v)
```

- **Duyệt cả key và value**:
```python
for k, v in d.items():
    print(k, v)
```

---

## 7. For lồng nhau (nested loop)
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

## 8. For với `enumerate()`
- **Lấy index và value cùng lúc**:
```python
names = ["A", "B", "C"]
for i, name in enumerate(names):
    print(i, name)
```

---

## 9. For với `zip()`
- **Duyệt nhiều list song song**:
```python
a = [1, 2, 3]
b = ["one", "two", "three"]

for x, y in zip(a, b):
    print(x, y)
```

---

## 10. For với `else`
- **Chạy `else` khi vòng for kết thúc bình thường (không bị break)**.
```python
for i in range(5):
    print(i)
else:
    print("Kết thúc vòng for")
```

---

## 11. Comprehension (ngắn gọn)
- **List comprehension**:
```python
squares = [x*x for x in range(6)]
```

- **Set comprehension**:
```python
unique = {x % 3 for x in range(10)}
```

- **Dict comprehension**:
```python
d = {x: x*x for x in range(5)}
```

---

# ✅ Tổng kết
Các dạng `for` trong Python:
- `for + range()`
- `for + chuỗi`
- `for + list/tuple/set`
- `for + dict` (keys, values, items)
- `for lồng nhau`
- `for + enumerate`
- `for + zip`
- `for ... else`
- `comprehension (list/set/dict)`
