from datetime import datetime
from controllers.exceptions.base import MyValidateError

from psycopg2._psycopg import cursor, connection


def validate_iin(iin: str) -> None:
    if len(iin) != 12:
        raise MyValidateError("IIN must have 12 symbols!")
    for letter in iin:
        try:
            int(letter)
        except ValueError:
            raise MyValidateError("IIN must have only numbers!")


def validate_date(date: str) -> bool:
    """Format: YYYY-MM-DD"""
    date_parts = date.split("-")
    if len(date_parts) != 3:
        raise MyValidateError("Separate symbols aren't correct!")
    try:
        year = int(date_parts[0])
        month = int(date_parts[1])
        day = int(date_parts[2])
    except ValueError:
        raise MyValidateError("Date must have only numbers and separator!")
    if not (year <= datetime.now().year):
        raise MyValidateError("Year isn't correct!")
    if not month <= 12:
        raise MyValidateError("Month isn't correct!")
    if not day <= 31:
        raise MyValidateError("Day isn't correct!")


def validate_time(time: str) -> None:
    """Format: HH:MM"""
    time_paths: list[str] = time.split(":")
    if len(time_paths) != 2:
        raise MyValidateError("Time format isn't correct")
    try:
        hours = int(time_paths[0])
        minutes = int(time_paths[1])
    except ValueError:
        raise MyValidateError("Time must have only numbers!")
    if hours < 0:
        raise MyValidateError("Hours isn't correct!")
    if minutes < 0 or minutes > 59:
        raise MyValidateError("Minutes isn't correct!")


def validate_now_date_and_time(date: str, time: str) -> None:
    validate_date(date)
    validate_time(time)
    now = datetime.now()
    now_date = now.date()
    now_time = now.time()

    date_paths: list[str] = date.split("-")
    year = int(date_paths[0])
    month = int(date_paths[1])
    day = int(date_paths[2])

    time_paths: list[str] = time.split(":")
    hours = int(time_paths[0])
    minutes = int(time_paths[1])

    # if year > now_date.year:
    #     return None
    # elif year < now_date.year:
    #     raise MyValidateError("Year• can't • be • in the past!")
    #
    # if month > now_date.month:
    #     return None
    # elif month < now_date.month:
    #     raise MyValidateError("Month can't be in the past!")
    #
    # if day > now_date.day:
    #     return None
    # elif day < now_date.day:
    #     raise MyValidateError("Day can't be in the past!")
    # if hours > now_time.hour:
    #     return None
    # elif hours < now_date.hour:
    #     raise MyValidateError("Hours can't be in the past!")
    #
    # if day > now_date.day:
    #     return None
    # elif day < now_date.day:
    #     raise MyValidateError("Day can't be in the past!")
    # if hours > now_time.hour:
    #     return None
    # elif hours < now_date.hour:
    #     raise MyValidateError("Hours can't be in the past!")
    # if minutes > now_time.minute:
    #     return None
    # elif minutes < now_date.minute:
    #     raise MyValidateError("Minutes can't be in the past!")


def validate_appoinment_time(
        cur: cursor, date: str, time: str, doctor_id: int) -> None:
    sql = """
    select * from appoinments
    where ap_date = %s and ap_time = %s and doctor = %s
    ;"""
    cur.execute(sql, (date, time, doctor_id))
    obj = cur.fetchall()
    if obj:
        raise MyValidateError("This time is already booked!")
