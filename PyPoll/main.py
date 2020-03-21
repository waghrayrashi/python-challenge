import os
import csv
votes=[]
candidate= ""
winner = ""
candidate_votes={}
candidate_percent_votes={}


# Import input csv file
input_csv_filepath = os.path.join('election_data.csv')
# Open csv file
with open (input_csv_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Skip header row
    next(csvreader)
        
    # Calculate total months
    total_votes=0
    winner_votes=0

    # Convert reader string into a list votes
    for line in csvreader:
        votes.append(line)

        # Calculate the total votes 
        total_votes = total_votes + 1
        candidate = line[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1
# Calculate percentage of votes and identify the winner
for person, vote_count in candidate_votes.items():
    candidate_percent_votes[person] = '{0:.0%}'.format(vote_count/total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

        # Print Summary
print("Election Results")
print("------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------")
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percent_votes[person]}, ({vote_count})")
print("------------------------------------")
print(f"Winner: {winner}")
print("------------------------------------")

# Write output to txt file ElectionResults.txt
# Define path for output text file
output_txt_filepath = os.path.join('ElectionResults.txt')

# Open the output file to begin writing the summary into it
text_file=open(output_txt_filepath, 'w')

# write the summary to the text file
text_file.write("Election Results")
text_file.write("\n----------------------------------")
text_file.write('\nTotal Votes: '+ str(total_votes))
text_file.write('\n----------------------------------')
for person, vote_count in candidate_votes.items():
    text_file.write(f'\n{person}: {candidate_percent_votes[person]} ({vote_count})')
text_file.write('\n------------------------------------')
text_file.write(f"\nWinner: {winner}")
text_file.write('\n------------------------------------')
text_file.close()

