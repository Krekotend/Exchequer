import psycopg2
import datetime
from config_a import load_config


def join_base():
    try:
        connection = psycopg2.connect(host=load_config().db.host, user='krekotend',
                                      password=load_config().db.password, database=load_config().db.db_name)
        connection.autocommit = True

        return connection

    except Exception as ex:
        print('This is ERROR ', ex)


def write_users_table(name: str, telega_id: int):
    with join_base().cursor() as cursor:
        SQL = 'SELECT user_name FROM users_a WHERE tg_id = %s;'
        cursor.execute(SQL, (telega_id,))
        if cursor.fetchone() == None:
            SQL = 'INSERT INTO users_a (user_name,tg_id) VALUES (%s,%s);'
            value = (name, telega_id)
            cursor.execute(SQL, value)


def write_data_table(price: float, coment: str, category: int, tg_id: int):
    with join_base().cursor() as cursor:
        today = datetime.date.today()
        rows = (price, coment, category, tg_id, today)
        SQL = 'INSERT INTO notes (price,coment,fk_posts_categories,fk_tg_id,recording_date) VALUES (%s,%s,%s,%s,%s);'
        cursor.execute(SQL, rows)


def show_categories_table():
    with join_base().cursor() as cursor:
        caegories = []
        SQL = 'SELECT * FROM categories;'
        cursor.execute(SQL)
        for item in cursor.fetchall():
            caegories.append([int(item[0]),item[1]])
        return sorted(caegories)


def shows_history_day(day: str, tg_id: int):
    with join_base().cursor() as cursor:
        item_day = []
        SQL_h = 'SELECT price,coment FROM notes WHERE recording_date = %s and fk_tg_id = %s;'
        cursor.execute(SQL_h, (day, tg_id))
        for item in cursor.fetchall():
            item_day.append(f'{item[0]} - {item[1]}')
        return item_day


def shows_history_months(mounth: int, tg_id: int):
    with join_base().cursor() as cursor:
        item_day = []
        SQL_h = 'SELECT price,coment FROM notes WHERE EXTRACT(MONTH FROM recording_date) = %s and fk_tg_id = %s;'
        cursor.execute(SQL_h, (mounth, tg_id))
        for item in cursor.fetchall():
            item_day.append(f'{item[0]} - {item[1]}')
        return item_day


def shows_last_item(tg_id):
    with join_base().cursor() as cursor:
        SQL_l = 'SELECT price,coment  FROM notes WHERE fk_tg_id = %s ORDER BY id DESC LIMIT 3;'
        cursor.execute(SQL_l, (tg_id,))
        return cursor.fetchall()


if __name__ == 'main':
    pass
