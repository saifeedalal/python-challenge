#Importing os and csv modules to read/write file data 
import os
import csv

#Setting the input file path
pypoll_file_path = os.path.join("Resources","election_data.csv")

candidateList = []

with open(pypoll_file_path) as pypollFile:

    pypollCsvReader = csv.DictReader(pypollFile,delimiter = ",")

    #Adding all candidate entires into the candidateList
    for row in pypollCsvReader:
        candidateList.append(row['Candidate'])
    
    print("\nElection Results")
    print("-----------------------")
    print(f"Total Votes: {len(candidateList)}")
    print("-----------------------")

    #Creating a set of unique Candidates
    candidateSet = set(candidateList)
    candidateCountDictionary = {}

    for candidate in candidateSet:
        print (f"{candidate}: {round(candidateList.count(candidate)/len(candidateList)*100,2)}% ({candidateList.count(candidate)})")
        #Adding count of votes for each unique candidate into a dictionary
        candidateCountDictionary[candidateList.count(candidate)] = candidate

    print("-----------------------")
    print(f"Winner: {candidateCountDictionary.get(max(candidateCountDictionary.keys()))}")
    print("-----------------------")

    with open("Output.txt", "w") as text_file:
        print("\nElection Results",file=text_file)
        print("-----------------------",file=text_file)
        print(f"Total Votes: {len(candidateList)}",file=text_file)
        print("-----------------------",file=text_file)
        for candidate in candidateSet:
            print (f"{candidate}: {round(candidateList.count(candidate)/len(candidateList)*100,2)}% ({candidateList.count(candidate)})",file=text_file)
        print("-----------------------",file=text_file)
        print(f"Winner: {candidateCountDictionary.get(max(candidateCountDictionary.keys()))}",file=text_file)
        print("-----------------------",file=text_file)

    
    print (f"\nAnalysis written successfully into output.txt file as well!")