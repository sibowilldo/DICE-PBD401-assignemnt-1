from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for
from .database.models import Vacancy, Status, Category, Type, User, Profile, Application, Attachment
from . import db
from flask_login import login_required, current_user
from .services.forms import VacancyForm, CategoryForm, TypeForm, StatusForm

main = Blueprint('routes', __name__)


@main.route(f"/", methods=['GET'])
def home():
    try:
        applications_ids = []
        if current_user.is_authenticated:
            applications = Application.query.filter(
                Application.user_id == current_user.id).all()
            applications_ids = list(
                map(lambda application: application.vacancy_id, applications))

        vacancies = Vacancy.query.filter(Vacancy.id.not_in(
            applications_ids)).order_by(Vacancy.created_at.desc()).all()
        vacancies = list(map(lambda vacancy: vacancy.long(), vacancies))

        return render_template('home.html', vacancies=vacancies)
    except Exception as ex:
        return render_template('errors/500.html', ex=ex)


@main.route(f"/<string:provider_id>/profile", methods=['GET'])
@login_required
def profile(provider_id):
    try:
        user = provider_id
        return jsonify({"user": user}), 200
    except Exception as ex:
        return render_template('errors/500.html', ex=ex)


'''
 ================= Users =====================
'''


@main.route(f"/admin/users", methods=['GET'])
@login_required
def users_index():
    try:
        users = User.query.all()
        users = list(map(lambda user: user.short(), users))
        return render_template('admin/users/index.html', data=users)
    except Exception as ex:
        return render_template('errors/500.html', ex=ex)


'''
 ================= Statuses =====================
'''


@main.route(f"/admin/statuses", methods=['GET'])
@login_required
def statuses_index():
    try:
        statuses = Status.query.all()
        statuses = list(map(lambda status: status.long(), statuses))
        return render_template('admin/statuses/index.html', data=statuses)
    except Exception as ex:
        return render_template('errors/500.html', ex=ex)


@main.route(f"/admin/statuses/create", methods=['GET'])
@login_required
def statuses_create():
    try:
        form = StatusForm.StatusForm()
        return render_template('admin/statuses/create.html', form=form)
    except Exception as ex:
        return render_template('errors/500.html', ex=ex)


@main.route(f"/admin/statuses", methods=['POST'])
@login_required
def statuses_store():
    try:
        form = request.form
        status = Status()
        status.model_type = form.get("model_type")
        status.name = form.get("name")
        status.description = form.get("description")
        status.priority = form.get("priority")

        status.insert()
        flash('Your status was published!', 'success')
        return redirect(url_for('routes.statuses_index'))
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/admin/statuses/<int:status_id>", methods=['GET'])
@login_required
def status_show(status_id):
    try:
        status = Status.query.filter(Status.id == status_id).first_or_404()

        status.update()
        return jsonify({
            "success": True,
            "status": status.long()
        }), 200
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/admin/statuses/<int:status_id>", methods=['PUT'])
@login_required
def status_update(status_id):
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
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/admin/statuses/<int:status_id>", methods=['DELETE'])
@login_required
def status_destroy(status_id):
    try:
        status = Status.query.filter(Status.id == status_id).first_or_404()
        status.delete()
        return jsonify({
            "success": True,
            "delete": status_id
        }), 200
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


'''
 ================= Category =====================
'''


@main.route(f"/admin/categories", methods=['GET'])
@login_required
def categories_index():
    try:
        categories = Category.query.all()
        categories = list(map(lambda category: category.long(), categories))
        return render_template('admin/categories/index.html', data=categories)
    except Exception as ex:
        return render_template('errors/500.html', ex=ex)


@main.route(f"/admin/category/create", methods=['GET'])
@login_required
def categories_create():
    try:
        form = CategoryForm.CategoryForm()
        return render_template('admin/categories/create.html', form=form)
    except Exception as ex:
        return render_template('errors/500.html', ex=ex)


@main.route(f"/admin/categories", methods=['POST'])
@login_required
def categories_store():
    try:
        form = request.form
        category = Category()
        category.name = form.get("name")
        category.description = form.get("description")

        category.insert()
        flash('Your category was published!', 'success')
        return redirect(url_for('routes.categories_index'))
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/admin/categories/<int:category_id>", methods=['GET'])
@login_required
def categories_show(category_id):
    try:
        category = Category.query.filter(
            Category.id == category_id).first_or_404()

        category.update()
        return jsonify({
            "success": True,
            "category": category.long()
        }), 200
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/admin/categories/<int:category_id>", methods=['PUT'])
@login_required
def categories_update(category_id):
    try:
        req = request.get_json()
        category = Category.query.filter(
            Category.id == category_id).first_or_404()

        category.name = req.get("name")
        category.description = req.get("description")

        category.update()
        return jsonify({
            "success": True,
            "category": category
        }), 200
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/admin/categories/<int:category_id>", methods=['DELETE'])
@login_required
def categories_destroy(category_id):
    try:
        category = Category.query.filter(
            Category.id == category_id).first_or_404()
        category.delete()
        return jsonify({
            "success": True,
            "delete": category_id
        }), 200
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


'''
 ================= Type =====================
'''


@main.route(f"/admin/types", methods=['GET'])
@login_required
def types_index():
    try:
        types = Type.query.all()
        types = list(map(lambda vacancy_type: vacancy_type.long(), types))
        return render_template('admin/types/index.html', data=types)
    except Exception as ex:
        return render_template('errors/500.html', ex=ex)


