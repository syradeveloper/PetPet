import sqlite3
from datetime import datetime
import random
DATABASE_NAME = 'PetPet.db'

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            hunger INTEGER DEFAULT 50,
            cleanliness INTEGER DEFAULT 50,
            happiness INTEGER DEFAULT 50,
            energy INTEGER DEFAULT 100,
            intelligence INTEGER DEFAULT 50,
            strength INTEGER DEFAULT 50,
            stamina INTEGER DEFAULT 50,
            agility INTEGER DEFAULT 50,
            flexibility INTEGER DEFAULT 50,
            last_fed TEXT,
            last_cleaned TEXT,
            last_played TEXT,
            last_trained TEXT,
            last_slept TEXT,
            personality TEXT,
            favorite_food TEXT,
            favorite_activity TEXT
        )
    ''')
    conn.commit()
    conn.close()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_pet(user_id: int):
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pets WHERE user_id = ?', (user_id,))
    pet = cursor.fetchone()
    conn.close()
    return pet

def create_pet(user_id: int, name: str):
    personality = random.choice(['Игривый', 'Ленивый', 'Любопытный', 'Дружелюбный', 'Застенчивый'])
    favorite_food = random.choice(['Яблоко', 'Морковь', 'Банан', 'Орехи', 'Ягоды'])
    favorite_activity = random.choice(['Бег', 'Плавание', 'Прыжки', 'Игра в мяч', 'Головоломки'])

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pets (user_id, name, personality, favorite_food, favorite_activity)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, name, personality, favorite_food, favorite_activity))
    conn.commit()
    conn.close()

def update_pet(user_id: int, **kwargs):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    set_clause = ', '.join(f'{k} = ?' for k in kwargs)
    query = f'UPDATE pets SET {set_clause} WHERE user_id = ?'
    cursor.execute(query, tuple(kwargs.values()) + (user_id,))
    conn.commit()
    conn.close()

def get_all_pets():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pets')
    pets = cursor.fetchall()
    conn.close()
    return pets