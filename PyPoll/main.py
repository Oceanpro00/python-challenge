# Importing all dependencies

import os
import csv

# File Path Designation for Inpout Csv file and Output Txt file

csv_input = os.path.join("Resources", "election_data.csv")
txt_output = os.path.join("analysis", "PyPoll_Analysis.txt")

# Defining required Variable for Data Measurements

total_Votes = 0
candidates = []
votes_counted = []
percentage_voted = []
total_Votes_Candidates = []
result = {}

# Open and read the Input Csv file

with open (csv_input, encoding="UTF-8") as csv_data:

	read = csv.reader(csv_data, delimiter=",")

	# skip and store header

	header = next(read)

	# a For loop to go through all rows in the CSV

	for i in read:

		# total vote counter

		total_Votes += 1

		# Candidates list creator

		candidates.append(i[2])

	# List all Unique Candidates

	candidates = list(set(candidates))

	# a For loop to go through each candidate listed

	# for cand in candidates:


	# 	# votes_counted.append([len(i) for i in read if i[2] == cand])

	# 	result[cand] = votes_counted

# print(result)

print(f"{total_Votes} total votes among these candidates : {candidates} and the result is {result}")
