from psycopg2._psycopg import cursor, connection


def to_dict(obj) -> dict:
    # return {
    #     "id": obj[0],
    #     "name": obj[1]
    # }
    return dict(obj)


def create(
        cur: cursor,
        conn: connection,
        name: str) -> None:
    sql = f""" insert into specializations(name) values (%s);"""
    cur.execute(sql, (name, ))
    conn.commit()


def create_with_inputs(cur: cursor, conn: connection) -> None:
    name = input("name specialization: ")
    create(cur, conn, name)


def all(cur: cursor) -> list[dict]:
    """Return all specializations!"""
    sql = """select * from specializations;"""
    cur.execute(sql)
    objs: list[tuple] = cur.fetchall()
    response: list[dict] = []
    for obj in objs:
        response.append(to_dict(obj))
    return response


def get_by_id(cur: cursor, id: str) -> dict:
    sql = """
    select * from specializations
    where id = %s;
    """
    obj = cur.execute(sql, (id,))
    if obj:
        return to_dict(cur.fetchone())
    return None

