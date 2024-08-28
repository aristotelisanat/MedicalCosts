medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
# 1. Print the original medical data
print("Original Medical Data:")
print(medical_data)
print()

# 2. Replace # with $ and store in updated_medical_data
updated_medical_data = medical_data.replace("#", "$")
print("Updated Medical Data:")
print(updated_medical_data)
print()

# 3-5. Count the number of medical records
num_records = updated_medical_data.count("$")
print(f"There are {num_records} medical records in the data.")
print()

# 6-7. Split the data into a list of records
medical_data_split = updated_medical_data.split(";")
print("Split Medical Data:")
print(medical_data_split)
print()

# 8-11. Clean up the data
medical_records = []
for record in medical_data_split:
    medical_records.append(record.split(","))

medical_records_clean = []
for record in medical_records:
    record_clean = []
    for item in record:
        record_clean.append(item.strip())
    medical_records_clean.append(record_clean)

print("Cleaned Medical Records:")
print(medical_records_clean)
print()

# 12-13. Print names in uppercase
print("Names (in uppercase):")
for record in medical_records_clean:
    print(record[0].upper())
print()

# 14-18. Separate data into individual lists
names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insurance_costs.append(record[3])

print("Separated Data:")
print("Names:", names)
print("Ages:", ages)
print("BMIs:", bmis)
print("Insurance Costs:", insurance_costs)
print()

# 19-22. Calculate average BMI
total_bmi = 0
for bmi in bmis:
    total_bmi += float(bmi)

average_bmi = total_bmi / len(bmis)
print(f"Average BMI: {average_bmi:.2f}")

# Extra tasks
# 1. Calculate average insurance cost
total_insurance_cost = 0
for cost in insurance_costs:
    total_insurance_cost += float(cost.replace("$", ""))

average_insurance_cost = total_insurance_cost / len(insurance_costs)
print(f"Average Insurance Cost: ${average_insurance_cost:.2f}")

# 2. Output formatted string for each individual
print("\nIndividual Summaries:")
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old with a BMI of {bmis[i]} and an insurance cost of {insurance_costs[i]}.")
