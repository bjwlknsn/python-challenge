import os
import csv

candidates = []
votes_per_candidate = []
percent_votes = []
total_votes=[]
total_votes = 0

election_data = os.path.join("Resources", "election_data.csv")

with open(election_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv_reader:
        total_votes += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            votes_per_candidate.append(1)
        else:
            index = candidates.index(row[2])
            votes_per_candidate[index] += 1
    
    for votes in votes_per_candidate:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    winner = max(votes_per_candidate)
    index = votes_per_candidate.index(winner)
    winning_candidate = candidates[index]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percent_votes[i]} ({votes_per_candidate[i]})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")
        

election_file = os.path.join("analysis", "election_results.txt")

with open(election_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for i in range(len(candidates)):
        outfile.write(f"{candidates[i]}: {percent_votes[i]} ({votes_per_candidate[i]})\n")    
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winning_candidate}\n")
    outfile.write("-------------------------\n")