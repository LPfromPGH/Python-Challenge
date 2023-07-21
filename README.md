# Python-Challenge
 Module 3 Work
![IMAGE_DESCRIPTION](https://github.com/LPfromPGH/Python-Challenge/blob/main/Resources/revenue-per-lead.png)

Pybank Challenge:
In this challenge we had to accomplish the following:
• The total number of months included in the dataset
• The net total amount of "Profit/Losses" over the entire period
• The changes in "Profit/Losses" over the entire period, and then the average of those changes
• The greatest increase in profits (date and amount) over the entire period
• The greatest decrease in profits (date and amount) over the entire period
  Print the information to the terminal and to a TXT file.

My number of months and net total are off, basically I'm missing the first row of data.
I know the problem has to do with this section:
"csv_header = next(csv_reader)
#Values for Variables
    first_row=next(csv_reader)"

But everything I tried to remedy the issue broke the code and then nothing would work right. So I'll take the deduction, losing 5 points is better than losing all of them lol.
Big shout out to Marc Calache, my tutor. He helped me fix my code so that Python would read my list as integers, and also helped me with the greatest increase/decrease and average change part of my code.
![IMAGE DESCRIPTION](https://github.com/LPfromPGH/Python-Challenge/blob/main/Screenshot%202023-07-20%20Finance.png)

PyPoll
![IMAGE DESCRIPTION](https://github.com/LPfromPGH/Python-Challenge/blob/main/Resources/Vote_counting.png)
In this challenge we had to accomplish the following:
• The total number of votes cast
• A complete list of candidates who received votes
• The percentage of votes each candidate won
• The total number of votes each candidate won
• The winner of the election based on popular vote
  Print the information to the terminal and to a TXT File

![IMAGE DESCRIPTION](https://github.com/LPfromPGH/Python-Challenge/blob/main/Screenshot%202023-07-20%20Election.png)

In this one everything worked correctly! The count command, round command and the write command were gleaned from the following:
Count command : https://pythonhow.com/how/count-the-occurrences-of-an-item-in-a-list/
Round command (Used in both challenges): https://stackoverflow.com/questions/46481351/how-to-round-numbers-to-the-nearest-1000
write function (Used in both challeges) : https://www.pythontutorial.net/python-basics/python-write-text-file/