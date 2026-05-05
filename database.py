import os
import psycopg2

def get_connection():
    return psycopg2.connect(os.environ["postgresql://postgres:HmABJHJaHJLadzMGIyvIZhtazTEpZpVq@postgres.railway.internal:5432/railway"])

