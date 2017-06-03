# python-csv-to-latex-table-script
Simple script which takes a csv file and outputs a latex table to stdout


Tested with python version 2.7.5

## Usage:
    $ python csv2latextable.py -i example1.csv
Writes to stdout a latex table based on example1.csv

    $ python csv2latextable.py -i example1.csv | pbcopy
Copies output directly to clipboard

Add the flag "-h" to get more info about user selectable parameters.

```
python csv2latextable.py -h
usage: csv2latextable.py [-h] [-i INPUTFILE] [-d DELIMITER] [-q QUOTECHAR]
                         [-pos TABLEPOS] [-caption CAPTION] [-label REFLABEL]
                         [-columns COLUMNS] [--nounderline] [-tablespec TABLESPEC]
                         [--longtable] [--lessspacing] [--twocolumn] [--notopline]
                         [--doubleunderline]

Csv to latex table converter.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE          Csv file to read, default=example1.csv
  -d DELIMITER          Set csv delimiter, default=;
  -q QUOTECHAR          Set csv quotechar, default="
  -pos TABLEPOS         Set table position, default=htbp
  -caption CAPTION      Set table caption, default='Generated table'
  -label REFLABEL       Set table reference label, default=''
  -columns COLUMNS      Excplicitly include given columns, default=':'
                        Given as single number, or range (0:3, 4:, 5:9)
  --nounderline         Don't add underline for each entry
  -tablespec TABLESPEC  Set table specifications, default='c', takes one type
                        and repeats it
  --longtable           Use longtable package
  --lessspacing         Don't add '&&&\\' as spacings between entries
  --twocolumn           Use table* package across two columns
  --notopline           Don't add a top line to the table
  --doubleunderline     Add double underline below headers
```

