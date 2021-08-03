# user_input = input ("please enter a number between 1 to 9 ")
# for number in range (int(user_input)):
#     print(f"{user_input} * {number +1} = {int (user_input) * (number +1)}")
# enter= input(" what is your fav number? ")
# for x in range (int(enter)):
#     print()
# mailing_list = [
#     ["Chilli", "chilli@thechihuahua.com"],
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Ivy", "noreply@goldendreamers.xyz"],
# ]
# for item in mailing_list:
# #     print(f"{item[0]}:{item[1]}")
# from functions_playground import total_cost


groceries = [
    ["Baby Spinach", 2],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
    ]
# unit = input ('Hoe many units of {Baby Spinach} did you buy?'.format(Baby Spinach=item))
receipt = []
totalCost = 0
# For each item in the list of groceries...
for item in groceries:
    # Ask the user for the number of units they bought
    units = input('How many units of {itemName} did you buy? '.format(itemName=item[0]))
    # Calculate the cost by multiplying the item's price by the number of units bought
    itemCost = item[1] * units
    # Increment the total cost by the new item cost
    totalCost += itemCost
    # Create the new receipt line item
    receipt.append('{name} ${cost}'.format(name=item[0], cost=itemCost))
print("====Izzy's Food Emporium====")
for lineItem in receipt:
    print(lineItem)
print("============================")
print(totalCost)