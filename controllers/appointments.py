from datetime import datetime, date, time

from psycopg2._psycopg import cursor, connection

from controllers import validators


def to_dict(obj) -> dict:
    obj_dict = dict(obj)
    for key in obj_dict:
        value = obj_dict[key]
        if isinstance(value, date):
            obj_dict[key] = f"{value.day}-{value.month}-{value.year}"
        elif isinstance(value, time):
            obj_dict[key] = f"{value.hour}:{value.minute}"
    return obj_dict


def get_by_name(cur: cursor, appointment: str) -> int:
    sql = """
        select id from appointments
        where name = %s;
        """
    cur.execute(sql, (appointment, ))
    id = cur.fetchone()
    print(id)
    if id:
        return id[0]
    return None


def create(
        cur: cursor,
        conn: connection,
        patient: int,
        doctor: int,
        ap_date: str,
        ap_time: str
    ) -> None:
    validators.validate_now_date_and_time(ap_date, ap_time)
    validators.validate_appoinment_time(ap_date, ap_time, doctor)
    sql = f"""
        insert into appointments(patient, doctor, ap_date, ap_time) 
        values (%s, %s, %s, %s);
    """
    cur.execute(sql, (patient, doctor, ap_date, ap_time))
    conn.commit()


def create_with_inputs(cur: cursor, conn: connection) -> None:
    patient = input("patient id: ")
    doctor = input("doctor id: ")
    ap_date = input("ap_date (YYYY-MM-DD): ")
    ap_time = input("patient (HH:MM): ")

    create(cur, conn, patient, doctor, ap_date, ap_time)


def all(cur):
    """Return all appointments!"""
    sql = """select * from appointments;"""
    cur.execute(sql)
    objs: list[tuple] = cur.fetchall()
    response: list[dict] = []
    for obj in objs:
        response.append(to_dict(obj))
    return response


def get_by_id(cur: cursor, id) -> dict:
    sql = """
    select * from appointments
    where id = %s;
    """
    obj = cur.execute(sql, (id, ))
    if obj:
        return to_dict(cur.fetchone())
    return None


def get_all_appointments_by_id(cur: cursor, doctor_id: str) -> dict:
    sql = """
    select * from appointments
    where doctor = %s;
    """
    cur.execute(sql, (doctor_id, ))
    objs = cur.fetchall()
    response: list[dict] = []
    for obj in objs:
        response.append(to_dict(obj))
    return response


def get_today_by_doctor(cur: cursor, doctor_id: int) -> list[dict]:
    now = datetime.now()
    now_str: str = f"{now.year}-{now.month}-{now.day}"
    sql = """
    select 
        a.ap_date, a.ap_time,
        p.iin as patient_iin,
        p.fio as patient_fio,
        p.birthdate as patient_birthdate,
        d.fio as doctor_fio,
        s.name as doctor_specialization,
        d.room_number
    from appointments a
    left join doctors d on d.id = a.doctor
    left join patients p on p.id = a.patient
    left join specializations s on s.id = d.special
    where doctor = %s and ap_date = %s
    order by a.ap_date, a.ap_time;
    """
    cur.execute(sql, (doctor_id, now_str))
    apois = cur.fetchall()
    return [to_dict(i) for i in apois]
