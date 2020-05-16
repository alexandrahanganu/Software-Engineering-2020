import unittest
import os
import csv
# CSV IN D:\\GIT\\CSV\\...
# 178-188 results UNIT TESTING
# Spunem ca medie_bolnav sub 0.5 sanatos peste 0.5 bolnav
# Start este pacientul cu care se incepe, stop pacientul cu care se termina, verificati sa aveti valori in ambele CSV-uri, cel principal unde vedeti clar daca un pacient
# este bolnav sau nu si in al doilea CSV (TBC_LEFT, TBC_RIGHT, CAVERNA_LEFT, CAVERNA_RIGHT, PLEUREZIE_LEFT, PLEUREZIE_RIGHT)
# CSV PRINCIPAL DE FORMA(RASPUNSURILE CORECTE):
# Pacientul(NUMAR):{row[0]} - LeftLungAffected {row[1]}, RightLungAffected {row[2]},CavernsLeft {row[3]},CavernsRight {row[4]},PleurisyLeft {row[5]},PleurisyRight {row[6]}
# CSV SECUNDAR DE FORMAL(TBC_LEFT, TBC_RIGHT, CAVERNA_LEFT, CAVERNA_RIGHT, PLEUREZIE_LEFT, PLEUREZIE_RIGHT):
# Pacientul(NUMAR):{row[0]} PREDICTIE: {row[1]}
Start = 178
Stop = 188
Diferenta = Stop - Start + 1
medie_bolnav = 0.5
class TestCase(unittest.TestCase):
    def test_TBC_Results_Left(self):
        predictii_gresite = 0
        predictii_corecte = 0
        with open('D:\\Git\\CSV\\CT_Report.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Coloanele sunt: {", ".join(row)}')
                    line_count += 1
                else:
                    if(line_count>=Start and line_count<=Stop):
                        #print(f'\tPacientul:{row[0]} - LeftLungAffected {row[1]}, RightLungAffected {row[2]},CavernsLeft {row[3]},CavernsRight {row[4]},PleurisyLeft {row[5]},PleurisyRight {row[6]}')
                        with open('D:\\Git\\CSV\\TBC_Results_Left.csv') as csv_file2:
                            csv_reader2 = csv.reader(csv_file2, delimiter=',')
                            for row2 in csv_reader2:
                                #print(f'\tPacientul:{row2[0]} - LeftLungAffected {row2[1]}')
                                if (row2[0] == row[0]):
                                    if(int(row[1])==1):
                                        if(float(row2[1]) < medie_bolnav):
                                            predictii_gresite = predictii_gresite + 1
                                        else:
                                            predictii_corecte = predictii_corecte + 1
                                    else:
                                        if (float(row2[1]) > medie_bolnav):
                                            predictii_gresite = predictii_gresite + 1
                                        else:
                                            predictii_corecte = predictii_corecte + 1
                    line_count += 1
        self.assertEqual(predictii_corecte, Diferenta,"[TBC_Results_Left]Raspunsuri corecte:" + str(predictii_corecte) + ", raspunsuri gresite:" + str(predictii_gresite))
    def test_TBC_Results_Right(self):
        predictii_gresite = 0
        predictii_corecte = 0
        with open('D:\\Git\\CSV\\CT_Report.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Coloanele sunt: {", ".join(row)}')
                    line_count += 1
                else:
                    if(line_count>=Start and line_count<=Stop):
                        #print(f'\tPacientul:{row[0]} - LeftLungAffected {row[1]}, RightLungAffected {row[2]},CavernsLeft {row[3]},CavernsRight {row[4]},PleurisyLeft {row[5]},PleurisyRight {row[6]}')
                        with open('D:\\Git\\CSV\\TBC_Results_Right.csv') as csv_file2:
                            csv_reader2 = csv.reader(csv_file2, delimiter=',')
                            for row2 in csv_reader2:
                                #print(f'\tPacientul:{row2[0]} - LeftLungAffected {row2[1]}')
                                if (row2[0] == row[0]):
                                    if(int(row[2])==1):
                                        if(float(row2[1]) < medie_bolnav):
                                            predictii_gresite = predictii_gresite + 1
                                        else:
                                            predictii_corecte = predictii_corecte + 1
                                    else:
                                        if (float(row2[1]) > medie_bolnav):
                                            predictii_gresite = predictii_gresite + 1
                                        else:
                                            predictii_corecte = predictii_corecte + 1
                    line_count += 1
        self.assertEqual(predictii_corecte, Diferenta,"[TBC_Results_Right]Raspunsuri corecte:" + str(predictii_corecte) + ", raspunsuri gresite:" + str(predictii_gresite))
    def test_Caverns_Results_Left(self):
        predictii_gresite = 0
        predictii_corecte = 0
        with open('D:\\Git\\CSV\\CT_Report.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Coloanele sunt: {", ".join(row)}')
                    line_count += 1
                else:
                    if(line_count>=Start and line_count<=Stop):
                        #print(f'\tPacientul:{row[0]} - LeftLungAffected {row[1]}, RightLungAffected {row[2]},CavernsLeft {row[3]},CavernsRight {row[4]},PleurisyLeft {row[5]},PleurisyRight {row[6]}')
                        with open('D:\\Git\\CSV\\Caverns_Results_Left.csv') as csv_file2:
                            csv_reader2 = csv.reader(csv_file2, delimiter=',')
                            for row2 in csv_reader2:
                                #print(f'\tPacientul:{row2[0]} - LeftLungAffected {row2[1]}')
                                if (row2[0] == row[0]):
                                    if(int(row[3])==1):
                                        if(float(row2[1]) < medie_bolnav):
                                            predictii_gresite = predictii_gresite + 1
                                        else:
                                            predictii_corecte = predictii_corecte + 1
                                    else:
                                        if (float(row2[1]) > medie_bolnav):
                                            predictii_gresite = predictii_gresite + 1
                                        else:
                                            predictii_corecte = predictii_corecte + 1
                    line_count += 1
        self.assertEqual(predictii_corecte, Diferenta,"[Caverns_Results_Left]Raspunsuri corecte:" + str(predictii_corecte) + ", raspunsuri gresite:" + str(predictii_gresite))
    def test_Caverns_Results_Right(self):
        predictii_gresite = 0
        predictii_corecte = 0
        with open('D:\\Git\\CSV\\CT_Report.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Coloanele sunt: {", ".join(row)}')
                    line_count += 1
                else:
                    if(line_count>=Start and line_count<=Stop):
                        #print(f'\tPacientul:{row[0]} - LeftLungAffected {row[1]}, RightLungAffected {row[2]},CavernsLeft {row[3]},CavernsRight {row[4]},PleurisyLeft {row[5]},PleurisyRight {row[6]}')
                        with open('D:\\Git\\CSV\\Caverns_Results_Right.csv') as csv_file2:
                            csv_reader2 = csv.reader(csv_file2, delimiter=',')
                            for row2 in csv_reader2:
                                #print(f'\tPacientul:{row2[0]} - LeftLungAffected {row2[1]}')
                                if (row2[0] == row[0]):
                                    if(int(row[4])==1):
                                        if(float(row2[1]) < medie_bolnav):
                                            predictii_gresite = predictii_gresite + 1
                                        else:
                                            predictii_corecte = predictii_corecte + 1
                                    else:
                                        if (float(row2[1]) > medie_bolnav):
                                            predictii_gresite = predictii_gresite + 1
                                        else:
                                            predictii_corecte = predictii_corecte + 1
                    line_count += 1
        self.assertEqual(predictii_corecte, Diferenta,"[Caverns_Results_Right]Raspunsuri corecte:" + str(predictii_corecte) + ", raspunsuri gresite:" + str(predictii_gresite))
    def test_Pleurisy_Results_Left(self):
        predictii_gresite = 0
        predictii_corecte = 0
        with open('D:\\Git\\CSV\\CT_Report.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Coloanele sunt: {", ".join(row)}')
                    line_count += 1
                else:
                    if(line_count>=Start and line_count<=Stop):
                        #print(f'\tPacientul:{row[0]} - LeftLungAffected {row[1]}, RightLungAffected {row[2]},CavernsLeft {row[3]},CavernsRight {row[4]},PleurisyLeft {row[5]},PleurisyRight {row[6]}')
                        with open('D:\\Git\\CSV\\Pleurisy_Results_Left.csv') as csv_file2:
                            csv_reader2 = csv.reader(csv_file2, delimiter=',')
                            for row2 in csv_reader2:
                                #print(f'\tPacientul:{row2[0]} - LeftLungAffected {row2[1]}')
                                if (row2[0] == row[0]):
                                    if(int(row[5])==1):
                                        if(float(row2[1]) < medie_bolnav):
                                            predictii_gresite = predictii_gresite + 1
                                        else:
                                            predictii_corecte = predictii_corecte + 1
                                    else:
                                        if (float(row2[1]) > medie_bolnav):
                                            predictii_gresite = predictii_gresite + 1
                                        else:
                                            predictii_corecte = predictii_corecte + 1
                    line_count += 1
        self.assertEqual(predictii_corecte, Diferenta,"[Pleurisy_Results_Left]Raspunsuri corecte:" + str(predictii_corecte) + ", raspunsuri gresite:" + str(predictii_gresite))
    def test_Pleurisy_Results_Right(self):
        predictii_gresite = 0
        predictii_corecte = 0
        with open('D:\\Git\\CSV\\CT_Report.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Coloanele sunt: {", ".join(row)}')
                    line_count += 1
                else:
                    if(line_count>=Start and line_count<=Stop):
                        #print(f'\tPacientul:{row[0]} - LeftLungAffected {row[1]}, RightLungAffected {row[2]},CavernsLeft {row[3]},CavernsRight {row[4]},PleurisyLeft {row[5]},PleurisyRight {row[6]}')
                        with open('D:\\Git\\CSV\\Pleurisy_Results_Right.csv') as csv_file2:
                            csv_reader2 = csv.reader(csv_file2, delimiter=',')
                            for row2 in csv_reader2:
                                #print(f'\tPacientul:{row2[0]} - LeftLungAffected {row2[1]}')
                                if (row2[0] == row[0]):
                                    if(int(row[6])==1):
                                        if(float(row2[1]) < medie_bolnav):
                                            predictii_gresite = predictii_gresite + 1
                                        else:
                                            predictii_corecte = predictii_corecte + 1
                                    else:
                                        if (float(row2[1]) > medie_bolnav):
                                            predictii_gresite = predictii_gresite + 1
                                        else:
                                            predictii_corecte = predictii_corecte + 1
                    line_count += 1
        self.assertEqual(predictii_corecte, Diferenta,"[Pleurisy_Results_Right]Raspunsuri corecte:" + str(predictii_corecte) + ", raspunsuri gresite:" + str(predictii_gresite))


if __name__ == '__main__':
    unittest.main()
#print('Predictii corecte TBC:' + str(predictii_corecte))
#print('Predictii gresite TBC:' + str(predictii_gresite))
#print(f'Processed {line_count} lines.')