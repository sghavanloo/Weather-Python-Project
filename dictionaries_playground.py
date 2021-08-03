# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Bacon": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08,
# }
# quantity = {
#     "Baby Spinach":1,
#     "Hot Chocolate":3,
#     "Crackers":2,
#     "Bacon":1,
#     "Carrots":4,
#     "Oranges":2,
# }
# # print(groceries ["Baby Spinach"])
# # groceries["Avocadoes"]= 1.00
# # groceries["Hot Chocolate"]=2.70
# # del groceries["Crackers"]
# # print(groceries)
# #  for item in groceries:
# #     print(f"{item}:${groceries[item]}")
# #     print()
# # for item,price in groceries.items():
# #     print(f"{item}: ${price}")
# for key in groceries:
#    calculation = round (groceries[key] * quantity[key], 2)
#    print(f"{quantity[key]} {key} @ $ {groceries[key]} = ${calculation} ")

# colour_counts = {
#     "blue": 0,
#     "green": 0,
#     "yellow": 0,
#     "red": 0,
#     "purple": 0,
#     "orange": 0,
#     }
# colours = ["purple","red","yellow","blue","purple","orange","blue","purple","orange","green"]

# for item in colours:
#     colour_counts[item] +=1
# for key, value in colour_counts.items():
#     print(f"{key}:{value}")

names = ["Maddy", "Bel", "Elnaz", "Gia", "Izzy",
            "Joy", "Katie", "Maddie", "Tash", 
            "Nic","Rachael", "Bec", "Bec", "Tabitha", 
            "Teagen","Viv", "Anna", "Catherine", "Catherine", 
            "Debby","Gab", "Megan", "Michelle", "Nic", "Roxy",
            "Samara", "Sasha", "Sophie", "Teagen", "Viv"
        ]
unique_names = dict.fromkeys(names,0)
dictionary = unique_names
for item in names:
    dictionary [item] +=1
for key, value in dictionary.items():
    print(f" {key}: {value}")