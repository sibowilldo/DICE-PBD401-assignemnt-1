import json
import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS
from werkzeug.exceptions import Forbidden, Unauthorized, BadRequest

from auth.auth import AuthError, requires_auth
from database.models import Vacancy, setup_db, Status

load_dotenv('.env')

app = Flask(__name__, instance_relative_config=True)

setup_db(app)

CORS(app, resources={r"/api/*": {"origins": "*"}})

api_route = os.getenv("API_URL", "/api/v1")

'''
 ================= Statuses =====================
'''


@app.route(f"{api_route}/home", methods=['GET'])
def home():
    try:
        vacancies = Vacancy.query.all()
        vacancies = list(map(lambda vacancy: vacancy.short(), vacancies))
        return jsonify({"vacancies": vacancies}), 200
    except Exception as ex:
        print(ex)
        return jsonify({
            "success": False,
        }), 500


@app.route(f"{api_route}/statuses", methods=['GET'])
def statuses_index():
    try:
        statuses = Status.query.all()
        statuses = list(map(lambda status: status.long(), statuses))
        return jsonify({"statuses": statuses}), 200
    except Exception as ex:
        print(ex)
        return jsonify({
            "success": False,
        }), 500


@app.route(f"{api_route}/statuses", methods=['POST'])
@requires_auth('post:status.store')
def status_store(payload):
    try:
        req = request.get_json()
        status = Status()

        status.model_type = req.get("model_type", "")
        status.name = req.get("name", "")
        status.description = req.get("description", "")
        status.priority = req.get("priority", None)

        status.insert()
        return jsonify({
            "success": True,
            "message": "Your status was saved!",
            "status": status.long()
        }), 200
    except Forbidden or Unauthorized or BadRequest:
        raise AuthError


@app.route(f"{api_route}/statuses/<int:statuses_id>", methods=['GET'])
@requires_auth('read:status.view')
def status_show(payload, status_id):
    try:
        status = Status.query.filter(Status.id == status_id).first_or_404()

        status.update()
        return jsonify({
            "success": True,
            "status": status.long()
        }), 200
    except Forbidden or Unauthorized or BadRequest:
        raise AuthError


@app.route(f"{api_route}/statuses/<int:statuses_id>", methods=['PUT'])
@requires_auth('put:status.update')
def status_update(payload, status_id):
    try:
        req = request.get_json()
        status = Status.query.filter(Status.id == status_id).first_or_404()

        status.model_type = req.get("model_type")
        status.name = req.get("name")
        status.description = req.get("description")
        status.priority = req.get("priority", None)

        status.update()
        return jsonify({
            "success": True,
            "status": status
        }), 200
    except Forbidden or Unauthorized or BadRequest:
        raise AuthError


@app.route(f"{api_route}/statuses/<int:statuses_id>", methods=['DELETE'])
@requires_auth('delete:status.destroy')
def status_destroy(payload, vacancy_id):
    try:
        vacancy = Vacancy.query.filter(Vacancy.id == vacancy_id).first_or_404()
        vacancy.delete()
        return jsonify({
            "success": True,
            "delete": vacancy_id
        }), 200
    except Forbidden or Unauthorized or BadRequest:
        raise AuthError


'''
 ================= Vacancies =====================
'''


@app.route(f"{api_route}/vacancies", methods=['GET'])
def vacancies_index():
    try:
        vacancies = Vacancy.query.all()
        vacancies = list(map(lambda vacancy: vacancy.long(), vacancies))
        return jsonify({"vacancies": vacancies}), 200
    except Exception as ex:
        print(ex)
        return jsonify({
            "success": False,
        }), 500


@app.route(f"{api_route}/vacancies", methods=['POST'])
@requires_auth('post:vacancy.store')
def vacancy_store(payload):
    try:
        req = request.get_json()
        vacancy = Vacancy()

        vacancy.title = req.get("title", "")
        vacancy.description = req.get("description", "")
        vacancy.department = req.get("department", "")
        vacancy.location = req.get("location", "")
        vacancy.expires_at = req.get("expires_at", "")
        vacancy.user_id = req.get("user_id", "")
        vacancy.category_id = req.get("category_id", "")
        vacancy.type_id = req.get("type_id", "")

        vacancy.insert()
        return jsonify({
            "success": True,
            "message": "Your vacancy was published!",
            "vacancy": vacancy.long()
        }), 200
    except Forbidden or Unauthorized or BadRequest:
        raise AuthError


@app.route(f"{api_route}/vacancies/<int:vacancy_id>", methods=['GET'])
@requires_auth('read:vacancy.view')
def vacancy_show(payload, vacancy_id):
    try:
        vacancy = Vacancy.query.filter(Vacancy.id == vacancy_id).first_or_404()

        vacancy.update()
        return jsonify({
            "success": True,
            "vacancy": vacancy.long()
        }), 200
    except Forbidden or Unauthorized or BadRequest:
        raise AuthError


@app.route(f"{api_route}/vacancies/<int:vacancy_id>", methods=['PUT'])
@requires_auth('put:vacancy.update')
def vacancy_update(payload, vacancy_id):
    try:
        req = request.get_json()
        vacancy = Vacancy.query.filter(Vacancy.id == vacancy_id).first_or_404()

        vacancy.title = req.get("title")
        vacancy.description = req.get("description")
        vacancy.department = req.get("department")
        vacancy.location = req.get("location")
        vacancy.expires_at = req.get("expires_at")
        vacancy.category_id = req.get("category_id")
        vacancy.type_id = req.get("type_id")

        vacancy.update()
        return jsonify({
            "success": True,
            "vacancy": vacancy
        }), 200
    except Forbidden or Unauthorized or BadRequest:
        raise AuthError


@app.route(f"{api_route}/vacancies/<int:vacancy_id>", methods=['DELETE'])
@requires_auth('delete:vacancy.destroy')
def vacancy_destroy(payload, vacancy_id):
    try:
        vacancy = Vacancy.query.filter(Vacancy.id == vacancy_id).first_or_404()
        vacancy.delete()
        return jsonify({
            "success": True,
            "delete": vacancy_id
        }), 200
    except Forbidden or Unauthorized or BadRequest:
        raise AuthError


@app.route(f"{api_route}/vacancies/<int:vacancy_id>/apply", methods=['POST'])
@requires_auth('post:vacancy.apply')
def vacancy_apply(payload, vacancy_id):
    try:
        vacancy = None  # ToDo: get this using vacancy_id
        applicant = None  # ToDo: get this using applicant_id/logged-in user_id
        #  ToDo: link vacancy and applicant to applications table
        return jsonify({
            "success": True,
            "message": "Your application was submitted. Good Luck!",
            "vacancy": vacancy,
            "applicant": applicant,
        }), 200
    except Forbidden or Unauthorized or BadRequest:
        raise AuthError


@app.route(f"{api_route}/application/<int:application_id>/destroy", methods=['POST'])
@requires_auth('delete:application.withdraw')
def application_withdraw(payload, vacancy_id):
    try:
        application = None

        # ToDo:,Delete Application

        return jsonify({
            "success": True,
            "message": "You withdrew your application!",
            "application": application,
        }), 200
    except Forbidden or Unauthorized or BadRequest:
        raise AuthError


@app.errorhandler(422)
def unprocessable():
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.error['code'],
        "message": error.error['description']
    }), error.status_code
