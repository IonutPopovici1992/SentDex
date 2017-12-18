import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    colors = []
    dates = []

    for row in readCSV:
        color = row[3]
        date = row[0]

        colors.append(color)
        dates.append(date)

    print(colors)
    print(dates)

    whatColor = input('What color do you wish to know the date of? ')
    color_index = colors.index(whatColor.lower())

    theDate = dates[color_index]

    print('The date of',whatColor,'is',theDate,'.')
