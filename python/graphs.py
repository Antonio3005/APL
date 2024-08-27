from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
import os
import io
from collections import Counter
import matplotlib.pyplot as plt

SECRET_KEY = os.environ['SECRET_KEY']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
db_host = os.environ['DB_HOST']

engine = create_engine(f'mysql://{db_user}:{db_password}@{db_host}/{db_name}')
metadata = MetaData()

populars = Table('research',  metadata,
            Column('id', Integer, primary_key=True),
            Column('city_from', String(255), unique=True, nullable=False),
            Column('city_to', String(255), nullable=False))

metadata.create_all(engine)

def graph():
    conn = engine.connect()
    query = select(populars)
    result = conn.execute(query)
    data = result.fetchall()

    conn.close()

    routes = []

    if data:
        for d in data:
            route = (d[1],d[2])
            routes.append(route)

        # Conto le occorrenze di ciascun tragitto unico
        route_counter = Counter(routes)

        route_labels = [f"{from_city} -> {to_city}" for from_city, to_city in route_counter.keys()]
        route_values = list(route_counter.values())

        plt.figure(figsize=(12, 8))
        plt.barh(route_labels, route_values, color='skyblue')

        plt.xlabel('Numero di Ricerche')
        plt.ylabel('Route')
        plt.title('Mete più Ricercate (Andata e Ritorno)')

        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()

        return buf
