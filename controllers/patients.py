from datetime import datetime

from psycopg2._psycopg import cursor, connection
from controllers import validators


def to_dict(obj) -> dict:
    return dict(obj)


def create(
        cur: cursor,
        conn: connection,
        fio: str,
        iin: str,
        birthdate: str
    ) -> None:
    validators.validate_iin(iin)
    validators.validate_date(birthdate)
    sql = f"""
        insert into patients(fio, iin, birthdate) values (
            '{fio}', '{iin}', '{birthdate}'
    );
    """
    cur.execute(sql, (fio, iin, birthdate))
    conn.commit()


def create_with_inputs(
        cur: cursor,
        conn: connection) -> None:
    fio = input("fio: ")
    iin = input("iin: ")
    birthdate = input("birthdate (YYYY-MM-DD): ")
    # birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
    create(cur, conn, fio, iin, birthdate)


def all(cur: cursor) -> list[dict]:
    """Return all patients!"""
    sql = """select * from patients;"""
    cur.execute(sql)
    objs: list[tuple] = cur.fetchall()
    response: list[dict] = []
    for obj in objs:
        response.append(to_dict(obj))
    return response


def get_by_id(cur: cursor, id):
    sql = """
    select * from patients
    where id = %s;
    """
    cur.execute(sql, (id, ))
    obj = cur.fetchone()
    if obj:
        return to_dict(obj)
    return None
