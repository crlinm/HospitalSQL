from datetime import datetime

from psycopg2._psycopg import cursor, connection


def to_dict(obj) -> dict:
    return dict(obj)


def get_by_name(cur: cursor, specialization: str) -> int:
    sql = """
        select id from specializations
        where name = %s;
        """
    cur.execute(sql, (specialization, ))
    id = cur.fetchone()
    if id:
        return id[0]
    return None


def create(
        cur: cursor,
        conn: connection,
        fio: str,
        special: int,
        money_per_hour: float,
        room_number: int
    ) -> None:
    sql = f"""
        insert into doctors(fio, special, money_per_hour, room_number) 
        values (%s, %s, %s, %s);
    """
    cur.execute(sql, (fio, special, money_per_hour, room_number))
    conn.commit()


def create_with_inputs(cur: cursor, conn: connection) -> None:
    fio = input("fio: ")
    special = get_by_name(cur, input("specialization: "))
    money_per_hour = float(input("money_per_hour: "))
    room_number = int(input("room_number: "))
    create(cur, conn, fio, special, money_per_hour, room_number)


def all(cur):
    """Return all doctors!"""
    sql = """select * from doctors;"""
    cur.execute(sql)
    objs: list[tuple] = cur.fetchall()
    response: list[dict] = []
    for obj in objs:
        response.append(to_dict(obj))
    return response


def get_by_id(cur: cursor, id_) -> dict:
    sql = """
    select * from doctors
    where id = %s;
    """
    cur.execute(sql, (id_, ))
    obj = cur.fetchone()
    if obj:
        return to_dict(obj)
    return None

