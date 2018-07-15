#Importing os and csv modules to read/write file data 
import os
import csv

#Defining variables
netProfit = 0
revenue = 0
revenueDifference = []
listOfMonths = []

#Setting the input file path
pybank_file_path = os.path.join("Resources","budget_data.csv")

with open(pybank_file_path,'r') as pybankFile:

    #Reading the input csv file
    pybankCsvReader = csv.reader(pybankFile,delimiter = ",")
    #Excluding Header row
    pybankCsvHeader = next(pybankCsvReader)

    for pybankRow in pybankCsvReader:
        #Adding total profit
        netProfit += int(pybankRow[1])

        #Adding each month to the list
        listOfMonths.append(pybankRow[0])

        # calculate difference in profit/loss between 2 subsequent months
        # check below is to skip the first month and start calculating from second month onwards
        if revenue != 0:
            revenueDifference.append(int(pybankRow[1]) - revenue)
        
        #setting revenue for current row to be used for next "for" iteration to calculate the difference
        revenue = int(pybankRow[1])
    
    print ("\nFinancial Analysis")
    print ("-----------------------------------------")
    print (f"Total Months: {len(listOfMonths)}")
    print (f"Total: ${netProfit}")
    print (f"Average Change : ${sum(revenueDifference)/ len(revenueDifference)}")
    print (f"Greatest Increase in Profits: {listOfMonths[revenueDifference.index(max(revenueDifference)) + 1]} (${max(revenueDifference)})")
    print (f"Greatest Decrease in Profits: {listOfMonths[revenueDifference.index(min(revenueDifference)) + 1]} (${min(revenueDifference)})")

    #Writing output to the text file
    with open("Output.txt", "w") as text_file:
        print ("\nFinancial Analysis", file=text_file)
        print ("-----------------------------------------",file=text_file)
        print (f"Total Months: {len(listOfMonths)}",file=text_file)
        print (f"Total: ${netProfit}",file=text_file)
        print (f"Average Change : ${sum(revenueDifference)/ len(revenueDifference)}",file=text_file)
        print (f"Greatest Increase in Profits: {listOfMonths[revenueDifference.index(max(revenueDifference)) + 1]} (${max(revenueDifference)})",file=text_file)
        print (f"Greatest Decrease in Profits: {listOfMonths[revenueDifference.index(min(revenueDifference)) + 1]} (${min(revenueDifference)})",file=text_file)
    
    print (f"\nAnalysis written successfully into output.txt file as well!")