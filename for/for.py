# ==============================
# 60 BÀI TẬP VÒNG FOR TRONG PYTHON
# ==============================

#? --- 1. Duyệt cơ bản ---
#* 1. In các số từ 1 đến 10.
# for i in range(1, 11):
# 	print(i)

#* 2. In các số chẵn từ 2 đến 20.
# for i in range(2, 21, 3):
# 	print(i)
#* 3. In các số lẻ từ 1 đến 19.
# for i in range(1, 20):
# 	if i % 2 != 0:
# 		print(i)

# for i in range(1, 20, 2):
# 	print(i)
#* 4. In bảng cửu chương của 5.
# for i in range (1, 11):
# 	print(f"5 x {i} = {5 * i}")

#* 5. In tất cả bảng cửu chương từ 1 đến 9.
# for i in range (1, 10):
# 	for j in range(1, 11):
# 		print(f"{i} x {j} = {i * j}")
# 	print("-" * 20)

#* 6. Tính tổng các số từ 1 đến 100.
# total = 0
# for i in range(1, 101):
# 	total += i
# 	print(f"tổng = {total}")

#* 7. Tính tích các số từ 1 đến 10.
# total = 0
# for i in range(1, 11):
# 	total += i
# 	print(f"tổng = {total}")

#* 8. Đếm số ký tự trong một chuỗi (không dùng len).
# s = input("nhap chuoi: ")
# count = 0
# for ch in s:
# 	count += 1
# 	print(f"chuoi {s}: {count}")

#* 9. In từng ký tự trong chuỗi "Python".
# s = "python"
# for ch in s:
# 	print(ch)

#* 10. In từng phần tử trong danh sách [1, 3, 5, 7, 9].
# ds = [1, 3, 5, 7, 9]
# for x in ds:
# 	print(x)

#* --- 2. Dùng range() ---
#* 11. In các số từ 10 đến 1 (giảm dần).
# for i in range(10, 0, -1):
# 	print(i)

#* 12. In các số từ 0 đến 50, bước nhảy 5.
# for i in range(0, 51, 5):
# 	print(i)

#* 13. In số từ 100 đến 50, bước nhảy -10.
# for i in range(100, 49, -10):
# 	print(i)

#* 14. In bình phương các số từ 1 đến 10.
# for i in range(1, 11):
# 	print(f"binh phuong cua {i} = {i * i}")

#* 15. In lập phương các số từ 1 đến 10.
# for i in range(1, 11):
#  	print(f"lap phuong cua {i} = {i * i * i}")
	 
#* 16. Tính tổng các số chẵn từ 1 đến 100.
# tong = 0
# for i in range(1, 101):
# 	if i % 2 == 0:
# 		tong += i
# 		print(f"tong {i} = {tong}")

#* 17. Tính tổng các số lẻ từ 1 đến 100.
# tong = 0
# for i in range(1, 101):
# 	if i % 2 != 0:
# 		tong += i
# 		print(f"tong {i} = {tong}")

#* 18. Tính tổng bình phương từ 1 đến 20.
# tong = 0
# for i in range(1, 21):
# 	tong += i**2
# 	print(f"tong binh phuong cua {i}: {tong}")

#* 19. Tính tổng lập phương từ 1 đến 20.
# tong = 0
# for i in range(1, 21):
# 	tong += i*i*i
# 	print(f"tong binh phuong cua {i}: {tong}")

#* 20. Tìm số lớn nhất trong danh sách bằng for.
# numbers = [3, 7, 2, 9, 5, 10, 6]

#* cách 3:
# max_num = numbers[0]
# for i, num in enumerate(numbers):
#     if num > max_num:
#         max_num = num

# print("Số lớn nhất là:", max_num)

#* cách 2:
# max_num = numbers[0]
# for i in range(1, len(numbers)):
#     if numbers[i] > max_num:
#         max_num = numbers[i]

# print("Số lớn nhất là:", max_num)

