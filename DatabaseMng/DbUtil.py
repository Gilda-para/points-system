import pymysql
import json


print('this is Dbutil.py')
def connect():
    conn = pymysql.connect(host='localhost',
                           user='research',
                           password='123456',
                           db='world',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    return conn, cursor


def get_list_sql(table_name, records):
    columns = ','.join(['`' + x + '`' for x in records[0].keys()])
    sql = """insert into %s(%s) values """ % (table_name, columns)
    for x in records:
        base_sql = '('
        for y in x.values():
            if type(y) == str:
                base_sql += '"' + y + '",'
            else:
                base_sql += str(y) + ','
        base_sql = base_sql[0:len(base_sql) - 1] + '),'
        sql += base_sql
    sql = sql[0:len(sql) - 1]
    return sql
    # to save a list of dict to db


def get_create_table_sql(table_name, record):
    sql = """create table `%s` (""" % (table_name)
    for x, y in record.items():
        if type(y) == int:
            schema_type = 'bigint'
        elif type(y) == float:
            schema_type = 'decimal(30,10)'
        else:
            schema_type = 'varchar(300)'
        sql_item = """`%s` %s default null,""" % (x, schema_type)
        sql += sql_item
    sql = sql[0:len(sql) - 1] + ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4'
    return sql


# save the records to database
def save_database_records(table_name, records):
    conn, cursor = connect()
    create_table_sql = get_create_table_sql(table_name, records[0])
    cursor.execute(create_table_sql)
    sql = get_list_sql(table_name, records)
    cursor.execute(sql)
    conn.commit()


def save_records(table_name, records):
    conn, cursor = connect()
    sql = get_list_sql(table_name, records)
    cursor.execute(sql)
    conn.commit()


def parse_value(item):
    if type(item) == str:
        item = "'" + item + "'"
    return item


def get_sql(table_name, record):
    columns = ','.join(['`' + x + '`' for x in record.keys()])
    base_values = ''
    for x in record.values():
        if type(x) == str:
            base_values += '"' + x + '",'
        elif x == None:
            base_values += '""' + ','
        elif type(x) == list:
            base_values += "'" + json.dumps(x) + "'" + ","
        elif type(x) == dict:
            base_values += "'" + json.dumps(x) + "'" + ","
        else:
            base_values += str(x) + ","
    base_values = base_values[0:len(base_values) - 1]
    sql = """
        insert into %s(%s) values(%s)
    """ % (table_name, columns, base_values)
    return sql


def get_base_sql(table_name, record):
    columns = ','.join(['`' + x + '`' for x in record.keys()])
    sql = "insert into " + table_name + "(" + columns + ")" + "values(%s)"
    return sql
