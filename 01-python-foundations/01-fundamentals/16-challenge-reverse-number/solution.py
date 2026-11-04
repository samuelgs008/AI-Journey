# 16 - 🏆 Final Challenge: Reverse Number


n = 1234
i = 100

values = int((n % i) // (i / 10))
print(values)

# place_value = 0
# reversed_value = 0
# digit_sum = 0
# number_of_10 = 0
# number_of_10_done = 0
# last_value = 0
# i = 1

# while (n != n % i):
#     if number_of_10 == 0 and number_of_10_done == 0:
#         while n > 10**(number_of_10 + 1):
#             number_of_10 += 1
#         number_of_10_done = 1
#         loop = number_of_10
#     i *= 10
#     values = int(n % i - last_value)
#     if values > 10:
#         for k in range(number_of_10,0,-1):
#             values = int(values / 10)
#             if 10 > values:
#                 break
#     digit_sum += values
#     last_value = int(n % i)
#     while loop != -1:
#         reversed_value += values * 10**loop
#         loop -= 1
#         break

# print(f"REVERSED = {reversed_value}")
# print(f"DIGIT SUM = {digit_sum}")