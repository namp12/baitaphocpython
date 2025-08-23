# Các hàm `is...()` trong Python

| Hàm                           | Ý nghĩa                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------- |
| `str.isalpha()`               | Chuỗi **toàn chữ cái** (A–Z, a–z, Unicode letters)                                |
| `str.isdigit()`               | Chuỗi **toàn số** (0–9)                                                           |
| `str.isnumeric()`             | Chuỗi toàn **ký tự số** (bao gồm số dạng Unicode như "²")                         |
| `str.isdecimal()`             | Chuỗi toàn **chữ số thập phân** (0–9, không bao gồm số đặc biệt như "²")          |
| `str.isalnum()`               | Chuỗi **chỉ gồm chữ hoặc số** (không có ký tự khác)                               |
| `str.islower()`               | Chuỗi toàn chữ cái thường                                                         |
| `str.isupper()`               | Chuỗi toàn chữ cái hoa                                                            |
| `str.istitle()`               | Chuỗi có dạng **viết hoa chữ cái đầu mỗi từ**                                     |
| `str.isspace()`               | Chuỗi toàn khoảng trắng (space, tab, newline)                                     |
| `str.isprintable()`           | Kiểm tra chuỗi có thể in ra màn hình (không chứa ký tự điều khiển như `\n`, `\t`) |
| `str.isidentifier()`          | Kiểm tra chuỗi có phải là **tên hợp lệ** trong Python (biến/hàm)                  |
| `str.isascii()` (Python 3.7+) | Chuỗi chỉ chứa ký tự ASCII (0–127)                                                |



# Hàm `any()` và `all()` trong Python

| Hàm     | Ý nghĩa                                                                                  |
|---------|------------------------------------------------------------------------------------------|
| `any()` | Trả về **True** nếu **ít nhất một phần tử** trong iterable (list, tuple, set, ...) là True |
| `all()` | Trả về **True** nếu **tất cả các phần tử** trong iterable đều là True                     |



