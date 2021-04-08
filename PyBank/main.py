import os
import csv

budgetdata = os.path.join(".", "Resources", "budget_data.csv")

#set the output of the text file
text_path = "output.txt"

#Empty Lists of data.
month_list = []
total_months = []
average_change_list = []
date_of_change = []
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
budget_dict = []


# Use encoding for Windows
# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
with open(budgetdata, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #lines = list(csvreader)
    next(csvreader)
    total = 0
    previous_total = 0
    average_change = 0
    budget_count = 0 
    change_Zero = 867884

    for row in csvreader:
#The total number of months included in the dataset
        month_list.append(str(row[1]))

#The net total amount of "Profit/Losses" over the entire period
        revenue = int(row[1])
        total += revenue

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        average_change = int(row[1]) - previous_total
        previous_total = int(row[1])
        average_change_list += [average_change]


        date_of_change = [date_of_change] + [row[0]]

#The greatest increase in revenue (date and amount) over the entire period
        if average_change>greatest_increase[1]:
                greatest_increase[1]= average_change
                greatest_increase[0] = row[0]

#The greatest decrease in revenue (date and amount) over the entire period
        if average_change<greatest_decrease[1]:
                greatest_decrease[1]= average_change
                greatest_decrease[0] = row[0]


# the total number of months included in the dataset.
        total_months = len(month_list)
        total = (total)
average_change_list1 = sum(average_change_list) - change_Zero
#average_change_final = (round(average_change_list1)/(total_months - 1))
average_change_final = str(round(average_change_list1/(total_months - 1), 2))
#write changes to csv
#with open(text_path, 'w') as file:
print("Financial Analysis")
print("--------------------------")
print(f'Total_Months: {total_months}')
print(f'Total: ${total}')
print(f'Average_Change: ${average_change_final}')
print(f'Greatest Increase in Revenue: {greatest_increase[0]},(${greatest_increase[1]})')
print(f'Greatest Decrease in Revenue: {greatest_decrease[0]},(${greatest_decrease[1]})')
print("--------------------------")

# Set variable for output file
output_file = os.path.join(".", "analysis","budget_data_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["--------------------------"])
    datafile.write("Total Months: "+ str(total_months)+"\n")
    datafile.write("Total: $"+ str(total)+"\n")
    datafile.write("Average Change: $"+ str(average_change_final)+"\n")
    datafile.write("Greatest Increase in Revenue: "+ str(greatest_increase[0])+",($"+str(greatest_increase[1])+")\n")
    datafile.write("Greatest Decrease in Revenue: "+ str(greatest_decrease[0])+",($"+str(greatest_decrease[1])+")\n")
    writer.writerow(["--------------------------"])

 