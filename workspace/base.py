from psycopg2._psycopg import cursor, connection
from workspace.doctors import doctor_workspace
from workspace.superusers import superuser_workspace
from workspace.patients import patient_workspace


def start_workspace(cur: cursor, conn: connection):
    while True:
        user_type: str = input(
            "Who are you? 1. Doctor; 2. Patient; 3. Superuser:"
        )
        if user_type == "1":
            doctor_workspace(cur, conn)
        elif user_type == "2":
            patient_workspace(cur, conn)
        elif user_type == "3":
            superuser_workspace(cur, conn)
        else:
            break

