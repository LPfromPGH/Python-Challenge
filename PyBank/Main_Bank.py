import os
import csv

# Gotta collect the Data
bank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

time = []
prof_losslist = []

total = 0
prof_loss = 0
average_change = 0
change_list=[]
greatest_increase = ["",-10000]
greatest_decrease = ["",10000]
# Reading the CSV
with open(bank_csv, encoding="utf_8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csv_reader)

    
   # total = sum([int(row[1]) for row in csv_reader])

    #total_months = 1
    #prof_loss = 0
    first_row=next(csv_reader)
    prev_net = int(first_row[1])
    for row in csv_reader:
        time.append((row[0]))
        prof_loss=int(row[1])

        prof_losslist.append(prof_loss)
        change=int(row[1])-prev_net
        prev_net=int(row[1])
        change_list.append(change)
        if change>greatest_increase[1]:
            greatest_increase[1]=change
            greatest_increase[0]=row[0]
        if change<greatest_decrease[1]:
            greatest_decrease[1]=change
            greatest_decrease[0]=row[0]
        #prof_loss.append([int(row['Profit/Losses'])])
        
        #total_months += int(row[0])
        #prof_loss = ((row[1]))

        

        #prof_loss.append((row[1]))
total = sum(prof_losslist)
average_change = sum(change_list)/len(change_list)
    #total += (prof_loss)
       # total = sum(prof_loss)
       # if not str(row[1]).startswith('P'):
        #    total = total + int(float(row[1]))
   # total = [sum(prof_loss)]
    #for col in prof_loss:
    #    if prof_loss = int

    #time.append(row["date"])
    #prof_loss.append(row[1])


    # might not need this piece
    
  #  print(f"Header: {csv_header}")
#Function Junction

#def Total_months(bank_csv)
    
   # Month = len(bank_csv["date"])
#    Net_Prof = int(bank_csv[1])

#time = int(len{csvfile["date"]})

#net_prof = sum(int(r[2]))
#for numbers in (prof_loss):
#    total =+ numbers

#for row in cr:  
#  total += int(row[2])



print(f"Financial Analysis")
print(f"---------------------------------------------------------------------")

print(f"Total Months:  " + str(len(time) + 1))
print("Total:  " + str(total))
print("Average Change:  " + str(average_change))
#print(f"total Months:  " + {total_months})
#print("Total:   " + str(prof_losslist))
print("Greatest Increase" + str(greatest_increase))
print("Greatest Decrease" + str(greatest_decrease))
#def list_information(prof_loss):
#    print(f"Total:    ")
#    for value in prof_loss:
#        print(value)
#print(f"Total:  " + int((prof_loss)))
#print(f"Total Months:" [time])

#print(f"Total:  " [net_prof])

      