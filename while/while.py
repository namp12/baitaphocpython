# ==========================
# 📘 60 BÀI TẬP VỚI WHILE
# ==========================
from rsa.prime import is_prime

# --- Nhóm 1: Cơ bản với số ---
#* 1. In các số từ 1 đến 10 bằng while
# i = 1
# while i < 11:
# 	print(i)
# 	i+= 1

#* 2. In các số chẵn từ 2 đến 20 bằng while
# i = 1
# while i < 20:
# 	if i % 2 == 0:
# 		print(i)
# 	i+=1

#* 3. In các số lẻ từ 1 đến 19 bằng while
# i = 1
# while i < 20:
# 	if i % 2 != 0:
# 		print(i)
# 	i += 1	

#* 4. In ngược các số từ 10 về 1
# i = 10
# while i >= 1:
# 	print(i)
# 	i -= 1

#* 5. Tính tổng các số từ 1 đến 100 bằng while
# i = 1
# tong = 0
# while i < 100:
# 	tong += i
# 	i += 1
# 	print(tong)

#* 6. Tính tổng các số chẵn từ 1 đến 50 bằng while
# i = 1
# tong = 0
# while i < 50:
# 	if i % 2 == 0:
# 		tong += i
# 	i += 1
# 	print(tong)	

#* 7. Tính tổng các số lẻ từ 1 đến 50 bằng while
# i = 1
# tong = 0
# while i < 50:
# 	if i % 2 != 0:
# 		tong += i
# 	i += 1
# 	print(tong)	

#* 8. Tính tổng bình phương các số từ 1 đến 20
# i = 1
# while i < 20:
# 	tong += i * i
# 	i += 1
# print("tong: ", tong)

#* 9. Tính giai thừa của một số n nhập vào
# n = int(input("nhap vao: "))
# i = 1
# giaithua = 1
# while i <= n:
# 	giaithua *= n
# 	i += 1
# print(f"tong {n}: {giaithua}")
	

# 10. In bảng cửu chương của một số n bằng while
# i = 1
# while i <= 10:
# 	j = 1
# 	while j <= 10:
# 		print(f"{i} x {j} = {i * j}")
# 		j += 1 
# 	print("-" * 20)
# 	i += 1

# --- Nhóm 2: Xử lý số nguyên ---
#* 11. Đếm số chữ số của một số nguyên
# n = int(input("Nhập số nguyên: "))
# count = 0
# temp = abs(n)   # lấy trị tuyệt đối để tránh số âm
# if temp == 0:
#     count = 1
# else:
#     while temp > 0:
#         count += 1
#         temp //= 10   # bỏ đi chữ số cuối
# print(f"Số {n} có {count} chữ số")

#* 12. Tính tổng các chữ số của một số nguyên
# n = int(input("Nhập số nguyên: "))
# temp = abs(n)   # tránh số âm
# tong = 0

# while temp > 0:
#     digit = temp % 10     # lấy chữ số cuối
#     tong += digit         # cộng vào tổng
#     temp //= 10           # bỏ chữ số cuối

# print(f"Tổng các chữ số của {n} là: {tong}")

#* 13. Kiểm tra một số có phải số đảo ngược (palindrome) không
# n = int(input("Nhập số cần kiểm tra: "))
# temp = n       # lưu lại giá trị ban đầu
# rev = 0        # số đảo ngược

# while n > 0:
#     digit = n % 10        # lấy chữ số cuối
#     rev = rev * 10 + digit  # thêm vào số đảo ngược
#     n //= 10              # bỏ chữ số cuối

# if temp == rev:
#     print(f"{temp} là số palindrome")
# else:
#     print(f"{temp} không phải số palindrome")
    
#* 14. In số đảo ngược của một số nguyên
# n = int(input("Nhập số nguyên: "))
# rev = 0
#
# while n > 0:
#     digit = n % 10          # lấy chữ số cuối
#     rev = rev * 10 + digit  # thêm vào số đảo ngược
#     n //= 10                # bỏ chữ số cuối
#
# print("Số đảo ngược là:", rev)

# 15. Tìm chữ số lớn nhất trong một số nguyên
# n = int(input("nhap so nguyen: "))
# max_digit = 0
# while n > 0:
#     digit = n % 10
#     if digit > max_digit:
#         max_digit = digit
#     n //= 10
#
# print(f"chu so lon nhat la: {max_digit}")

 # 16. Tìm chữ số nhỏ nhất trong một số nguyên
