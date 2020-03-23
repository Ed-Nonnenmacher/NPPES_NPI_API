# NPPES_NPI_API
Small, simple script to pull most data pertaining to NPI numbers searched for through NPPES' API.

This script is only suitable to take a list of NPI numbers and pull most information provided by the NPPES API and stores as an excel workbook.  There is different data available depending on types of practices, taxonomies, etc, so this will generate a 56 column length dataframe.  While script is running, each iteration/call to the API will print iteration index, NPI #, length of current record pulled for given NPI #, and total dataframe length.

#Basic Operation
At a fundamental level, NPPES hosts an API service for its NPI database through its core url: https://npiregistry.cms.hhs.gov/api/?. Among the many different paramenters possibly to query for, this script uses only 1, being the NPI number, queried with the following url https://npiregistry.cms.hhs.gov/api/?number={i}&version=2.1. (Substitute {i} for NPI number of choice for a proper call). No authentication key is needed, as this is a free service hosted by NPPES.
Response from API is provided in Json format with some consistent information such as names, phone numbers, and taxonomies, where some organizations and practices will have authorizers info, and other identifiers.  This is all included pulled if available, otherwise denoted as "N/A".  There is a timer built in for every 15 iterations where a random 0-5 second delay occurs, and every 1,000 iterations a 7 second delay plus a random interval between 0-5 seconds.



#How to use-
Store a csv file containing all NPI #'s you want to pull data for named "NPI.csv" in the same directory as your root python files. (usually Python37 folder for windows, which is where all your scripts are stored by default with idle.)

Create a subfolder named npis.  This will be your checkpoint area.  Every 20k iterations will store current dataframe in this subfolder as fault protection.

You should be all set after this!

Script was developed for Windows only, with a broad assumption made that users have a basic understanding of pathing and file structures.


Please reach out to edward.nonnenmacher@outlook.com with any issues.
