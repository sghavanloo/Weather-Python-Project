# Demonstrate a function
# def create_greeting(name):
#     greeting = f"Hello, {name}!"
#     return greeting
# print(create_greeting ("chilli"))
# print(create_greeting ("Ivy"))
# print(create_greeting ("Remus"))

# def convert_cm_to_in(length_cm):
#     length_in_inches= length_cm /2.54
#     return length_in_inches
# print (convert_cm_to_in(20))
 
# def calculate_mean (a,b):
#     total = a+b
#     mean = total /2
#     return mean
# print (calculate_mean (3,4))

# def tem_in_cel (temp_in_f):
#     temp_in_cel = (temp_in_f -32) *(5/9)
#     return tem_in_cel
#     print(temp_in_cel (32)) 
# def is_odd (num):
#     if num %2 == 0:
#         return True
#     else:
#         return False
# print(is_odd (9))

# def mean(num_list):
#     mean = sum (num_list)/ len (num_list)
#     return mean 
# print (mean ([3,4,6,2]))

def total_cost ( price_per_unit, num_units):
    return price_per_unit*num_units
print(f'${total_cost (4.25,3)}')