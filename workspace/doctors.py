from pprint import pprint

from psycopg2._psycopg import cursor, connection

from controllers import doctors, appointments
from controllers.appointments import get_all_appointments_by_id


def doctor_workspace(cur: cursor, conn: connection) -> None:
    while True:
        try:
            id_ = int(input("enter doctor's id: "))
            # pprint(get_all_appointments_by_id(cur, id_))
        except ValueError:
            print("Please enter only numbers!")
        auth_doctors = doctors.get_by_id(cur, id_)
        if auth_doctors:
            print(f"Welcome {auth_doctors['fio']}!\n")
            break
    appois_today: list[dict] = appointments.get_today_by_doctor(cur, auth_doctors['id'])
    if len(appois_today) == 0:
        print("Today you dont have any appointments")
    else:
        pprint(appois_today)
        for app in appois_today:
            for key in app.keys():
                print(f'{key}: {app[key]}')
            print()

