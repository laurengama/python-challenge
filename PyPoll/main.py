# First we'll import the os module
import os

# Module for reading CSV files
import csv

pypoll_csv = os.path.join('election_data.csv')

# Create dictionary to store data
candidate_name = {}

# Read in the CSV file
with open(pypoll_csv, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        name = row[2]
        # Add names to dictionary
        if name in candidate_name:
            candidate_name[name] += 1
        else:
            candidate_name[name] = 1

#print(candidate_name)


#The total number of votes cast
total_votes = sum(candidate_name.values())
#print(total_votes)


#A complete list of candidates who received votes
list_names = []
for name in candidate_name.keys():
    list_names.append(name)

#print(list_names)


#The percentage of votes each candidate won
vote_percent = []
for votes in candidate_name.values():
    vote_percent.append(round((votes / total_votes * 100), 2))

#print(vote_percent)


#The total number of votes each candidate won
list_votes = []
for votes in candidate_name.values():
    list_votes.append(votes)

#print(list_votes)


#The winner of the election based on popular vote.
max_value = max(candidate_name.values())
max_keys = [name for name, v in candidate_name.items() if v == max_value]
#print(max_keys, max_value)




print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"{list_names[0]}: {vote_percent[0]}% ({list_votes[0]})")
print(f"{list_names[1]}: {vote_percent[1]}% ({list_votes[1]})")
print(f"{list_names[2]}: {vote_percent[2]}% ({list_votes[2]})")
print(f"{list_names[3]}: {vote_percent[3]}% ({list_votes[3]})")
print(f"----------------------------")
print(f"Winner: {max_keys[0]}")
print(f"----------------------------")


with open("PyPoll.txt","w", newline="") as file:
    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"----------------------------\n")
    file.write(f"{list_names[0]}: {vote_percent[0]}% ({list_votes[0]})\n")
    file.write(f"{list_names[1]}: {vote_percent[1]}% ({list_votes[1]})\n")
    file.write(f"{list_names[2]}: {vote_percent[2]}% ({list_votes[2]})\n")
    file.write(f"{list_names[3]}: {vote_percent[3]}% ({list_votes[3]})\n")
    file.write(f"----------------------------\n")
    file.write(f"Winner: {max_keys[0]}\n")
    file.write(f"----------------------------\n")