import os
import csv

budget_data_csv = os.path.join('..', 'Pybank', 'Resources', 'budget_data.csv')  # Specify path to collect budget_data.csv file from Resources folder of Pybank

months = []                                                                     # Create 'month' list to store the months 
profit_loss = []                                                                # Create 'profit_loss' list to store the profits/losses values
change_profit_loss = []                                                         # Create 'change_profit_loss' list to store difference of profit/loss values between months

with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')                          # Read csv without the header row, split the data by commas
    total_months = int(len(list(csvreader)))                                    # Calculate the total number of months in the csv file

with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")                          # Read csv without the header row, split the data by commas
    for row in csvreader:                                                       # Use 'for loops' to go through rows to add values into the list
        months.append(row['Date'])                                              # Add each month to 'months' list
        profit_loss.append(int(row['Profit/Losses']))                           # Add each profit/loss value to 'profit_loss' list

total_profit_loss = sum(profit_loss)                                            # Calculate the sum of profit/lost value in 'profit_loss' list

with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")                          # Read csv without the header row, split the data by commas
    for i in range(total_months):                                               # Use 'for loops' to go through values in 'profit_loss' list with range from i to total number of months
        change = profit_loss[i]-profit_loss[i-1]                                # Calculate the difference between the ocurrent row's value to previous row's value
        change_profit_loss.append(int(change))                                  # Add each difference value 'change' to 'change_profit_loss' list

total_change = sum(change_profit_loss) - change_profit_loss[0]                  # Calculate the total sum of change, removing the first row value since the counting starts at first row
average_change = round((total_change/(total_months-1)) ,2)                      # Calculate the average change by this formula (total change/total # of months); one less since the first row has no value. cannot assign 0 as there is no previous "month" to calculate the change

greatest_increase = max(change_profit_loss)                                     # Find the greatest increase in change of profits in the 'change_profit_loss' list
increase_index = change_profit_loss.index(greatest_increase)                    # Find the index of the greatest increase in change of profits
increase_month = months[increase_index]                                         # Find the month of the matching index in the 'month' list

greatest_decrease = min(change_profit_loss)                                     # Find the greatest decrease in change of profits in the 'change_profit_loss' list
decrease_index = change_profit_loss.index(greatest_decrease)                    # Find the index of the greatest decrease in change of profits
decrease_month = months[decrease_index]                                         # Find the month of the matching index in the 'month' list

print(f'Financial Analysis' + "\n")                                             # Print results, "\n" to add spaces                                                                       
print(f'-------------------------------' + "\n")                                                                
print(f'Total Months: {total_months}' + "\n")                                                                  
print(f'Total: $ {total_profit_loss}' + "\n")                                                                  
print(f'Average Change: ${average_change}' + "\n")                                                                                                                     
print(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})' + "\n")
print(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})' + "\n")

bd_txt = os.path.join('..', 'PyBank', 'analysis', 'budget_data.txt')            # Print results into a new textfile in the analysis folder under PyBank Folder

with open(bd_txt, 'w') as txt:
    txt.write(f'Financial Analysis' + "\n" + "\n")                                                                         
    txt.write(f'-------------------------------' + "\n" + "\n")                                                               
    txt.write(f'Total Months: {total_months}' + "\n" + "\n")                                                                  
    txt.write(f'Total: $ {total_profit_loss}' + "\n" + "\n")                                                                   
    txt.write(f'Average Change: ${average_change}' + "\n" + "\n")                                                                                                                     
    txt.write(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})' + "\n"+ "\n") 
    txt.write(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')