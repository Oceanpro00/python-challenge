# Importing the Dependencies

import os
import csv

# File Path Designations for CSV Input and TXT Output

csv_input = os.path.join("Resources", "budget_data.csv")
txt_output = os.path.join("analysis", "PyBank_Analysis.txt")

# Defining required Variables for Data Measurements

total_Month = 0
total_net = 0
last_num = 0
change_list = []
avg_Change = 0
months_list = []
greatest_increase_Count = 0
greatest_decrease_Count = 0 

# Open and read the Input CSV file

with open(csv_input, encoding="UTF-8") as csv_data:

	read = csv.reader(csv_data, delimiter=",")

# skip and store header

	header = next(read)

# a for loop to go through all values

	for i in read:

	# Calculate Total Month

		total_Month += 1

	# Calculate Total Net

		total_net += int(i[1])

	# Creates a list of all Changes and another with the months

		change = -(last_num - int(i[1]))
		change_list.append(change)
		last_num = int(i[1])

		months_list.append(i[0])
	
# Remove first list Variable
	months_list.pop(0)
	change_list.pop(0)

# Calculate avg_Change

	avg_Change = round((sum(change_list)/len(change_list)),2)

# Zip together the months list and change list

	PL_change = list(zip(months_list,change_list))

# Conditional statements inside a for loop to find and define Greatest Increase/ Decrease
	
	for i in PL_change:

		if int(i[1]) > greatest_increase_Count:

			greatest_increase_Count = int(i[1])
			greatest_Increase = f"{i[0]} (${greatest_increase_Count})"

		elif int(i[1]) < greatest_decrease_Count:

			greatest_decrease_Count = int(i[1])
			greatest_Decrease = f"{i[0]} (${greatest_decrease_Count})"


# Preparing Lines for Txt File

txt_lines = ["", "Financial Analysis", "",
			"--------------------------------------", "",
			f"Total Months: {total_Month}", "",
			f"Total: ${total_net}", "",
			f"Average Change: ${avg_Change}", "",
			f"Greatest Increase in Profits: {greatest_Increase}", "",
			f"Greatest Decrease in Profits: {greatest_Decrease}", ""]

# Open and write the Output Txt File with line comprehension

with open(txt_output, "w") as txt_file:

	txt_file.writelines([line + "\n" for line in txt_lines])