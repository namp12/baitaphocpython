# a = int(input("nhập vào số a: "))
#? 📘 50 BÀI TẬP PYTHON VỀ if - else
#? Nhóm 1: Cơ bản (1–10)
#* 1. Kiểm tra một số có phải là số dương hay không.
# if a > 0:
# 	print("so duong")
# else:
# 	print("so am")

#* 2. Kiểm tra một số có phải là số âm hay không.
# if a < 0:
# 	print("so am")
# else:
# 	print("so duong")

#* 3.Kiểm tra một số có bằng 0 hay không.
# if a == 0:
# 	print("la so 0")
# else:
# 	print("0 phai so 0")

#* Kiểm tra một số có lớn hơn 100 hay không.
# if a > 100:
# 	print("so lon hon 100")
# else:
# 	print("so nho hon 100")

#* Kiểm tra một số có nhỏ hơn 20 hay không.
# if a > 20:
# 	print("so lon hon 20")
# else:
# 	print("so nho hon 20")

#* Kiểm tra một số có chia hết cho 2 hay không.
# if a % 2 == 0:
# 	print("so chia het cho 2")
# else:
# 	print("so khong chia het cho 2")

#* Kiểm tra một số có chia hết cho 5 hay không.
# if a % 5 == 0:
# 	print("so chia het cho 5")
# else:
# 	print("so khong chia het cho 5")

#* Kiểm tra một số có phải là số chẵn hay số lẻ.
# if a % 2 == 0:
# 	print("so chia het chan")
# else:
# 	print("la so le")

#* Kiểm tra một số có phải là bội số của 3 không.
# if a % 3 == 0:
#     print("x là bội số của 3")
# else:
#     print("x không phải bội số của 3")

#* Nhập tuổi → kiểm tra xem đã đủ 18 tuổi hay chưa.
# if a >= 18:
# 	print("đủ 18 ")
# else:
# 	print("lượn")


#? Nhóm 2: So sánh số (11–20)
# a = int(input("nhap so a: "))
# b = int(input("nhap so b: "))
# c = int(input("nhap so c: "))
#* So sánh hai số, in ra số lớn hơn.
# if a > b:
# 	print(f"so lon hon la: {a}")
# elif b > a:
# 	print(f"so lon hon la: {b}")
# else:
# 	print(f"hai so bang nhau {a}, {b}")

# #* So sánh hai số, in ra số nhỏ hơn.
# if a > 0 and b > 0:
#     print(f"{a} cung dau voi {b}")
# if a < 0 and b < 0:
#     print(f"{a} cung dau voi {b}")
# elif a > 0 and b < 0:
#     print(f"{a} khac dau voi {b}")
    
# #* So sánh ba số, tìm số lớn nhất.
# if a >= b and a >= c:
#     print("Số lớn nhất là:", a)
# elif b >= a and b >= c:
#     print("Số lớn nhất là:", b)
# else:
#     print("Số lớn nhất là:", c)
    
# #* So sánh ba số, tìm số nhỏ nhất.
# if a <= b and a <= c:
#     print("Số nhỏ nhất là:", a)
# elif b <= a and b <= c:
#     print("Số nhỏ nhất là:", b)
# else:
#     print("Số nhỏ nhất là:", c)
    
# #* Kiểm tra xem hai số có bằng nhau hay không.
# if a == b:
#     print("hai so bang nhau")
# else:
#     print("hai so khac nhau")

# #* Kiểm tra xem một số có nằm trong đoạn [10, 50] hay không.
#* cách 1:
# if 10 <= a <= 50:
#     print(f"{a}, nằm trong đoạn 10 - 50")
# else:
#     print("khong nam trong khoan")

#* cách 2:
# if a in range(10, 51):
#     print("nam trong")

#* Kiểm tra xem một số có nằm ngoài đoạn [100, 200] không.
# if a in range(100, 201):
# 	print("co nam trong")
# else:
# 	print("khong nam trong")
	
#* Nhập vào hai số, kiểm tra xem chúng có cùng dấu không.
#* cách 1:
# if (a > 0 and b > 0) or (a < 0 and b < 0):
# 	print("hai so cung dau")
# else:
# 	print("hai so khac dau")

#* hai so khac dau
# if a * b > 0:
# 	print("Hai so cung dau")
# else:
# 	print("Hai so khac dau")
	
