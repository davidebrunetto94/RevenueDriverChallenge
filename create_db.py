from numpy import insert
import pymysql
import pandas as pd

def main():
    path = "./code_challenge.csv"
    df = pd.read_csv(path, sep=";")

    #preprocessing of some columns to make them more suitable for the db
    df["True Revenue"] = df.apply(lambda row: row["True Revenue"][1:], axis=1) #this remove the "$" from the column
    df["Coverage"] = df.apply(lambda row: row["Coverage"][:-1], axis=1) #this removes the "%" from the column
    df["Queries"] = df.apply(lambda row: row["Queries"].replace(',', ''), axis=1) #removes the commas from some numbers such as "1,254"

    header= list(df) #this will contain the header that will make the structure for the table
    rows = df.apply(lambda x: x.tolist(), axis=1)
    try:
        db_connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin')
        cursor = db_connection.cursor()

        db_query = "CREATE DATABASE IF NOT EXISTS challenge"
        cursor.execute(db_query)

        drop_query = "DROP TABLE IF EXISTS challenge.new_table"
        cursor.execute(drop_query)

        creation_query = "CREATE TABLE challenge.new_table( \
                        {} DATE, \
                        `{}` VARCHAR(50),\
                        `{}` INT UNSIGNED PRIMARY KEY, \
                        `{}` INT UNSIGNED, \
                        `{}` VARCHAR(40), \
                        `{}`VARCHAR(40), \
                        `{}` INT UNSIGNED, \
                        `{}` INT UNSIGNED, \
                        `{}` INT UNSIGNED, \
                        `{}` FLOAT, \
                        `{}` FLOAT, \
                        `{}` FLOAT, \
                        `{}` FLOAT, \
                        `{}` FLOAT)".format(*header)
        cursor.execute(creation_query)
        
        rows_tuples = [tuple(x) for x in rows] #We need the rows in a list of tuples to use it on executemany
        insert_query = "INSERT INTO challenge.new_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.executemany(insert_query, rows_tuples)
        db_connection.commit()
    except Exception as e:
        print("Exception occurred : {}".format(e))
    finally:
        db_connection.close()
        print("Connection to the db closed")

if __name__ == "__main__":
    main()