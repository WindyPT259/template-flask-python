from flask import render_template, jsonify, request
from src.models.db import db
from src.models.users import UserApp
from sqlalchemy import text, exc
import re


def home():
    return render_template("home.html")


def get_list():
    try:
        query = text(
            "SELECT column_name FROM information_schema.columns WHERE table_name = 'user_app'"
        )
        connection = db.session.connection()

        columns = db.session.execute(query)
        column_names = [column[0] for column in columns]
        users = UserApp.query.all()
        users_data = []
        for user in users:
            user_data = {}
            for column_name in column_names:
                user_data[column_name] = getattr(user, column_name)
            users_data.append(user_data)
        connection.close()

        results = {
            "status_code": 200,
            "success": True,
            "data": {"users": users_data, "header": column_names},
        }
    except exc.ProgrammingError as e:
        pattern = re.compile(r"\((\d+), \"(.+?)\"\)")
        match = pattern.search(str(e)).group(2)
        results = {"status_code": 400, "success": False, "message": match}
    except Exception:
        pattern = re.compile(r"\((\d+), \"(.+?)\"\)")
        match = pattern.search(str(e)).group(2)
        results = {"status_code": 500, "success": False, "message": match}

    return jsonify(results)
