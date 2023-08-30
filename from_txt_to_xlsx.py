import re
import os
import xlsxwriter


def taking_cities():
    # Finding all files in directory, and taking their names 
   cities = [filename for filename in os.listdir('nowe_miasta/')]
    return cities


def opening_file(file_name):
    # Opening and reading file
    with open('nowe_miasta/' + file_name, 'r') as file:
        city_data = file.read()
    return city_data


def find_values(city_data):
    # Values are separated by space, using regex to find all values
    values = re.findall(r'-*\w\S*', city_data)
    return [float(value) for value in values]


def creating_lines(values):
    # Creating table which has 8 item tables. Taking first 8 items from 46 items in values
    new_values = [['Godz.', 'Mies.', 'Dzien', 'Godz. UTC', 'Temp. term. such.', 'Wilg. wzgl.', 'Zaw. wilg.', 'Wiatr']]
    j = 0
    k = 1
    for i in values:
        if j == 0:
            i = float(i)
            new_values.append([i])
            j = j + 1
        elif j < 8:
            i = float(i)
            new_values[k].append(i)
            j = j + 1
        elif j == 45:
            j = 0
            k = k + 1
        else:
            j = j + 1
    return new_values


def saving_to_new_file(data, file_name):
    # Changing filename txt into xlsx
    file_name = file_name[:-3] + 'xlsx'

    # Create a workbook and add a worksheet
    workbook = xlsxwriter.Workbook('excele/' + file_name)
    worksheet = workbook.add_worksheet()

    # Start from the first cell. Rows and columns are zero indexed
    row = 3
    col = 0

    # Iterate over the data and write it out row by row
    for item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8 in data:
        worksheet.write(row, col, item_1)
        worksheet.write(row, col + 1, item_2)
        worksheet.write(row, col + 2, item_3)
        worksheet.write(row, col + 3, item_4)
        worksheet.write(row, col + 4, item_5)
        worksheet.write(row, col + 5, item_6)
        worksheet.write(row, col + 6, item_7)
        worksheet.write(row, col + 7, item_8)
        worksheet.write(row, col + 8, '=$B$1 - E' + str(row+1))
        row += 1

    # Writing basic - the same for all worksheets
    worksheet.write(0, 0, 'Temp. wew')
    worksheet.write(0, 1, 18)
    worksheet.write(3, 8, 'Stopniogodz.')

    workbook.close()


if __name__ == '__main__':
    cities = taking_cities()

    for i in cities:
        file_name = i
        city_data = opening_file(file_name)
        values = find_values(city_data)
        data = creating_lines(values)
        saving_to_new_file(data, file_name)
