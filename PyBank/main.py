#Dependencies
import os
import csv

# Create the path name toa ccess the bank data in a csv file
with open('PyBank_Resources_budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        row num = row_num +1
Date = []
Profit = []
row_num = 0

total month = row_num-1
print(f"Total_months: {total_month}")





# txt file
with open('main2.txt', 'w')as txt:
    txt.write("Financial Analysis"='\n')
    txt.write(f"Total months: {total_month}"+'\n')
    txt.write(f"Total: {total}"'\n')


final 
