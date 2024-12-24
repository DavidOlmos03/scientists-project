import psycopg2
from app.config import config

def get_db_connection():
    connection = psycopg2.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD
    )
    return connection

def get_all_scientists():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM scientists')
    results = cur.fetchall()
    cur.close()
    conn.close()
    return [{'id': r[0], 'name': r[1], 'birthday': r[2], 'description': r[3], 'area': r[4]} for r in results]

def get_scientist_by_id(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM scientists WHERE id = %s', (id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def create_scientist(name, birthday, description, area):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO scientists (name, birthday, description, area) VALUES (%s, %s, %s, %s) RETURNING id',
        (name, birthday, description, area)
    )
    scientist_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return scientist_id

def update_scientist(id, name, birthday, description, area):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE scientists SET name = %s, birthday = %s, description = %s, area = %s WHERE id = %s',
        (name, birthday, description, area, id)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_scientist(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM scientists WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
