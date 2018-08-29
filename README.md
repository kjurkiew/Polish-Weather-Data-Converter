# From_txt_to_xls
  On side [miir.gov.pl](https://www.miir.gov.pl/strony/zadania/budownictwo/charakterystyka-energetyczna-budynkow/dane-do-obliczen-energetycznych-budynkow-1/) you can download data about weather in 61 cities in Poland. The main problem is that they are in txt file, not separated by comma but with random number of space. Energetic Auditors need that data in xlsx file to caluculate degree hours. This program take txt file and change it to xlsx file also making basic calculations for degree hours  

## Execution

The script find all files in directory, and taking their names. Opens and reads file. Using regex to take values into table. Saving data from table to xlsx file, and adding some basic formula to help caluculate degree hours
