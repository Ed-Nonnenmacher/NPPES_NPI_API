# NPPES_NPI_API
Small, simple script to pull most data pertaining to NPI numbers searched for through NPPES' API.

This script is only suitable to take a list of NPI numbers and pull most information provided by the NPPES API and stores as an excel workbook.  There is different data available depending on types of practices, taxonomies, etc, so this will generate a 56 column length dataframe.  While script is running, each iteration/call to the API will print iteration index, NPI #, length of current record pulled for given NPI #, and total dataframe length.

#How to use-
Store a csv file containing all NPI #'s you want data for as NPI.csv in same directory as your root python files. (usually Python37 folder for windows, which is where all your scripts are stored by default with idle.)

Create a subfolder named npis.  This will be your checkpoint area.  Every 20k iterations will store current dataframe in this subfolder as fault protection.

You should be all set after this!

Script was developed for Windows only, with a broad assumption for users understanding basic pathing and file structure.


Please reach out to edward.nonnenmacher@outlook.com with any issues.
