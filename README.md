# From_txt_to_xls
  On side miir.gov.pl you can download data about weather in 61 cities in Poland. The main problem is that they are in txt file, not separated by comma but with random number of space. Energetic Auditors need that data in xlsx file to caluculate degree hours. This program take txt file and change it to xlsx file also making basic calculations for degree hours  
[a link](https://www.miir.gov.pl/strony/zadania/budownictwo/charakterystyka-energetyczna-budynkow/dane-do-obliczen-energetycznych-budynkow-1/)

## Execution

The script takes two arguments (first: a path to file with the websites addres; second: name of the file with results) and write results.
Example:
```
buttonz-counter.py files_with_websites counted_websites.csv
```
