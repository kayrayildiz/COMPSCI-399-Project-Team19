from flask import request, session

from flask import Blueprint, render_template, url_for

from src.domain.model import Question
import src.utilities.utilities as utilities
import src.utilities.services as services
import src.adapters.repo as repo

modules_blueprint = Blueprint('modules_bp', __name__)
@modules_blueprint.route('/modules', methods=['GET', 'POST'])
def modules():
    user_name = session['user_name']
    score = utilities.get_user_score(user_name)
    return render_template(
        'quiz/modules.html',
        user_score = score
    )