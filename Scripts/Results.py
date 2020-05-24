# def def_labels_right_has_Tuberculosis(nume_pacient):
#     with open('D:\\Git\\CT_Report.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             if row[0] == nume_pacient:
#                 if row[2] == '1':
#                     return [1, 0]  # has tbc
#                 if row[2] == '0':
#                     return [0, 1]  # doesn't have tbc
#                 break



# with open('C:\\Users\\Theo\\PycharmProjects\\TuberculosisProject\\TBC_Results_Left.csv', 'r') as file:
#     with open('Final_Results.csv', 'a') as f:
#         rowIndex = []
#         tbcList = []
#         reader = csv.reader(file)
#         i = 0
#         j = 0
#         for row in reader:
#             id = row[0]
#             TBCpercent = row[1]
#             rowIndex.append(id)
#             tbcList.append(TBCpercent)
#             #fa liste pt fiecare coloana si apoi scrie
#
#         print (rowIndex)
#         print (tbcList)
#         print (rowIndex[0])
#         print (tbcList[0])
#         print (row_count)





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


# with open('TBC_Results_Right.csv', 'w') as f:
#     f.write('id,label\n')
#
# with open('TBC_Results_Right.csv', 'a') as f:
#     value = '178'
#     avg = 0
#     cont = 0
#     valoare = 0
#     for data in tqdm(test_data):
#         img_num = data[1]
#
#         if value in img_num:
#
#             cont = cont + 1
#             img_data = data[0]
#             data = img_data.reshape(-1, IMG_SIZE, IMG_SIZE, easy)
#             model_out = model.predict([data])[0]
#             avg = avg + model_out[0]
#         else:
#             valoare = avg / cont
#             f.write('{}, {}\n'.format(value, valoare))
#             value1 = int(value)
#             value1 = value1 + 1
#             value = str(value1)
#
#             avg = 0
#             cont = 0
#     valoare = avg / cont
#     f.write('{}, {}\n'.format(value, valoare))
