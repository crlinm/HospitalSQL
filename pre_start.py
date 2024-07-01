from psycopg2._psycopg import cursor, connection
from controllers import superusers
from controllers import doctors


def start_up(cur: cursor, conn: connection):

    sql = """
        create table if not exists specializations (
            id serial primary key,
            name varchar(255)
        );
        create table if not exists doctors (
        id serial primary key,
        fio varchar(255),
        special integer references specializations(id),
        money_per_hour float check(money_per_hour > 0) not null,
        room_number integer
        );
        create table if not exists patients (
            id serial primary key,
            fio varchar(255),
            iin varchar(12) check(length(iin) = 12),
            birthdate date
        );
        create table if not exists superusers (
            id serial primary key,
            login varchar(100) not null,
            password varchar(100) not null
        );
        create table if not exists appointments (
            id serial primary key,
            patient integer references patients(id) not null,
            doctor integer references doctors(id) not null,
            ap_date date not null,
            ap_time time not null,
            is_done boolean default(false)
        );
    """
    cur.execute(sql)
    conn.commit()
    superusers_from_db = superusers.get_first(cur)
    if not superusers_from_db:
        superusers.create(cur, conn, "root", "qwerty")
    print(superusers_from_db)
