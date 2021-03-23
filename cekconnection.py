import pyodbc
import pandas as pd
#		KONEKSI DENGAN ODBC
def connectionSQLExpress():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=ADITYAANGR;'
                          'Database=pos;'
                          'UID=sa;'
                          'PWD=kudaponi69;'
                          'Trusted_Connection=no;')

    return conn

def functionDataframe(q):
    try:
        result = pd.read_sql(
            sql=q,
            con=connectionSQLExpress()
        )
    except Exception as e:
        result = 'Error: ', e
    return result


def get_querry_KBBIS_FIN(nama):
    results_query = (
        f'''
            SELECT *
            FROM [pos].[dbo].[masterbarang]
            where Nama like '%{nama}%'
            '''
        )
    all_result = functionDataframe(results_query)
    print(results_query)
    return all_result

#		KONEKSI DENGAN ODBC
def connectionSQLExpress():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=ADITYAANGR;'
                          'Database=pos;'
                          'UID=sa;'
                          'PWD=kudaponi69;'
                          'Trusted_Connection=no;')

    return conn

cnxn = connectionSQLExpress()
cursor = cnxn.cursor()
results_query = (
f'''
    SELECT *
    FROM [pos].[dbo].[masterbarang]
    '''
)
# print(results_query)
# cursor.execute(results_query)
# resultfirst = cursor.fetchall()
# print(len(resultfirst))


# field_names = [i[0] for i in cursor.description]

# print(field_names)
# print(field_names.__dict__)

from datetime import datetime 
import datetime

asd = datetime.datetime.utcnow().strftime('%Y-%m%d %H:%M:%S.%f0')
print(asd)