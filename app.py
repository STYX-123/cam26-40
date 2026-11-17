import pymysql

connection = pymysql.connect(
    host='localhost',
    user='python_app',
    password='python@123',
    database='camerin_student_2',
    port=3306
)
# print("Connection established successfully!")
# print(connection.__dict__)
try:
    # cursor = connection.cursor()
    with connection.cursor() as cursor:
 
        # query="""
        # alter table students
        #  add column phone varchar(20) not null default '111'
        #  """
        # query="""
        # alter table students
        # modify phone int default 11111;
        # """
        # cursor.execute(query)
        # connection.commit()
        # print("column added successfully")
        # query="desc students"
        # cursor.execute(query)
        # result=cursor.fetchall ()
        # for col in result:
        #     print(col)
        query="""
        alter table students
        rename column phone to contact_number;
        """
        cursor.execute(query)
        connection.commit()
        print("column added successfully")
        query="desc students"
        cursor.execute(query)
        result=cursor.fetchall ()
        for col in result:
            print(col)
        # cursor.execute("SELECT * FROM students")
        # records = cursor.fetchall()
        # # print (records)
        # for record in records:
        #     print(record)
        # data =('kochi',)

        # query = f"""select * from students 
        #         where city= 'kochi' """
        # cursor.execute(query)
        # result = cursor.fetchall()
        # for record in result:
        #     print(record)
        # print(result)


    # user_input="'OR '1'='1"
    # query = f"""select * from students
    # where s_name= '{user_input}'"""
    # print(query)

#     query= """
#     insert into students
#     values(%s, %s, %s, %s, %s)
#     """
#     values=(108,"Aleyas",'aleyas@gmail.com', 'kochi')
#     cursor.execute(query, values)
#     connection.commit()
except:
    print("something went wrong")
finally:
    connection.close()
    print("operation completed")