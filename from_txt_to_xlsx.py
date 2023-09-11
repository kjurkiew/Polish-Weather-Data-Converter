import re
import os
import xlsxwriter
from typing import List

# Constants
NUM_COLUMNS = 8


def get_city_files(directory: str) -> List[str]:
    """Get a list of city files in the specified directory.

    Args:
        directory (str): The directory to search for city files.

    Returns:
        List[str]: A list of city file names.
    """
    return [filename for filename in os.listdir(directory) if filename.endswith(".txt")]


def read_city_data(file_path: str) -> str:
    """Read and return the content of a city file.

    Args:
        file_path (str): The path to the city file.

    Returns:
        str: The content of the city file as a string.
    """
    with open(file_path, "r") as file:
        return file.read()


def extract_values(city_data: str) -> List[float]:
    """Extract numerical values from city data.

    Args:
        city_data (str): The city data as a string.

    Returns:
        List[float]: A list of extracted numerical values.
    """
    return [float(value) for value in re.findall(r"-*\w\S*", city_data)]


def creating_lines(values: List[float]) -> List[List[float]]:
    """Create a table from numerical values.

    Args:
        values (List[float]): A list of numerical values.

    Returns:
        List[List[float]]: A list of lists representing the table.
    """
    table = [
        [
            "Godz.",
            "Mies.",
            "Dzien",
            "Godz. UTC",
            "Temp. term. such.",
            "Wilg. wzgl.",
            "Zaw. wilg.",
            "Wiatr",
        ]
    ]
    column_index = 0
    row_index = 1

    for value in values:
        if column_index == 0:
            value = float(value)
            table.append([value])
            column_index += 1
        elif column_index < 8:
            value = float(value)
            table[row_index].append(value)
            column_index += 1
        elif column_index == 45:
            column_index = 0
            row_index += 1
        else:
            column_index += 1

    return table


def save_to_excel(data: List[List[float]], output_filename: str) -> None:
    """Save data to an Excel file.

    Args:
        data (List[List[float]]): The data to be saved as a table.
        output_filename (str): The name of the output Excel file.
    """
    output_filename = output_filename[:-4] + ".xlsx"  # Ensure it's an xlsx file
    workbook = xlsxwriter.Workbook(os.path.join("excele", output_filename))
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
        worksheet.write(row, col + 8, "=$B$1 - E" + str(row + 1))
        row += 1

    # Writing basic - the same for all worksheets
    worksheet.write(0, 0, "Temp. wew")
    worksheet.write(0, 1, 18)
    worksheet.write(3, 8, "Stopniogodz.")

    workbook.close()


if __name__ == "__main__":
    city_directory = "nowe_miasta/"
    cities = get_city_files(city_directory)

    for city_file in cities:
        city_data = read_city_data(os.path.join(city_directory, city_file))
        values = extract_values(city_data)
        data = creating_lines(values)
        save_to_excel(data, city_file)
