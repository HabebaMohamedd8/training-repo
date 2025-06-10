# #
# #
# # def add(x,y):
# #     return x+y
# #
# # def multiply(x,y):
# #     return x* y
# #
# # z=int(input("Select the operation: 1/add , 2/ multiply"))
# #
# # x=int(input("enter the first num"))
# # y=int(input("enter the second num"))
# #
# # if z ==1:
# #     print(add(x,y))
# # else:
# #     print(multiply(x,y))
#
#
# def calculator():
#     print("Calculator")
#     print("1\ add")
#     print("2\ multiply")
#     print("3\ subtract")
#     print("4\ divide")
#     print("5\ AND")
#     print("6\ OR")
#     print("7\ NOT")
#     print("8\ XOR ")
#     print("9\ Generate Truth Table")
#     print("10\ Exit")
#
#     while True:
#         try:
#             choice = input("Enter a number: ")
#
#             if choice == '10':
#                 print("Calculator closed.")
#                 break
#
#             if choice=='1':
#                 a = input("Enter first number ")
#                 b = input("Enter second number ")
#                 print(a+b)
#
#
#             elif  choice=='2':
#                 a = int(input("Enter first number "))
#                 b = int(input("Enter second number "))
#                 print(a * b)
#
#             elif choice == '3':
#                 a = int(input("Enter first number "))
#                 b = int(input("Enter second number "))
#                 print(a - b)
#
#             elif choice == '4':
#                 a = int(input("Enter first number "))
#                 b = int(input("Enter second number "))
#                 print(a / b)
#
#
#             elif choice == '5':
#                 a = input("Enter first value (True/False): ").capitalize()
#                 b = input("Enter second value (True/False): ").capitalize()
#                 a = True if a == "True" else False
#                 b = True if b == "True" else False
#                 print(f"{a} AND {b} = {a and b}")
#
#             elif choice == '6':
#                 a = input("Enter first value (True/False): ").capitalize()
#                 b = input("Enter second value (True/False): ").capitalize()
#                 a = True if a == "True" else False
#                 b = True if b == "True" else False
#                 print(f"{a} OR {b} = {a or b}")
#
#             elif choice == '7':
#                 a = input("Enter value (True/False): ").capitalize()
#                 a = True if a == "True" else False
#                 print(f"NOT {a} = {not a}")
#
#             elif choice == '8':
#                 a = input("Enter first value (True/False): ").capitalize()
#                 b = input("Enter second value (True/False): ").capitalize()
#                 a = True if a == "True" else False
#                 b = True if b == "True" else False
#                 print(f"{a} XOR {b} = {a != b}")
#
#             elif choice == '9':
#                 operator = input("Enter operator (AND/OR/NOT/XOR): ").upper()
#                 if operator == "AND":
#                     print("\nAND Truth Table:")
#                     print("A\tB\tA AND B")
#                     for a in [True, False]:
#                         for b in [True, False]:
#                             print(f"{a}\t{b}\t{a and b}")
#                 elif operator == "OR":
#                     print("\nOR Truth Table:")
#                     print("A\tB\tA OR B")
#                     for a in [True, False]:
#                         for b in [True, False]:
#                             print(f"{a}\t{b}\t{a or b}")
#                 elif operator == "NOT":
#                     print("\nNOT Truth Table:")
#                     print("A\tNOT A")
#                     for a in [True, False]:
#                         print(f"{a}\t{not a}")
#                 elif operator == "XOR":
#                     print("\nXOR Truth Table:")
#                     print("A\tB\tA XOR B")
#                     for a in [True, False]:
#                         for b in [True, False]:
#                             print(f"{a}\t{b}\t{a != b}")
#                 else:
#                     print("Invalid operator!")
#
#             else:
#                 print("Invalid choice! Please enter 1-6.")
#
#         except ValueError:
#             print("Invalid input! Please enter True/False values.")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#
#
# if __name__ == "__main__":
#     calculator()
from http.client import responses

# for num in range(1,21):
#     if num %3 ==0 and num %5==0:
#         print("FizzBuzz")
#     elif num %3==0:
#         print("Fizz")
#     elif num %5==0:
#         print("Buzz")
#     else:
#         print(num)


# def circle_area(radius,pi_const = 3.14):
#     area= pi_const*radius*radius
#     return area
#
# r=int(input("Enter a radius: "))
# print(circle_area(r))

from setup import test2
# from beba.demo import *
#
# hi()


# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# if response.status_code == 200:
#     data = response.json()
#     print("OK")
# else:
#     print("Error:", response.status_code)

import requests
data = {
    "id":1,
    "title":"Updated",
    "body":"From blabla",
    "userId":1
}
response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=data)

print(response.status_code)
print(response.json())