# n = int(input("nhap so nguyen: "))
# min_digit = n % 10
# while n > 0:
#     digit = n % 10
#     if digit < min_digit:
#         min_digit = digit
#     n //= 10
# print(f"so nguyen nho nhat la {min_digit}")

# 17. Kiểm tra một số có phải số Armstrong không
# n = int(input("nhap so nguyen: "))
# k = len(str(n))
# temp = n
# Armstrong_sum = 0
# while temp > 0:
#     digit = temp % 10
#     Armstrong_sum += digit ** k
#     temp //= 10
# if Armstrong_sum == n:
#     print(f"{n} la so amstrong")
# else:
#     print(f"{n} khong phai la so amstrong")

# 18. Liệt kê tất cả ước của một số nguyên
# n = int(input("nhap so nguyen: "))
# i = 1
# print(f"cac uoc cua {n} la: ")
# while i <= n:
#     if n % i == 0:
#         print(i, end="-")
#     i += 1

# 19. Tính tổng các ước của một số nguyên
# n = int(input("nhap so nguyen: "))
# i = 1
# tong = 0
# while i <= n:
#     if n % i == 0:
#         tong += i
#     i += 1
# print(f"Tổng các ước của {n} là: {tong}")

# 20. Kiểm tra một số có phải số nguyên tố không
# n = int(input("Nhập số nguyên: "))
#
# if n <= 1:
#     print(f"{n} không phải là số nguyên tố")
# else:
#     is_prime = True
#     for i in range(2, int(n**0.5) + 1):  # căn bậc 2
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{n} là số nguyên tố")
#     else:
#         print(f"{n} không phải là số nguyên tố")



# --- Nhóm 3: Dãy số ---
# 21. In dãy Fibonacci đến n phần tử
# 22. Tính tổng dãy Fibonacci đến n phần tử
# 23. In dãy số tam giác (1,3,6,10,...) đến n
# 24. In dãy số bình phương (1,4,9,16,...) đến n
# 25. In dãy số lập phương (1,8,27,...) đến n
# 26. In tất cả số nguyên tố nhỏ hơn n
# 27. Tính tổng các số nguyên tố nhỏ hơn n
# 28. Đếm số nguyên tố nhỏ hơn n
# 29. In dãy số chia hết cho 3 nhỏ hơn 100
# 30. In dãy số chia hết cho 5 nhỏ hơn 100

# --- Nhóm 4: Xử lý chuỗi ---
# 31. Nhập chuỗi → đếm số ký tự (không dùng len)
# 32. In từng ký tự của chuỗi bằng while
# 33. In chuỗi đảo ngược bằng while
# 34. Đếm số nguyên âm trong chuỗi
# 35. Đếm số phụ âm trong chuỗi
# 36. Đếm số chữ hoa trong chuỗi
# 37. Đếm số chữ thường trong chuỗi
# 38. Đếm số ký tự số trong chuỗi
# 39. Đếm số khoảng trắng trong chuỗi
# 40. Kiểm tra chuỗi có phải palindrome không (chuỗi đối xứng)

# --- Nhóm 5: Danh sách ---
# 41. In từng phần tử trong danh sách bằng while
# 42. Tính tổng các phần tử trong danh sách
# 43. Tìm số lớn nhất trong danh sách
# 44. Tìm số nhỏ nhất trong danh sách
# 45. Đếm số chẵn trong danh sách
# 46. Đếm số lẻ trong danh sách
# 47. Đếm số âm trong danh sách
# 48. Đếm số dương trong danh sách
# 49. Đếm số nguyên tố trong danh sách
# 50. Tính trung bình cộng của danh sách

# --- Nhóm 6: Bài toán nâng cao ---
# 51. Nhập một số → đổi sang hệ nhị phân bằng while
# 52. Nhập một số → đổi sang hệ thập lục phân bằng while
# 53. Nhập một số → kiểm tra có phải số hoàn hảo không
# 54. In tất cả số hoàn hảo nhỏ hơn 1000
# 55. In tất cả số Armstrong nhỏ hơn 1000
# 56. In tam giác số (1, 22, 333, ...)
# 57. In tam giác ngược (12345, 1234, ...)
# 58. Vẽ tam giác Pascal bằng while
# 59. In hình vuông sao (*) cạnh n
# 60. In hình tam giác sao (*) cân đối bằng while

