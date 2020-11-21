import psycopg2

if __name__ == '__main__':
    conn = psycopg2.connect("host=127.0.0.1 dbname=demo user=demo password=demo port=6432")
    cur = conn.cursor()

    cur.execute("SELECT * FROM articles;")
    rows = cur.fetchall()
    for row in rows:
        print(row[0])
        print(row[1])
        print(row[2])
        print()

    cur.close()
    conn.close()
