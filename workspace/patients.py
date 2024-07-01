from pprint import pprint

from psycopg2._psycopg import cursor, connection

from controllers import patients, doctors, appointments
from controllers.exceptions.base import MyValidateError


def patient_workspace(cur: cursor, conn: connection):
    while True:
        try:
            id_ = int(input("enter patient's id: "))
        except ValueError:
            print("Please enter only numbers!")
        auth_patients = patients.get_by_id(cur, id_)
        if auth_patients:
            print(f"Welcome {auth_patients['fio']}!\n")
            break
    while True:
        try:
            input_text = (
                "What do you want?\n"
                "1. Create an appointment\n"
                "2. Show all appointments\n"
                "3. Show all doctors\n"
                "-1. Exit\n"
            )
            user_choose: str = input(input_text)
            if user_choose == "-1":
                return None
            elif user_choose == "1":
                appointments.get_by_id(cur, id_)
                print("choose a doctor: ")
                pprint(doctors.all(cur))
                choice_doctor = input("choose a doctor: ")
                pprint(appointments.get_all_appointments_by_id(cur, choice_doctor))
                patient_date = input("choose a date (YYYY-MM-DD): ")
                patient_time = input("choose time (HH:MM): ")
                try:
                    appointments.create(cur, conn,
                                        auth_patients["id"],
                                        choice_doctor,
                                        patient_date,
                                        patient_time
                                        )
                except MyValidateError as e:
                    print(e.message)
            elif user_choose == "2":
                pprint(appointments.all(cur))
            elif user_choose == "3":
                pprint(doctors.all(cur))

        except MyValidateError as e:
            print(e.message)
