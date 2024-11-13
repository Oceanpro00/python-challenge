# Importing all dependencies

import os
import csv

# File Path Designation for Inpout Csv file and Output Txt file

csv_input = os.path.join("Resources", "election_data.csv")
txt_output = os.path.join("analysis", "PyPoll_Analysis.txt")

# Defining required Variable for Data Measurements

total_Votes = 0
candidates = []
unique_candidates = []
votes_count = 0
votes_counted = []
percentage_voted = []
txt_lines_2 = []

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

	unique_candidates = list(set(candidates))

	# a For loop to go through each candidate listed

	for x in unique_candidates:
	
		# a For loop to go through and calculate the number of votes per candidate

		for i in candidates:
			if i == x:
				votes_count += 1

		# votes_count = [votes_count += 1 for i in candidates if i == x]

		# Define the votes per Candidate

		votes_counted.append(votes_count)

		# Calculate and Define the percentage voted per Candidate and reset vote counter for next Candidate

		percentage_voted.append(round(((votes_count/total_Votes)*100),3))
		votes_count = 0
	

# Preparing Executable Text Lines for Analysis

txt_lines_1 = ["Election Results", "",
            "--------------------------------------", "",
            f"Total Votes: {total_Votes}", "",
            "--------------------------------------", "",]

for i in range(len(unique_candidates)):
    txt_lines_2.append(f"{unique_candidates[i]}: {percentage_voted[i]}% ({votes_counted[i]})")

txt_lines_3 = ["--------------------------------------", "",
            "Winner :"]

# new function to print and add line breaks

def execute_Print(x):

	for line in x:
		print(line)
	print("") 



# Terminal Print Out - ( print("") are for legibility )

execute_Print(txt_lines_1)
execute_Print(txt_lines_2)
execute_Print(txt_lines_3)