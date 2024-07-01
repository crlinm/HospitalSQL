from pprint import pprint

from psycopg2._psycopg import cursor, connection

from controllers import patients, specializations, appointments, doctors
from controllers.exceptions.base import MyValidateError
from controllers.superusers import get_by_login_and_password


def superuser_workspace(cur: cursor, conn: connection) -> None:
    print("i am superuser!")
    attempts: int = 5
    while attempts > 0:
        login: str = input("login: ")
        password: str = input("password: ")
        user = get_by_login_and_password(cur, login, password)
        if user:
            print(f"welcome {user['login']}")
            break
        else:
            print(f"superuser {login} isn't found")
        attempts -= 1
    while True:
        try:
            input_text = (
                "What do you want?\n"
                "1. Show current appointment\n"
                "2. Show all appointments\n"
                "3. Create an appointment\n"
                "4. Show current doctor\n"
                "5. Show current patient\n"
                "6. Show current specialization\n"
                "7. Show all specialization\n"
                "8. Create specialization\n"
                "9. Show all doctors\n"
                "10. Show all patients\n"
                "11. Create doctor\n"
                "12. Create patient\n"
                "-1. Exit\n"
            )
            user_choose: str = input(input_text)
            if user_choose == "-1":
                return None
            elif user_choose == "1":
                id = input("id: ")
                appointments.get_by_id(cur, id)
            elif user_choose == "2":
                pprint(appointments.all(cur))
            elif user_choose == "3":
                appointments.create_with_inputs(cur, conn)
            elif user_choose == "4":
                id = input("id: ")
                doctors.get_by_id(cur, id)
            elif user_choose == "5":
                id = input("id: ")
                patients.get_by_id(cur, id)
            elif user_choose == "6":
                id = input("id: ")
                specializations.get_by_id(cur, id)
            elif user_choose == "7":
                pprint(specializations.all(cur))
            elif user_choose == "8":
                specializations.create_with_inputs(cur, conn)
            elif user_choose == "9":
                pprint(doctors.all(cur))
            elif user_choose == "10":
                pprint(patients.all(cur))
            elif user_choose == "11":
                doctors.create_with_inputs(cur, conn)
            elif user_choose == "12":
                patients.create_with_inputs(cur, conn)

        except MyValidateError as e:
            print(e.message)

