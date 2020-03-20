import os
import csv
profit_loss=[]
pl_summary={}
# Import input csv file
input_csv_filepath = os.path.join('budget.csv')

with open (input_csv_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Skip header row
    next(csvreader)
        
    # Calculate total months
    total_months=0
    total=0
    
    # Convert reader string to a list profit_loss
    for line in csvreader:
        profit_loss.append(line)
                
        # Calculate the Total net amount of Profit/Losses over the entire period
        total=total + float(line[1])
        # Calculate total number of months
        total_months=total_months + 1
    # Print summary
    print("\nFinancial Analysis", "\n" + "-" * 50)
    print(f"Total Months: {total_months}")
    print (f"Total: ${total}")
    
    MoM_change=0
    MoM_total=0
    MoM_avg=0
# As we are at the last line now, we must compute change in PL between months over the entire period 
# by iterating backwards from latest month-year to teh earliest month-year
    
    # Initialize variable for Greatest increase with the latest increase value
    max_increase=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])

    # Initialize variables for Greatest decrease with the latest decrease value
    max_decrease=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])

    # Calculate Total Profits and Losses
    for i in range(total_months,1,-1): # i stops at 2 because we dont want to check header row
        MoM_change=int(profit_loss[i-1][1]) - int(profit_loss[i-2][1]) 
        if MoM_change < max_decrease:
            min_month=profit_loss[i-1][0]
            max_decrease=MoM_change
        elif MoM_change > max_increase:
            max_month=profit_loss[i-1][0]
            max_increase=MoM_change
        #Calculate total change in PL between months over the entire period
        MoM_total=MoM_total+MoM_change
    # Calculate the average change in PL between months over the entire period
    MoM_avg=round(MoM_total/(total_months-1),2)
    print(f"Average Change: ${MoM_avg}")
    print(f"Greatest Increase in Profits: {max_month} (${max_increase})")
    print(f"Greatest Decrease in Profits: {min_month} (${max_decrease})")

# Define path for output text file
output_txt_filepath = os.path.join('FinancialSummary.txt')

# Open the output file to begin writing the summary into it
text_file=open(output_txt_filepath, 'w')

# write the summary to the text file
text_file.write("Financial Analysis")
text_file.write('\n')
text_file.write("------------------------------------------")

text_file.write('\nTotal Months: '+str(total_months))
text_file.write('\nTotal: $'+str(total))
text_file.write('\nAverage  Change: $'+str(round(MoM_avg,2)))
text_file.write('\nGreatest Increase in Profits: ' + max_month + ' ($'+str(max_increase) + ')')
text_file.write('\nGreatest Decrease in Profits: ' + min_month + ' ($'+str(max_decrease) + ')')
text_file.close()