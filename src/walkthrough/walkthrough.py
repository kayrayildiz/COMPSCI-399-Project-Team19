from flask import Blueprint, render_template

walkthrough_blueprint = Blueprint('walkthrough_bp', __name__)
@walkthrough_blueprint.route('/walkthrough', methods=['GET'])
def walkthrough():
    return render_template(
        'walkthrough.html',
    ) 
