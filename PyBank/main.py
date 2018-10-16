# First we'll import the os module
import os

# Module for reading CSV files
import csv

pybank_csv = os.path.join('budget_data.csv')


# Lists to store data
total_months_list = []
net_profit_list = []


# Read in the CSV file
with open(pybank_csv, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        # Add months
        total_months_list.append(row[0])
        # Add profits/losses
        net_profit_list.append(int(row[1]))




#create variable to store total number of months included in the dataset
total_months = len(total_months_list)

#create variable to store total net amount of "Profit/Losses" over the entire period
net_profit = sum(net_profit_list)



#create list to store monthly change in "Profit/Losses" over the entire period
monthly_change_list = [net_profit_list[i+1]-net_profit_list[i] for i in range(len(net_profit_list)-1)]


#find average change in "Profit/Losses" between months over the entire period
def average(monthly_change_list):
    length = len(monthly_change_list)
    total = 0.0
    for number in monthly_change_list:
        total += number
    return total / length



#create variable to store ave monthly change
monthly_change = round((average(monthly_change_list)), 2)


#create variable to store greatest increase in profits
great_inc = max(net_profit_list)

#create variable to store index of greatest increase in profits
inc_index = net_profit_list.index(great_inc)

#use index to find date
great_inc_date = total_months_list[inc_index]


#create variable to store greatest decrease in losses
great_dec = min(net_profit_list)

#create variable to store index of greatest decrease in losses
dec_index = net_profit_list.index(great_dec)

#use index to find date
great_dec_date = total_months_list[dec_index]


print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average  Change: ${monthly_change}")
print(f"Greatest Increase in Profits: {great_inc_date} (${great_inc})")
print(f"Greatest Decrease in Profits: {great_dec_date} (${great_dec})")

with open("PyBank.txt","w", newline="") as file:
    file.write(f"Financial Analysis\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_profit}\n")
    file.write(f"Average  Change: ${monthly_change}\n")
    file.write(f"Greatest Increase in Profits: {great_inc_date} (${great_inc})\n")
    file.write(f"Greatest Decrease in Profits: {great_dec_date} (${great_dec})")