#* cách 1:
# max_num = numbers[0]   # giả sử phần tử đầu tiên là lớn nhất
# for num in numbers:
#     if num > max_num:
#         max_num = num

# print("Số lớn nhất là:", max_num)

#* --- 3. Chuỗi và danh sách ---
#* 21. Đếm số nguyên âm trong chuỗi.
# s = "Hello Python Programming"
# count = 0
# vowels = "aeiouAEIOU"   # bao gồm cả chữ hoa và thường

# for ch in s:
#     if ch in vowels:
#         count += 1

# print("Số nguyên âm trong chuỗi là:", count)

#* 22. Đếm số ký tự số trong chuỗi.
# s = input("nhap chuoi: ")
# count = 0
# for i in s:
# 	count += 1
# 	print(count)

#* 23. Đảo ngược chuỗi bằng vòng for.
# s = input("nhap chuoi: ")
#* cách 1:
# rev = "".join(reversed(s))
# print(f"chuỗi đảo ngược là: {rev}")

#* cách 2: slicing
# rev = s[::-1]
# print(rev)
#* 24. Kiểm tra chuỗi có chứa ký tự "a".
# s = "python width chatgpt"
# find trả về chỉ số đầu tiên nếu tìm thấy
# print(s.find("a"))

# index giống find nhưng nếu sai trả về lỗi
# print(s.index("a"))

# dùng count đếm số lần xuất hiện
# print(s.count("a"))

# s = "phuong nam"
# am = "pn"
# print(any(ch in am for ch in s))
#* 25. Xóa tất cả khoảng trắng trong chuỗi.

#* 26. In tất cả phần tử trong danh sách 2 chiều.
#* 27. Tính tổng phần tử trong danh sách [2,4,6,8].
#* 28. Tìm phần tử lớn nhất trong danh sách.
#* 29. Tìm phần tử nhỏ nhất trong danh sách.
#* 30. Đếm số phần tử lớn hơn 10 trong danh sách.

#* --- 4. Bài toán số học ---
#* 31. In dãy Fibonacci 10 số đầu tiên.
#* 32. Kiểm tra một số có phải số nguyên tố.
#* 33. Liệt kê các số nguyên tố nhỏ hơn 100.
#* 34. Liệt kê ước của một số.
#* 35. Tính giai thừa của một số.
#* 36. Tính tổng các ước của một số.
#* 37. Kiểm tra số hoàn hảo.
#* 38. Kiểm tra số Armstrong.
#* 39. In các số đối xứng (palindrome) nhỏ hơn 200.
#* 40. In các số chia hết cho cả 3 và 5 trong [1, 100].

#* --- 5. Dạng lồng nhau (nested loop) ---
#* 41. Vẽ hình vuông bằng dấu *.
#* 42. Vẽ tam giác vuông bằng dấu *.
#* 43. Vẽ tam giác cân bằng dấu *.
#* 44. Vẽ hình chữ nhật m x n.
#* 45. Vẽ tam giác số (1 → n).
#* 46. Vẽ tam giác Pascal.
#* 47. Vẽ bàn cờ caro (ô đen trắng).
#* 48. Vẽ bảng cửu chương dạng bảng.
#* 49. In ma trận đơn vị n x n.
#* 50. In tam giác đảo ngược bằng *.

#* --- 6. Ứng dụng nâng cao ---
#* 51. Duyệt dict và in key, value.
#* 52. Duyệt set và in phần tử.
#* 53. Ghép 2 list bằng for.
#* 54. Tính tổng ma trận 2D.
#* 55. Ma trận chuyển vị.
#* 56. Tìm phần tử xuất hiện nhiều nhất trong list.
#* 57. Lọc số chẵn từ list.
#* 58. Lọc số nguyên tố từ list.
#* 59. Tính tổng các số trong chuỗi "12345".
#* 60. Đếm số từ trong chuỗi.

# ==============================
# HẾT - 60 BÀI TẬP FOR
# ==============================
