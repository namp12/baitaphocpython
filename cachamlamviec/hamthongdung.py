# item = input("what item would you like to buy?: ")
# price = float(input("what is the price?: "))
# quantity = float(input("how many would you like?: "))
# total = price * quantity
#
# print(f"you have bought {quantity} x {item}/s")
# print(f"you total is ${total}")

# trò chơi nối từ
# name = input("nhập tên của một người: ")
# food = input("nhập một món ăn nào đó: ")
# reason = input("nhập khẩu vị")
# trangthai = input("nhập trạng thái cá nhân (độc thân, có ny, đã kết hôn, góa) ")
# print(f"tôi có người bạn tên là {name}")
# print(f"anh ấy thích ăn {food} vì nó rất {reason}")
# print(f"anh ấy còn {trangthai}. ")

# số học
# x = 3.14
# y = -4
# z = 5
# result = round(x)      # hàm làm tròn
# result = abs(y)        # hàm giá trị tuyệt đối
# result = pow(4, 3)     # hàm lũy thừa
# result = min(x, y, z)  # hàm tìm số lớn nhất, nhỏ nhất.

# import math
# x = 9.6
# print(math.pi)
# print(math.e)
# # result = math.sqrt(x)  # hàm căn bặc 2
# # result = math.ceil(x)    #hàm làm tròn lên
# result = math.floor(x)   # làm tròn hàm xuống
# print(result)


# age = int(input("nhập tuổi của bạn: "))
# cccd = input("bạn đã từng có căn cước công dân trước đây? (yes/no): ").strip().lower()
# tung_hoc = input("bạn đã từng học ở đây trước chưa? (yes/no): ").strip().lower()

# cccd = cccd == "yes"
# tung_hoc = tung_hoc == "yes"

# if (18 <= age <= 35) and cccd and not tung_hoc:
# 	print("bạn đủ điều kiện để học....")
# else:
# 	print("bạn không đủ điều kiện để học.... cryyy")
# 	if age < 18 or age > 35:
# 		print("tuổi của bạn không trong khoảng 18 - 35")
# 	if not cccd:
# 		print("bạn không có cccd - cmnd")
# 	if tung_hoc:
# 		print("bạn đã từng học lớp này trước đó")

# num = 6
# # print("duong" if num > 0 else "am")
# result = "chia het cho 2" if num % 2 == 0 else "khong chia het cho 2"
# print(result)
#* tính max num
# num1 = int(input("nhập số thứ nhất: "))
# num2 = int(input("nhập số thứ 2 : "))
# max_num = f"{num1} là số cao nhất" if num1 > num2 else f"{num2} là số cao nhất"
# print(max_num)	

#* chuỗi
name = input("nhập họ và tên của bạn: ")
result = name.find("p")
result = name.rfind("n")   # tìm ngược lại 
name = name.capitalize() 	# viết hoa chữ cái đầu
print(name)
print(result)