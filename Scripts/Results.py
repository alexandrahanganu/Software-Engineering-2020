
import csv

with open('Final_Results.csv', 'w') as f:
    f.write('Filename, LeftLungAffected, RightLungAffected, CavernsLeft, CavernsRight, PleurisyLeft, PleurisyRight\n')


with open('C:\\Users\\Theo\\PycharmProjects\\TuberculosisProject\\TBC_Results_Left.csv', 'r') as file:
    row_count = sum(1 for row in file)#in order to know how many lines there are in each csv


with open('C:\\Users\\Theo\\PycharmProjects\\TuberculosisProject\\TBC_Results_Left.csv', 'r') as tbcleft:
    rowIndex = []
    tbcleftpercentage = []
    reader = csv.reader(tbcleft)
    for row in reader:
        rowIndex.append(row[0])
        tbcleftpercentage.append(row[1])


with open('C:\\Users\\Theo\\PycharmProjects\\TuberculosisProject\\TBC_Results_Right.csv', 'r') as tbcright:
    tbcrightpercentage = []
    reader = csv.reader(tbcright)
    for row in reader:
        tbcrightpercentage.append(row[1])


with open('C:\\Users\\Theo\\PycharmProjects\\TuberculosisProject\\Caverns_Results_Left.csv', 'r') as cavernsleft:
    clpercentage = []
    reader = csv.reader(cavernsleft)
    for row in reader:
        clpercentage.append(row[1])
    print (clpercentage)


with open('C:\\Users\\Theo\\PycharmProjects\\TuberculosisProject\\Caverns_Results_Right.csv', 'r') as cavernsright:
    crpercentage = []
    reader = csv.reader(cavernsright)
    for row in reader:
        crpercentage.append(row[1])
    print (crpercentage)


with open('C:\\Users\\Theo\\PycharmProjects\\TuberculosisProject\\Pleurisy_Results_Left.csv', 'r') as pleurisyleft:
    plpercentage = []
    reader = csv.reader(pleurisyleft)
    for row in reader:
        plpercentage.append(row[1])
    print (plpercentage)


with open('C:\\Users\\Theo\\PycharmProjects\\TuberculosisProject\\Pleurisy_Results_Right.csv', 'r') as pleurisyright:
    prpercentage = []
    reader = csv.reader(pleurisyright)
    for row in reader:
        prpercentage.append(row[1])
    print (prpercentage)


with open('Final_Results.csv', 'a') as f:
    i = 1
    for index in range(row_count-1):
        f.write('{}, {}, {}, {}, {}, {}, {}\n'.format(rowIndex[i], tbcleftpercentage[i], tbcrightpercentage[i],
                                                  clpercentage[i], crpercentage[i],
                                                  plpercentage[i], prpercentage[i]))
        i = i + 1


