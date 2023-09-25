# Define the file path for the csv
file_path = 'C:/Users/debra/Documents/python-challenge-clean-repo/PyPoll/Resources/election_data.csv'

# Read the csv file and store the data in a list of dictionaries
with open(file_path, 'r') as file:
    lines = file.readlines()
    header = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]

# Calculate the total number of votes
total_votes = len(data)

# Find the different candidates
candidates = set(row[2] for row in data)

# Calculate the number of votes for each candidate
votes_per_candidate = {candidate: sum(1 for row in data if row[2] == candidate) for candidate in candidates}

# Calculate the percentage of votes for each candidate
percentage_per_candidate = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_per_candidate.items()}

# Determine the candidate with the most votes
winning_candidate = max(votes_per_candidate, key=votes_per_candidate.get)

# Print results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates:
    print(f"{candidate}: {percentage_per_candidate[candidate]:.3f}% ({votes_per_candidate[candidate]})")

print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

# Write results to a text file
with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")

    for candidate in candidates:
        txtfile.write(f"{candidate}: {percentage_per_candidate[candidate]: .3f}% ({votes_per_candidate[candidate]})\n")
    
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winning_candidate}\n")
    txtfile.write("-------------------------\n")
