import pymysql

connection = pymysql.connect(
    host='localhost',
    user='python_app',
    password='python@123',
    database='camerin_student_2',
    port=3306
)

try:
    with connection.cursor() as cursor:
        update_query = """
        UPDATE course
        SET course_name = %s
        WHERE course_id = %s
        """
        cursor.execute(update_query, ('DSML with Gen AI', 3))
        connection.commit()

        print("Course updated successfully\n")
        select_query = """
        SELECT *
        FROM course
        """

        cursor.execute(select_query)
        courses = cursor.fetchall()
        print("=== Updated Course List ===")
        for course in courses:
            print(course)
except Exception as e:
    print(f"Error: {e}")
finally:
    connection.close()
    print("\nOperation completed")