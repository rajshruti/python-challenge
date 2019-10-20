import os
import csv

# Intialize the variables
count = 0
total_profit_loss = 0
profit_loss_change = 0
total_profit_loss_change = 0
profit_loss_previous = 0
greatest_incr = 0
greatest_decr = 0
changes=[]

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        # Calculate total number of months included in the dataset
        count = count+1
        
        # Calculate total amount of "Profit/Losses" over the entire period
        total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
        
        # Calculate profit/loss changes for each month
        profit_loss_current=int(row["Profit/Losses"])
        if profit_loss_previous!=0:
            profit_loss_change = profit_loss_current-profit_loss_previous
            date=row["Date"]
               
            # Calculate greatest increase and decrease in profits (date and amount) over the entire period
            if profit_loss_change>=greatest_incr:
                greatest_incr=profit_loss_change
                incr_date=date
            elif profit_loss_change<=greatest_decr:
                greatest_decr=profit_loss_change
                decr_date=date
                
        # populate profit/loss changes in list
        changes.append(profit_loss_change)
                
        profit_loss_previous=int(row["Profit/Losses"])
        
    # Calculate average of the changes in "Profit/Losses" over the entire period    
    for row in changes:  
        total_profit_loss_change= total_profit_loss_change + row
           
    avg_profit_loss= total_profit_loss_change/(count-1)
        
# Print the financial analysis to the terminal
print ('''Financial Analysis
----------------------------''')
print(f'Total Months: {count}')
print(f'Total: ${total_profit_loss}')
print (f'Average Change: ${("%.2f" % avg_profit_loss)}')
print(f'Greatest Increase in Profits: {incr_date} ($ {greatest_incr} )')
print(f'Greatest Decrease in Profits: {decr_date} (${greatest_decr} )')
    
output_path = os.path.join('Resources', 'financial analysis.txt')

# Write the results of financial analysis into a text file 
with open(output_path, 'w') as text_file:
    
    text_file.write('''Financial Analysis
----------------------------\n''')
    text_file.write(f'Total: ${total_profit_loss}\n')
    text_file.write (f'Average Change: ${("%.2f" % avg_profit_loss)}\n')
    text_file.write(f'Greatest Increase in Profits: {incr_date} ($ {greatest_incr} )\n')
    text_file.write(f'Greatest Decrease in Profits: {decr_date} (${greatest_decr} )\n')
    text_file.close()
