from psycopg2._psycopg import cursor, connection


def to_dict(obj) -> dict:
    # return {
    #     "id": obj[0],
    #     "login": obj[1],
    #     "password": obj[2]
    # }
    return dict(obj)


def get_first(cur: cursor) -> list:
    sql = """
        select * from superusers
        order by id limit 1;
    """
    cur.execute(sql)
    return cur.fetchone()


def create(cur: cursor, conn: connection, login: str, password: str):
    sql = """
        insert into superusers(login, password)
        values (%s, %s);
    """
    cur.execute(sql, (login, password))
    conn.commit()


def get_by_login_and_password(cur: cursor, login: str, password: str) -> dict:
    sql = """
        select * from superusers
        where login = %s and password = %s;
        """
    cur.execute(sql, (login, password))
    superuser = cur.fetchone()
    if superuser:
        return to_dict(superuser)
    return None