@main.route(f"/admin/types/create", methods=['GET'])
@login_required
def types_create():
    try:
        form = TypeForm.TypeForm()
        return render_template('admin/types/create.html', form=form)
    except Exception as ex:
        return render_template('errors/500.html', ex=ex)


@main.route(f"/admin/types", methods=['POST'])
@login_required
def types_store():
    try:
        form = request.form
        type = Type()
        type.name = form.get("name")
        type.description = form.get("description")

        type.insert()
        flash('Your type was published!', 'success')
        return redirect(url_for('routes.types_index'))
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/admin/types/<int:type_id>", methods=['GET'])
@login_required
def types_show(type_id):
    try:
        vacancy_type = Type.query.filter(Type.id == type_id).first_or_404()

        vacancy_type.update()
        return jsonify({
            "success": True,
            "vacancy_type": vacancy_type.long()
        }), 200
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/admin/types/<int:type_id>", methods=['PUT'])
@login_required
def types_update(type_id):
    try:
        req = request.get_json()
        vacancy_type = Type.query.filter(Type.id == type_id).first_or_404()

        vacancy_type.name = req.get("name")
        vacancy_type.description = req.get("description")

        vacancy_type.update()
        return jsonify({
            "success": True,
            "vacancy_type": vacancy_type
        }), 200
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/admin/types/<int:type_id>", methods=['DELETE'])
@login_required
def types_destroy(type_id):
    try:
        vacancy_type = Type.query.filter(Type.id == type_id).first_or_404()
        vacancy_type.delete()
        return jsonify({
            "success": True,
            "delete": type_id
        }), 200
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


'''
 ================= Vacancies =====================
'''


@main.route(f"/vacancies", methods=['GET'])
@login_required
def vacancies_index():
    try:
        vacancies = Vacancy.query.all()
        vacancies = list(map(lambda vacancy: vacancy.long(), vacancies))
        return render_template('admin/vacancies/index.html', data=vacancies)
    except Exception as ex:
        return render_template('errors/500.html', ex=ex)


@main.route(f"/vacancies/create", methods=['GET'])
@login_required
def vacancies_create():
    form = VacancyForm.VacancyForm()
    return render_template('admin/vacancies/create.html', form=form)


@main.route(f"/vacancies", methods=['POST'])
@login_required
def vacancies_store():
    try:
        form = request.form
        vacancy = Vacancy()
        vacancy.title = form.get("title")
        vacancy.description = form.get("description")
        vacancy.department = form.get("department")
        vacancy.location = form.get("location")
        vacancy.expires_at = form.get("expires_at")
        vacancy.user_id = form.get("user_id")
        vacancy.category_id = form.get("category_id")
        vacancy.type_id = form.get("type_id")

        vacancy.insert()
        flash('Your vacancy was published!', 'success')
        return redirect(url_for('routes.home'))
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/vacancies/<int:vacancy_id>", methods=['GET'])
@login_required
def vacancies_show(vacancy_id):
    try:
        vacancy = Vacancy.query.filter(Vacancy.id == vacancy_id).first_or_404()

        vacancy.update()
        return jsonify({
            "success": True,
            "vacancy": vacancy.long()
        }), 200
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/vacancies/<int:vacancy_id>", methods=['PUT'])
@login_required
def vacancies_update(vacancy_id):
    try:
        form = request.form
        vacancy = Vacancy.query.filter(Vacancy.id == vacancy_id).first_or_404()

        vacancy.title = form.get("title")
        vacancy.description = form.get("description")
        vacancy.department = form.get("department")
        vacancy.location = form.get("location")
        vacancy.expires_at = form.get("expires_at")
        vacancy.category_id = form.get("category_id")
        vacancy.type_id = form.get("type_id")

        vacancy.update()
        flash('Your vacancy was updated!', 'success')
        return redirect(url_for('routes.home'))
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/vacancies/<int:vacancy_id>", methods=['DELETE'])
@login_required
def vacancies_destroy(vacancy_id):
    try:
        vacancy = Vacancy.query.filter(Vacancy.id == vacancy_id).first_or_404()
        vacancy.delete()
        return jsonify({
            "success": True,
            "delete": vacancy_id
        }), 200
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)


@main.route(f"/vacancies/<int:vacancy_id>/apply", methods=['POST'])
@login_required
def vacancies_apply(vacancy_id):
    try:
        vacancy = Vacancy.query.filter(Vacancy.id == vacancy_id).first_or_404()
        status = Status.query.filter(
            Status.name == 'active', Status.model_type == 'application').first_or_404()
        applicant = current_user
        application = Application()
        application.vacancy_id = vacancy.id
        application.status_id = status.id
        application.user_id = applicant.id

        application.insert()
        flash('Your application was submitted. Good Luck!', 'success')
        return redirect(url_for('routes.home'))
    except Exception as ex:
        db.session.rollback()
        return render_template('errors/400.html', ex=ex)


@main.route(f"/applications", methods=['GET'])
@login_required
def applications():

    # application = Application.query.first_or_404();

    # print(application.user.profile.given_name, application.vacancy.title, application.status.name)
    try:
        applications = Application.query.filter(
            Application.user_id == current_user.id).all()

        return render_template('applications.html', applications=applications)
    except Exception as ex:
        return render_template('errors/500.html', ex=ex)


@main.route(f"/application/<int:application_id>/destroy", methods=['POST'])
@login_required
def application_withdraw(vacancy_id):
    try:
        application = None

        # ToDo:,Delete Application

        return jsonify({
            "success": True,
            "message": "You withdrew your application!",
            "application": application,
        }), 200
    except Exception as ex:
        return render_template('errors/400.html', ex=ex)
