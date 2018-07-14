import os
import csv

pypoll_file_path = os.path.join("Resources","election_data.csv")
candidateList = []

with open(pypoll_file_path) as pypollFile:

    pypollCsvReader = csv.DictReader(pypollFile,delimiter = ",")

    for row in pypollCsvReader:
        candidateList.append(row['Candidate'])
    
    print("\nElection Results")
    print("-----------------------")
    print(f"Total Votes: {len(candidateList)}")
    print("-----------------------")

    candidateSet = set(candidateList)
    candidateCountDictionary = {}

    for candidate in candidateSet:
        print (f"{candidate}: {round(candidateList.count(candidate)/len(candidateList)*100,2)}% ({candidateList.count(candidate)})")
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