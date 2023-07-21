import os
import csv


# Gotta collect the Data
poll_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Rock down to Variable Avenue


totccs = 0
totddg = 0
totrad = 0
ccsperc = 0
ddgperc = 0
radperc = 0
ccsperc2 = 0
ddgperc2 = 0
radperc2 = 0
candilist = []
totvot = []

#Reading the data
with open(poll_csv, encoding="utf_8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csv_reader)

    for row in csv_reader:
        totvot.append((row[0]))
        candilist.append((row[2]))
#Tally the votes
    totccs = candilist.count("Charles Casper Stockham")
    totddg = candilist.count("Diana DeGette")
    totrad = candilist.count("Raymon Anthony Doane")

#Total Votes
totvot = (totccs + totddg + totrad)
#Getting and rounding percentages
ccsperc = (totccs/totvot) * 100 
ddgperc = (totddg/totvot) * 100
radperc = (totrad/totvot) * 100
ccsperc2 = round(ccsperc,3)
ddgperc2 = round(ddgperc,3)
radperc2 = round(radperc,3)

#Declare the winner!
if totccs > totddg and totccs > totrad:
    winner = str("Charles C Stockham")
if totddg > totccs and totddg > totrad:
    winner = str("Diana DeGette")
if totrad > totccs and totrad > totddg:
    winner = str("Raymon Anthony Doane")


#print it all out and put it in a file
print("ELECTION RESULTS")
print("-------------------------------------------------------------")

print ("Total Votes    :" + str(totvot))        
print ("------------------------------------------------------------")
print( "Charles C Stockham:   " + str(ccsperc2) + "%" + "(" + str(totccs) + ")")
print( "Diana DeGette:        " + str(ddgperc2) + "%" + "(" + str(totddg) + ")")
print( "Raymon Anthony Doane  " + str(radperc2) + "%" + "(" + str(totrad) + ")")
print("--------------------------------------------------------------")
print("WINNER!!   " + str(winner))

with open('Election_Results.txt', 'w') as f:
    f.write("ELECTION RESULTS")
    f.write('\n' "--------------------------------------------------------")
    f.write('\n' "Total Votes    :" + str(totvot))  
    f.write('\n' "--------------------------------------------------------")
    f.write('\n' "Charles C Stockham:   " + str(ccsperc2) + "%" + "(" + str(totccs) + ")")
    f.write('\n' "Diana DeGette:        " + str(ddgperc2) + "%" + "(" + str(totddg) + ")")
    f.write('\n' "Raymon A Doane:       " + str(radperc2) + "%" + "(" + str(totrad) + ")")
    f.write('\n' "--------------------------------------------------------")
    f.write('\n' "WINNER!!    " + str(winner))






