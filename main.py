import csv

scores = {}

with open('Housing Form.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    x = 0
    for row in csvreader:
        if x == 0:
            x = 1
            continue

        scores[row[2]] = 0
        tempPoints = 0

        # Grade Level
        if row[5] == 'Junior':
            tempPoints += 20
        elif row[5] == 'Senior':
            tempPoints += 30
        
        # scores for each student are updated by dividing points earned by total possible points for the section and multiplying by the section's weight in the final score
        scores [row[2]] += (tempPoints / 30) * 19 
        tempPoints = 0

        # GPA
        for x in range(6, 9): # iterate through Spring 2019, Fall 2020, Winter 2020 (in reverse order)
            if row[x] == '3.7+': # GPA is 3.7+
                tempPoints += 6
            elif row[x] == '3.5 - 3.7': #  GPA is 3.5 - 3.7
                tempPoints += 4
            elif row[x] == '3.0 - 3.5': # GPA is 3.0 - 3.5
                tempPoints += 2
        
        scores [row[2]] += (tempPoints / 18) * 13.5
        tempPoints = 0

        # Positions Held
        if row[9] == 'Yes': # outgoing exec
            tempPoints += 20
        
        if row[10] == 'Yes': # incoming exec
            tempPoints += 20

        if row[11] == 'Yes': # candidate exec
            tempPoints += 10
        
        if row[12] == 'Yes': # honor board
            tempPoints += 5
        
        if row[13] == 'Yes': # non-exec chairman
            tempPoints += 10
        
        scores [row[2]] += (tempPoints / 65) * 18
        tempPoints = 0

        # Service
        if row[14] == 'Yes': # took a sigma nuggets shift
            tempPoints += 5
        tempPoints += float(row[15]) * 10 # mixer RM shifts
        tempPoints += float(row[16]) * 18 # party RM shifts
        tempPoints += float(row[17]) * 5 # num times opened room for party
        tempPoints += float(row[18]) * 25 # formal RM shifts

        scores [row[2]] += (tempPoints / 217) * 18
        tempPoints = 0

        # Volunteering 
        tempPoints += float(row[19]) * (20/36) # number of service hours - can claim up to 36
        tempPoints += float(row[20]) * 4 # number of IM teams participated in - can claim up to 5

        dmMoney = float(row[22]) * (1/16) # amount raised for DM - up to 40 pts
        if dmMoney > 40:
            tempPoints += 40
        else:
            tempPoints += dmMoney

        tempPoints += float(row[23]) * (5/2) # number of sigma nuggets tickets sold - can claim up to 6
        tempPoints += float(row[28]) * 5 # number of big/little taks completed - can claim up to 3

        scores [row[2]] += (tempPoints / 110) * 13.5
        tempPoints = 0
        
        # Attendance
        missedCandChapter = float(row[24]) * -1 # number of candidate chapters missed - up to -6 pts
        tempPoints += missedCandChapter
        
        missedRegChapter = float(row[25]) * -1 # number of regular chapters missed - up to -15 pts
        tempPoints += missedRegChapter
        
        tempPoints += float(row[26]) * 3 # number of brotherhood events attended of 9

        missedCandEvent = float(row[27]) * -1 # number of candidate events missed - up to -6 pts
        tempPoints += missedCandEvent

        scores [row[2]] += (tempPoints / 27) * 18

    sortedScores = {k: v for k, v in sorted(scores.items(), reverse=True, key=lambda item: item[1])}  

    for score in sortedScores:
        print (score, ":", round(sortedScores[score] * 10))

    