#* Kiểm tra một số có phải là số nguyên tố nhỏ hơn 10 không.
# if a < 2:
# 	print("khong phai so nguyen to")
# else:
# 	iss = True
# 	for i in range(2, a):
# 		if a % i == 0:
# 			iss = False
# 			break
#     if iss:
# 	    print("la so nguyen to")
# 	else:
#         print("khong chia het cho 2")
#* Kiểm tra xem một năm có phải là năm nhuận hay không.
# year = int(input("Nhập năm: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} là năm nhuận")
# else:
#     print(f"{year} không phải năm nhuận")



#? Nhóm 3: Xử lý chuỗi (21–30)
s = input("mời nhập chuỗi: ")
#* Nhập chuỗi → kiểm tra chuỗi có rỗng không.
# if s == "":
# 	print("chuỗi rỗng")
# else:
# 	print("chuỗi không rỗng")
	
# #* Kiểm tra chuỗi có chứa ký tự số không.
# print(any(ch.isdigit() for ch in s))

# #* Kiểm tra chuỗi có phải toàn chữ in hoa không.
# if s.isupper:
# 	print("chuoi toan chu in hoa")
# else:
# 	print("chuoi khong co chu in hoa")
	
# #* Kiểm tra chuỗi có phải toàn chữ in thường không.
# if s.islower:
# 	print("chuoi thuong")
# else:
# 	print("chuoi hoa")
	
# #* Kiểm tra chuỗi có bắt đầu bằng ký tự "a" không.
# # cách 1:
# if s.startswith == "a":
# 	print("bat dau bang chu a")
# else:
# 	print("khong bat dau bang chu a")
	
# # cách 2:
# if s[0] == "a":
# 	print("bat dau bang chu a")
# else:
# 	print("khong bat dau bang chu a")
	
# #* Kiểm tra chuỗi có kết thúc bằng ký tự "z" không.
# # cách 1:
# if s.endswith("z"):
#     print("Chuỗi kết thúc bằng chữ 'z'")
# else:
#     print("Chuỗi KHÔNG kết thúc bằng chữ 'z'")

# # cách 2:
# if s and s[-1] == "z":   # s[-1] lấy ký tự cuối cùng
#     print("Chuỗi kết thúc bằng chữ 'z'")
# else:
#     print("Chuỗi KHÔNG kết thúc bằng chữ 'z'")
	
# #* Kiểm tra chuỗi có độ dài lớn hơn 5 không.
# if len(s) > 5:
# 	print("chuoi lon hon 5")
# else:
# 	print("chuoi be hon 5")
	
#* Kiểm tra ký tự đầu tiên có phải là chữ cái viết hoa không.
# if s.istitle:
# 	print("chuoi dau co viet hoa")

#* Kiểm tra chuỗi có phải là chuỗi đối xứng (palindrome).

#* Nhập mật khẩu → kiểm tra có đủ 8 ký tự trở lên không.

#? Nhóm 4: Lồng nhau & nhiều điều kiện (31–40)

#* Nhập điểm → phân loại (Giỏi ≥ 8, Khá ≥ 6.5, TB ≥ 5, Yếu < 5).

#* Nhập số → kiểm tra số dương chẵn, dương lẻ, âm chẵn, âm lẻ.

#* Nhập số → kiểm tra thuộc khoảng (0, 50), (50, 100) hay ngoài 100.

#* Kiểm tra số có chia hết cho cả 3 và 5 không.

#* Kiểm tra số có chia hết cho 3 nhưng không chia hết cho 5.

#* Nhập ba cạnh tam giác → kiểm tra có tạo thành tam giác không.

#* Nếu tạo được tam giác, phân loại: đều, cân, vuông, thường.

#* Nhập một tháng → in ra số ngày trong tháng.

#* Kiểm tra số có phải số Armstrong (153, 370, …).

#* Kiểm tra số có phải số hoàn hảo (6, 28, …).



#? Nhóm 5: Thực tế & ứng dụng (41–50)

#* Nhập giờ → kiểm tra là sáng, trưa, chiều hay tối.

#* Nhập nhiệt độ → kiểm tra: lạnh (<20), mát (20–29), nóng (30–39), rất nóng (≥40).

#* Nhập cân nặng & chiều cao → tính BMI và phân loại.

#* Nhập số điện → tính tiền điện theo bậc thang.

#* Nhập số km taxi → tính tiền cước.

#* Nhập điểm kiểm tra → xét học bổng (>=8.0).

#* Nhập thu nhập → tính thuế thu nhập cá nhân.

#* Nhập năm sinh → tính tuổi & phân loại: trẻ em, thiếu niên, người lớn, người già.

#* Nhập số giờ làm → tính tiền lương (>=40h có thêm overtime).

#* Trò chơi: nhập số dự đoán → kiểm tra đúng/sai với số bí mật.




