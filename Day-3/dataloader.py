import logging


logging.basicConfig(
    filename='errors.log',  # File where logs will be saved
    level=logging.ERROR,    # Only log errors (ignore warnings/info)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Timestamp + error message
)

try:
    with open("nonexistent_file.csv", "r") as file:
        data = file.read()
except FileNotFoundError as e:
    logging.error(f"File not found: {e}", exc_info=True)  # Logs the full error traceback

#task 1: save your data.
ages = [25,42, "Unknown", 28,90,88,"",69]

with open("data.txt", "w") as file:
    for age in ages:
        file.write(f"{age}\n")

#this task 1 loads data and saves it in to a file called data.txt.

#task 2
#lets validate age and insert 

valid_ages = []  #we will add only valid ages in this list

#lets load a data file
with open("data.txt", "r") as file:
    for line in file:
        line = line.strip()
        try:
            valid_ages.append(int(line))
        except (ValueError, TypeError):
            logging.error(print(f"Invalid entry: {line}"))
            
#task 3: Generate Report
report = f""" 
CLEANED DATA REPORT
====================
Valid Entry = {len(valid_ages)}
Min age = {min(valid_ages)}
Max age = {max(valid_ages)}
Invalid or skipped ages = {len(ages) - len(valid_ages)}
"""
print(report)