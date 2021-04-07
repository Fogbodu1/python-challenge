import os
import csv

electiondata = os.path.join(".", "Resources", "election_data.csv")

#set the output of the text file
#text_path = "output.txt"

#Empty Lists of data.
votes = []
total_votes = []
candidate_dict = {}
Khan_percentage = []

# Use encoding for Windows
# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
with open(electiondata, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #lines = list(csvreader)
    next(csvreader)
    total_votes = 0
    vote_count = 0
    most_vote = 0

    for row in csvreader:
#The total number of votes cast
        votes.append(str(row[1]))
        total_votes = len(votes)

#Count each number of candidates in the candidates list
        vote_count += 1
        candidate_dict[row[2]] = candidate_dict.get(row[2], 0) + 1
        vote = candidate_dict

#The total number of votes and the percentage of votes each candidate won.
#For Khan
for i in candidate_dict.items():
       i =  candidate_dict["Khan"] 
       Khan_percentage = round((i/vote_count) * 100)
#For Correy
for x in candidate_dict.items():
       x =  candidate_dict["Correy"] 
       Correy_percentage = round((x/vote_count) * 100)
#For Li
for y in candidate_dict.items():
       y =  candidate_dict["Li"] 
       Li_percentage = round((y/vote_count) * 100)
#For O'Tooley
for z in candidate_dict.items():
       z =  candidate_dict["O'Tooley"] 
       O_Tooley_percentage = round((z/vote_count) * 100)

#The winner of the election based on popular vote.
if i > x > y > z:
       Winner = "Khan"
elif x > i > y > z:
       Winner = "Correy"
elif y > i > x > z:
       Winner = "Li"
elif z > i > x > y:
       Winner = "O'Tooley"

#write changes to csv
#with open(text_path, 'w') as file:
print("Election Results")
print("--------------------------")
print(f'Total Votes: {total_votes}')
print("--------------------------")
#print(f'Khan: ({Khan_percentage}.000%) {x}')
print(f'Khan: {Khan_percentage}.000% ({i})')
print(f'Correy: {Correy_percentage}.000% ({x})')
print(f'Li: {Li_percentage}.000% ({y})')
print(f"O'Tooley: {O_Tooley_percentage}.000% ({z})")
print("--------------------------")
print(f"Winner: {Winner}")
print(f'----------------------------')

# Set variable for output file
output_file = os.path.join(".", "analysis","election_data_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Election Results"])
    writer.writerow(["--------------------------"])
    datafile.write("Total Votes: "+ str(total_votes)+"\n")
    writer.writerow(["--------------------------"])
    datafile.write("Khan: "+ str(Khan_percentage)+".000% ("+str(i)+")\n")
    datafile.write("Correy: "+ str(Correy_percentage)+".000% ("+str(x)+")\n")
    datafile.write("Li: "+ str(Li_percentage)+".000% ("+str(y)+")\n")
    datafile.write("O'Tooley: "+ str(O_Tooley_percentage)+".000% ("+str(z)+")\n")
    writer.writerow(["--------------------------"])
    datafile.write("Winner: "+ str(Winner)+"\n")
    writer.writerow(["--------------------------"])