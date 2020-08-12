import os
import csv


#Path for CSV file
csvpath = os.path.join("Resources","PyPolldata.csv")

#Declare dictionary for the CSV data
candidate_dictionary = {}

# Read csv data and add it to the dictionary
with open(csvpath,"r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for row in csv_reader:
        candidate = row[2]
        if candidate in candidate_dictionary:
            candidate_dictionary[candidate] = candidate_dictionary[candidate] + 1
        else:
            candidate_dictionary[candidate] = 1

# Calculate the total number of votes cast
total_votes = sum(candidate_dictionary.values())

# Percentage of votes each candidate's won
khan_percentage_votes =(candidate_dictionary['Khan'])/ (total_votes) * 100
correy_percentage_votes = candidate_dictionary['Correy'] / total_votes * 100
li_percentage_votes = candidate_dictionary['Li'] / total_votes * 100
otooley_percentage_votes = candidate_dictionary["O'Tooley"] / total_votes * 100

# Total number of votes each candidate won
khan_total_votes = candidate_dictionary['Khan']
correy_total_votes = candidate_dictionary['Correy']
li_total_votes = candidate_dictionary['Li']
otooley_total_votes = candidate_dictionary["O'Tooley"]

# Finding winner of the election 
winner = ""

if khan_total_votes > correy_total_votes and khan_total_votes > li_total_votes and khan_total_votes > otooley_total_votes:
    winner = "Khan"
elif correy_total_votes > khan_total_votes and correy_total_votes > li_total_votes and correy_total_votes > otooley_total_votes:
        winner = "Correy"
elif li_total_votes > correy_total_votes and li_total_votes > khan_total_votes and li_total_votes > otooley_total_votes:
        winner = "Li"
else:
    winner = "O'Tooley"

#Print output to terminal
print("Election Results")
print("---------------------")
print(f'Total Votes: {total_votes}')
print("---------------------")
print(f'Khan: {khan_percentage_votes}% ({khan_total_votes})')
print(f'Correy: {correy_percentage_votes}% ({correy_total_votes})')
print(f'Li: {li_percentage_votes}% ({li_total_votes})')
print(f"O'Tooley: {otooley_percentage_votes}% ({otooley_total_votes})")
print("---------------------")
print(f'Winner: {winner}')
print("---------------------")

#Write output to file
file=open("output.txt","w")
file.write("Election Results" + "\n")
file.write("-----------------------------------------------------------------" +"\n")
file.write("Khan:" +str(khan_percentage_votes)  +"%" +" " +str(khan_total_votes) +"\n")
file.write("Correy : " +str(correy_percentage_votes) +"%" +" " +str(correy_total_votes) +"\n")
file.write("Li: " +str(li_percentage_votes) +"%" +" " +str(li_total_votes) +"\n")
file.write("O'Tooley:"  +str(otooley_percentage_votes)  +"%" +" " +str(otooley_total_votes) +"\n")
file.write("---------------------")
file.write("Winner: " +winner)
file.write("---------------------")
