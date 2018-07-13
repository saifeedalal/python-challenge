import os
import csv

netProfit = 0
revenue = 0
revenueDifference = []
listOfMonths = []

pybank_file_path = os.path.join("Resources","budget_data.csv")

with open(pybank_file_path,'r') as pybankFile:

    pybankCsvReader = csv.reader(pybankFile,delimiter = ",")
    pybankCsvHeader = next(pybankCsvReader)

    for pybankRow in pybankCsvReader:
        netProfit += int(pybankRow[1])
        listOfMonths.append(pybankRow[0])

        if revenue != 0:
            revenueDifference.append(int(pybankRow[1]) - revenue)
        
        revenue = int(pybankRow[1])
    
    print ("\nFinancial Analysis")
    print ("-----------------------------------------")
    print (f"Total Months: {len(listOfMonths)}")
    print (f"Total: ${netProfit}")
    print (f"Average Change : ${sum(revenueDifference)/ len(revenueDifference)}")
    print (f"Greatest Increase in Profits: {listOfMonths[revenueDifference.index(max(revenueDifference)) + 1]} (${max(revenueDifference)})")
    print (f"Greatest Decrease in Profits: {listOfMonths[revenueDifference.index(min(revenueDifference)) + 1]} (${min(revenueDifference)})")

    with open("Output.txt", "w") as text_file:
        print ("\nFinancial Analysis", file=text_file)
        print ("-----------------------------------------",file=text_file)
        print (f"Total Months: {len(listOfMonths)}",file=text_file)
        print (f"Total: ${netProfit}",file=text_file)
        print (f"Average Change : ${sum(revenueDifference)/ len(revenueDifference)}",file=text_file)
        print (f"Greatest Increase in Profits: {listOfMonths[revenueDifference.index(max(revenueDifference)) + 1]} (${max(revenueDifference)})",file=text_file)
        print (f"Greatest Decrease in Profits: {listOfMonths[revenueDifference.index(min(revenueDifference)) + 1]} (${min(revenueDifference)})",file=text_file)
    
    print (f"\nAnalysis written successfully into output.txt file as well!")