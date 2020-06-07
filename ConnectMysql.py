import mysql.connector
try:
    connection = mysql.connector.connect(
        auth_plugin='mysql_native_password',
        port = 3306,
        host='localhost',
        database='emarket',
        user='root',
        password='123456')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")