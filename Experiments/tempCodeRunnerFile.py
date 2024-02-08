# import the mysql library
import mysql.connector as mysql

# Variables/Configurations
data_file = r'Data Analist\Projects\Toronto Airnb\calendar.csv'
delimiter=','
newline = '\n'
header=True
mysql_host = "126.0.0.1:3301"
mysql_port = "3301"
mysql_db = "airnb"
mysql_table = "calendar"
mysql_user = "Prabh"
mysql_password = "Prabhjot01"
# ----------------------------------
# read first line of the input file to create header
inFile = open(data_file,"r")
header = inFile.readline()
inFile.close()
# ---------------------------------------------------
# Extract column lists
column_list = header.split(delimiter)
# ---------------------------------------------------
# Construct Create table statement
create_table_statement = "CREATE TABLE " + mysql_db + "." + mysql_table + "("
for a_field in column_list:
    create_table_statement += a_field.replace("\n","") + " text,"
create_table_statement = create_table_statement[:-1] + ")"
print("Create Table Statement:")
print(create_table_statement)
print("---------------------------------------------------------------------------")
# ---------------------------------------------------
# Connect to mysql DB
db = mysql.connect(
    host = mysql_host,
    user = mysql_user,
    passwd = mysql_password,
    database = mysql_db,
    allow_local_infile=True
)
# ---------------------------------------------------
cursor = db.cursor()
# Creating table (DDL hence auto commit)
cursor.execute(create_table_statement)
# --------------------------------------
# Constructing load statement
load_statement = "LOAD DATA LOCAL INFILE '" + data_file + "'\nINTO TABLE " + mysql_db + "." + mysql_table + "\nFIELDS TERMINATED BY '" + delimiter + "'" + "\nLINES TERMINATED BY '" + newline + "'" + "\nIGNORE 1 LINES\n("
for a_field in column_list:
    load_statement += a_field.replace("\n","") + ","
load_statement = load_statement[:-1] + ");"
print("Load Table Statement:")
print(load_statement)
print("---------------------------------------------------------------------------")
# -------------------------------------
cursor.execute(load_statement)
db.commit()
db.close()
print("Complete")