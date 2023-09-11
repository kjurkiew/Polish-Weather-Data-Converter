# Polish-Weather-Data-Converter
The "Polish Weather Data Converter" is a Python script designed to simplify the process of converting weather data from the miir.gov.pl website, available in text format, into Excel (.xlsx) files. This tool is particularly valuable for Energetic Auditors and researchers who need structured weather data for various cities in Poland.

## Features

File Conversion: The program identifies and processes all text files within a specified directory.

Data Extraction: Using regular expressions, the program extracts relevant values from the text files and organizes them into a structured table.

Excel Output: The extracted data is then saved in Excel format (.xlsx), making it convenient for further analysis.

Basic Calculations: Additionally, the program includes basic formulas in the Excel file to assist with degree hour calculations.

## Execution

Clone or download the repository to your local machine.

Ensure you have the necessary dependencies installed, which include re, os, xlsxwriter, and typing.

Run the script to initiate the conversion process. The script will identify all text files within a specified directory and convert them to Excel format.

The resulting Excel files will contain organized weather data for further analysis and degree hour calculations.

## Usage

This project simplifies the task of converting weather data from text files into Excel files, streamlining the process for Energetic Auditors and anyone requiring weather data in a more structured and convenient format.

Note: Ensure that the miir.gov.pl weather data files are placed in the designated input directory before running the script.
