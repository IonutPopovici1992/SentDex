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

    try:
        whatColor = input('What color do you wish to know the date of? ')

        if whatColor in colors:
            color_index = colors.index(whatColor.lower())
            theDate = dates[color_index]
            print('The date of', whatColor, 'is:', theDate, '.')
        else:
            print('Color not found, or is not a color!')

    except Exception as e:
        print(e)

    print('Continuing ...')
