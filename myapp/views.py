from django.core.exceptions import ImproperlyConfigured
from django.views.generic import ListView
from django.shortcuts import render
from .models import score1
import json
import mysql.connector


def load_secrets():
    try:
        with open('secrets.json', 'r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        raise ImproperlyConfigured("Couldn't find secret.json file.")

secrets = load_secrets()


def get_secret(setting):
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured(f"{setting} Set the environment variable.")


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password=get_secret("DB_PW"),
        database='lecture',
        port=3306
    )

def index(request):
    return render(request, 'index.html')

def vulnerable(request):
    result = []
    if request.method == 'POST':
        name = request.POST.get('name', '')
        dbquery = f"SELECT id, name, score FROM myapp_score1 WHERE name = '{name}'"

        try:
            dbconnection = get_db_connection()
            with dbconnection.cursor() as curs:
                curs.execute(dbquery)
                result = curs.fetchall()
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            dbconnection.close()

    return render(request, 'vulnerable.html', {'result': result})


def secure(request):
    global dbconnection
    result = []
    if request.method == 'POST':
        name = request.POST.get('name', '')

        try:
            dbconnection = get_db_connection()
            with dbconnection.cursor() as curs:
                dbquery = "SELECT id, name, score FROM myapp_score1 WHERE name = %s"
                curs.execute(dbquery, (name,))
                result = curs.fetchall()
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            dbconnection.close()

    return render(request, 'secure.html', {'result': result})
