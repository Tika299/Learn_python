# #In hello word ra màn hình
# print("Hello Word")
# # thực hiện dùng biến
# a = 29092005
# b = 18082004
# c = a+b
# print(c)

# #inport thử viên decimal
# from decimal import *
# #lấy tối đã 30 chữ số phần nguyên và phần thập phân decimal
# getcontext().prec = 30
# k = 10
# h = 3
# print(Decimal(k)/Decimal(h))

#import thư viên fractions
# from fractions import*
# a = Fraction(6,9)
# print(a)

#số phức trong python
# c = complex(2,5)
# print(c)
# print(c.real)
# print(c.imag)

# strtest = ''''"Heloo
# le 'xuan vu
# '''
# print(strtest)

# class SomeThing:
#         def __repr__(self):
#                 return 'Đây là __repr__'
#         def __str__(self):
#              return 'Đây là __str__'
# sthing = SomeThing()
# print('%s'%(sthing))

# r = '1: {one},2: {two}'.format(one = 111, two=222)
# print(r)

s = input('Xin nhap so bat ky: ')
print('So vua nhap la: ',s)