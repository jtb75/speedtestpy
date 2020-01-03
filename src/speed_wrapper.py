#!/usr/local/bin/python
#
import subprocess
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from datetime import datetime
############################################################################3
def create_db():
    try:
        conn = psycopg2.connect(user = "demopostgresadmin",
                                password = "demopostgrespwd",
                                host = "postgres",
                                dbname = "postgres")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    except:
        print ("I am unable to connect to the database")
    cur = conn.cursor()
    cur.execute("""SELECT datname from pg_database""")
    name_Database = "speeddb"
    rows = cur.fetchall()
    dbexists = 0
    for row in rows:
        if row[0] == name_Database:
            dbexists = 1
    if not dbexists:
        sqlCreateDatabase = "create database "+name_Database+";"
        cur.execute(sqlCreateDatabase)
    conn.close()
############################################################################3

############################################################################3
def create_tables():
    try:
        conn = psycopg2.connect(user = "demopostgresadmin",
                                password = "demopostgrespwd",
                                host = "postgres",
                                dbname = "speeddb")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    except:
        print ("I am unable to connect to the database")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';""")
    name_Table = "speed_tbl"
    rows = cur.fetchall()
    tblexists = 0
    for row in rows:
        if row[1] == name_Table:
            tblexists = 1
    if not tblexists:
        sql = "create table speed_tbl (id serial, host varchar(128), distance numeric(8, 4), ping numeric(8, 4), upload numeric(8, 4), download numeric(8, 4), ts timestamp)"
        cur.execute(sql)
        conn.commit()
    conn.close()
############################################################################3

############################################################################3
def run_speed_test():
    result = subprocess.check_output(['/usr/local/bin/speedtest-cli'])
    result = result.decode('utf-8')
    result = result.split('\n')
    result[4] = result[4].split('Hosted by ', 1)[-1]
    (host, remainder) = result[4].split(' [')
    (distance, pingspeed) = remainder.split(']: ')
    distance = distance.split()
    pingspeed = pingspeed.split()
    download = result[6].split()
    download.pop(0)
    upload = result[8].split()
    upload.pop(0)
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    dt_object = datetime.fromtimestamp(timestamp)
    try:
        conn = psycopg2.connect(user = "demopostgresadmin",
                                password = "demopostgrespwd",
                                host = "postgres",
                                dbname = "speeddb")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    except:
        print ("I am unable to connect to the database")
    cur = conn.cursor()
    cur.execute("insert into speed_tbl(host, distance, ping, upload, download, ts) values (%s, %s, %s, %s, %s, %s)", (host, distance[0], pingspeed[0], upload[0], download[0], dt_object))
    conn.commit()
    conn.close()
############################################################################3



create_db()
create_tables()
run_speed_test()
