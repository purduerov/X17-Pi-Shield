"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Multiplies CSV row 2 by 4 and displays on a scatterplot.

Assignment Information:
    Assignment:     8.1.2. Py4 Pre 1
    Team ID:        011_28
    Author:         Nicholas Zhang, nzhang21@purdue.edu
    Date:           09/21/24

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import matplotlib.pyplot as plt
import csv
import numpy as np


def main():
    in_file = 'py4_pre_task0_data.csv'
    out_file = 'y4_pre_1_nzhang21.csv'

    x = []
    Y = []

    # input and open file, change and write to new csv
    with open(in_file, mode='r') as infile, open(out_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        
        writer = csv.writer(outfile)

        for row in reader:
            row[1] = str(int(row[1]) * 4)
            Y.append(int(row[1]))
            x.append(float(row[0]))

    # create scatterplot
    plt.scatter(x, Y)
    plt.xlabel('Time (s)')
    plt.ylabel('Original Data')
    plt.title('Py4_Pre_1_data')
    
    plt.show()

if __name__ == "__main__":
    main()
