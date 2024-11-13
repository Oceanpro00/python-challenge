# Importing the Dependencies

import os
import csv

# File Path Designations for CSV Input and TXT Output

csv_input = os.path.join("Resources", "budget_data.csv")
txt_output = os.path.join("analysis", "PyBank Analysis.txt")

# Defining Variables for Data Measurements

total_Month = 0
total_net = 0
change = 0
greatest_Increase = 0
greatest_Decrease = 0 