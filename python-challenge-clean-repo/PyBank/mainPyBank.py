# Define the file path
file_path = 'C:/Users/debra/Documents/python-challenge-clean-repo/PyBank/Resources/budget_data.csv'

# Read the csv file and parse the data
with open(file_path, 'r') as file:
    # Read the header
    header = file.readline().strip().split(',')
    
    # Initialize variables
    total_months = 0
    total_profit_losses = 0
    changes = []
    greatest_increase = None
    greatest_decrease = None
    
    # Process each line
    for line in file:
        row = line.strip().split(',')
        
        # Update total months and total profit/losses
        total_months += 1
        total_profit_losses += int(row[1])
        
        # Calculate change and keep track of greatest increase and decrease
        if total_months > 1:
            change = int(row[1]) - prev_profit_losses
            changes.append(change)
            
            if greatest_increase is None or change > greatest_increase[1]:
                greatest_increase = (row[0], change)
            if greatest_decrease is None or change < greatest_decrease[1]:
                greatest_decrease = (row[0], change)
        
        prev_profit_losses = int(row[1])

# Calculate the average change
average_changes = sum(changes) / len(changes)

# Display the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_changes:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,.0f})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,.0f})")

# Export a text file with the results
with open('financial_analysis.txt', "w") as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${total_profit_losses}\n")
    f.write(f"Average Change: ${average_changes:.2f}\n")
    f.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,.0f})\n")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,.0f})\n")