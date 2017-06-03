#!/usr/bin/python
import argparse
import csv
import re

class Csv2LatexTable:
    def __init__(self, inputFile, delimiter, quotechar, tablepos, cap, reflabel, noUnderLine, tableSpec, longTable, lessSpacing, twoColumn):
        self.inputFile = inputFile
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.tablePos  = tablepos 
        self.caption   = cap
        self.refLabel  = reflabel
        self.noUnderLine = noUnderLine
        self.tableSpec = tableSpec
        self.longTable = longTable
        self.lessSpacing = lessSpacing
        self.twoColumn = twoColumn

    def readCsvandMakeTable(self):
        """Reads a csv file and outputs a table to stdout"""
        with open(self.inputFile, "r") as csvfile:
            tablereader = csv.reader(csvfile, delimiter=self.delimiter, quotechar=self.quotechar)
            columnHeaders = tablereader.next()
            numColumn = len(columnHeaders)
            self.genTableHead(numColumn, columnHeaders)
            

            if (not self.noUnderLine):
                print("\\hline")
            
            for row in tablereader:
                if (not self.lessSpacing):
                    print('&'*(numColumn-1) + '\\\\')
                
                # Replace newlines or comma with actual newline in table
                for i in range(numColumn-1): #temp fix
                    if '\n' in row[i]:
                        row[i] = '\\parbox{0.4\\textwidth}{' + str.replace(row[i], '\n', ' \\\\') + '}'
                    elif ',' in row[i]:
                        row[i] = '\\parbox{0.4\\textwidth}{' + str.replace(row[i], ',', ' \\\\') + '}'
                    
                if '\n' in row:
                    print(row.index('\n'))
                
                print("  %s \\\\" % re.sub('_', '\\_', ' & '.join(row[:numColumn]) ))
                if (not self.noUnderLine):
                    print("\\hline")
            
            self.genTableFooter()



    def longTableHeaders(self, numColumn, columnHeaders):
        """ Generates the column headers for longtable,
        function takes number of columns and the column headers"""
        for i in range(numColumn):
            joiner = " &"
            if (i == (numColumn-1)):
                joiner = " \\\\"
            print("\\multicolumn{1}{%s|}{\\textbf{%s}} %s" % (self.tableSpec, columnHeaders[i], joiner))

    def genTableHead(self, numColumn, columnHeaders):
        """Make the table headers,
        either standard or longtable."""
        temp = '|' + self.tableSpec + (('|'+self.tableSpec)*(numColumn-1)) + '|'
        if (not self.longTable):
            print("""\\begin{table%s}[%s]
\\centering
 \\caption{%s}
 \\begin{tabular}{%s}""" % ("*" if self.twoColumn else "", self.tablePos, self.caption, temp))
        
            print("  %s \\\\" % (' & '.join(columnHeaders[:numColumn])))
            print("  \\hline")
            
        else:
            print("""\\begin{center}
\\begin{longtable}[%s]{%s}
\\caption{%s}""" % (self.tablePos, temp, self.caption))

            if (self.refLabel != ""):
                print("\\label{%s}\\\\" % self.refLabel)
                print("\\hline")
            
            self.longTableHeaders(numColumn, columnHeaders)
            print("""\\hline 
\\endfirsthead
\\multicolumn{%d}{c}{{\\bfseries \\tablename\\ \\thetable{} -- continued from previous page}} \\\\
\hline""" % numColumn)
            self.longTableHeaders(numColumn, columnHeaders)
            print("""\\hline 
\\endhead

\\hline \\multicolumn{%d}{|r|}{{Continued on next page}} \\\\ \\hline
\\endfoot

\\hline \\hline
\\endlastfoot""" % numColumn)


    def genTableFooter(self):
        """ Prints out table footers """
        if (not self.longTable):
            print(" \\end{tabular}")
            if (self.refLabel != ""):
                print("\\label{%s}" % self.refLabel)
            print ("\\end{table%s}" % ("*" if self.twoColumn else ""))
        else:
            print("\\end{longtable}")
            if (self.refLabel != ""):
                print("\\label{%s}" % self.refLabel)
            print("\\end{center}")




if __name__=="__main__":
    parser = argparse.ArgumentParser(
        description="""Csv to latex table converter.  """)
    parser.add_argument('-i', dest='inputFile', default="example1.csv", 
                        help="Csv file to read, default=example1.csv")    
    parser.add_argument('-d', dest='delimiter', default=";", 
                        help="Set csv delimiter, default=;")    
    parser.add_argument('-q', dest='quotechar', default='"', 
                        help='Set csv quotechar, default="')    
    parser.add_argument('-pos', dest='tablePos', default="htbp", 
                        help="Set table position, default=htbp")
    parser.add_argument('-caption', dest='caption', default="Generated table", 
                        help="Set table caption, default='Generated table'")   
    parser.add_argument('-label', dest='refLabel', default="", 
                        help="Set table reference label, default=''")   
    parser.add_argument('--nounderline', dest='noUnderLine', action='store_true',
                        help="Don't add underline for each entry")   
    parser.add_argument('-tablespec', dest='tableSpec', default="c", 
                        help="Set table specifications, default='c', takes one type and repeats it")  
    parser.add_argument('--longtable', dest='longTable', action='store_true',
                        help="Use longtable package") 
    parser.add_argument('--lessspacing', dest='lessSpacing', action='store_true',
                        help="Don't add '&&&\\\\' as spacings between entries") 
    parser.add_argument('--twocolumn', dest='twoColumn', action='store_true',
                        help="Use table* package across two columns")   
    

    args = parser.parse_args()

    c2lt = Csv2LatexTable(args.inputFile, args.delimiter, args.quotechar, args.tablePos, args.caption, args.refLabel, args.noUnderLine, args.tableSpec, args.longTable, args.lessSpacing, args.twoColumn)
    c2lt.readCsvandMakeTable()
