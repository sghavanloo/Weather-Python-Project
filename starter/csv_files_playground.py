# import csv
# with open("2016_pilbara.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line)
# population = []
# with open ("2016_pilbara.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader (csv_file)
#     for line in reader:
#         population.append(line)
# print(population)
# print()
# for age_group in population:
#     print(f"{age_group[0]} {age_group[1]}")
# with open ("population.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")
#     for age_group in population:
#         csv_writer.writerow([age_group[1], age_group[0]])

# Exersice Reading Q1
# import csv
# population= []
# with open ("colours_20.csv") as csv_file:
#     csv_reader = csv.reader (csv_file, delimiter=",")
#     for row in csv_reader:
#         print (f' {row[1]} {row[2]} {row[3]}')

#Exercises Reading Q2
# import csv
# with open ('colours_20_simple.csv') as csv_file:
#     csv_reader = csv.reader (csv_file, delimiter=',')
#     for i, row in enumerate (csv_reader):
#         if i !=0:
#             print (f'{row[2]}, HEX: {row[1]}, RGB: {row[0]}')
import csv
with open ("2016_pilbara.csv") as csv_file:
    reader = csv.reader (csv_file)
    for line in reader:
        print (line)
    
population = []
with open ("2016_Pilbara.csv", encoding="utf-8") as csv_file:
    reader = csv.reader (csv_file)
    for line in reader:
        population.append(line)
print(population)
print()
for age_group in population:
    print( f"{age_group [0]} {age_group[1]}")