import psycopg2
#CONNECTIGN TO DATABASE ADN CREATING TABLE
def connector():
    conn = psycopg2.connect("dbname=BookaD user=postgres password=sagar123")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS BookaD (id serial, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert_data(title,author, year, isbn):
    conn = psycopg2.connect("dbname=BookaD user=postgres password=sagar123")
    cur=conn.cursor()
    cur.execute("INSERT INTO BookaD VALUES (DEFAULT,%s,%s,%s,%s)",(title, author, year, isbn))
    conn.commit()
    conn.close()
def view_data():
    conn = psycopg2.connect("dbname=BookaD user=postgres password=sagar123")
    cur=conn.cursor()
    cur.execute("SELECT * FROM BookaD")
    rows=cur.fetchall()
    conn.close()
    return rows
def search_data(isbn):
    conn = psycopg2.connect("dbname=BookaD user=postgres password=sagar123")
    cur=conn.cursor()
    cur.execute("SELECT * FROM BookaD WHERE isbn= %s ", (isbn,))
    rows=cur.fetchall()
    conn.close()
    return rows


def delete_data(id):
    conn = psycopg2.connect("dbname=BookaD user=postgres password=sagar123")
    cur=conn.cursor()
    cur.execute("DELETE FROM BookaD WHERE Id =%s" ,(id,))
    conn.commit()
    conn.close()
def update_data(id,title, author,year,isbn):
    conn = psycopg2.connect("dbname=BookaD user=postgres password=sagar123")
    cur=conn.cursor()
    cur.execute("UPDATE BookaD SET title=%s,author =%s, year=%s, isbn=%s WHERE ID=%s" ,(title,author,year,isbn,id))
    conn.commit()
    conn.close()

#update_data(2,"The Hero","Ghimire Sagar", 1997, 113665)

#delete_data(3)


#insert_data("The Summer Love","Kafle",2000,113667)
#print(view_data())
#print(search_data(2))
connector()






