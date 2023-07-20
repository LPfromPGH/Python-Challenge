import os
import csv

# Gotta collect the Data
bank_csv = os.path.join('..', 'Resources', 'budget_data.csv')
# Place for Variables
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

    
#Values for Variables

    for row in csv_reader:
        time.append((row[0]))
        prof_loss=int(row[1])
        prof_losslist.append(prof_loss)

    first_row=next(csv_reader)
    prev_net = int(first_row[1])
    for row in csv_reader:
        
        
        change=int(row[1])-prev_net
        prev_net=int(row[1])
        change_list.append(change)
        if change>greatest_increase[1]:
            greatest_increase[1]=change
            greatest_increase[0]=row[0]
        if change<greatest_decrease[1]:
            greatest_decrease[1]=change
            greatest_decrease[0]=row[0]
        
total = sum(prof_losslist)
average_change = sum(change_list)/len(change_list)

with open('Finance_analysis.txt', 'w') as f:
    f.write("Financial Analysis")
    f.write('\n' "-------------------------------------------------------------------")
    f.write('\n' "Total Months:  " + str(len(time) + 1))
    f.write('\n' "Total:   " + str(total))
    f.write('\n' "Average Change:  " + str(average_change))
    f.write('\n' "Greatest Increase:"  + str(greatest_increase))
    f.write('\n' "Greatest Decrease:" + str(greatest_decrease))


print(f"Financial Analysis")
print(f"---------------------------------------------------------------------")

print(f"Total Months:  " + str(len(time) + 1))
print("Total:  " + str(total))
print("Average Change:  " + str(average_change))
print("Greatest Increase" + str(greatest_increase))
print("Greatest Decrease" + str(greatest_decrease))


      