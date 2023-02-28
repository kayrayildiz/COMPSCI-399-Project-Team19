from flask import request, session
from flask import Blueprint, render_template, url_for
import src.utilities.utilities as utilities

ten_questions_list = utilities.get_10_questions()

quiz_blueprint = Blueprint('quiz_bp', __name__)


@quiz_blueprint.route('/quiz', methods=['GET', 'POST'])
def quiz():
    total_number_of_questions = len(ten_questions_list)
    questions_chunks = utilities.get_chunks(ten_questions_list, 1)

    page_number = request.args.get("page_number")

    if page_number is None: page_number = 0
    page_number = int(page_number)

    if page_number == 0:
        previous_page = 0
    else:
        previous_page = page_number - 1

    if page_number == len(questions_chunks) - 1:
        next_page = len(questions_chunks) - 1
    else:
        next_page = page_number + 1

    question = utilities.get_question(page_number + 1)
    score = utilities.get_user_score(session['user_name'])

    num_emails_left, num_spam, num_legit = (total_number_of_questions - page_number), 5, 5

    return render_template(
        'quiz/module1.html',
        question=question,
        next_page=next_page,
        prev_page=previous_page,
        total_questions=total_number_of_questions,
        current_page=page_number,
        q_list=questions_chunks[page_number],
        num_pages=len(questions_chunks),
        num_emails_left=num_emails_left, num_spam=num_spam, num_legit=num_legit, score=score,
    )


submit_blueprint = Blueprint('submit_bp', __name__)


@submit_blueprint.route('/submitquiz', methods=['POST', 'GET'])
def submit():
    # Bring user back to question screen (essentially same as Quiz() blueprint)
    total_number_of_questions = len(ten_questions_list)
    questions_chunks = utilities.get_chunks(ten_questions_list, 1)
    page_number = request.args.get("page_number")

    if page_number is None: page_number = 0
    page_number = int(page_number)

    if page_number == 0: 
        previous_page = 0
    else: 
        previous_page = page_number - 1

    if page_number == len(questions_chunks) - 1: 
        next_page = len(questions_chunks) - 1
    else: 
        next_page = page_number + 1

    question = utilities.get_question(page_number + 1)
    score = utilities.get_user_score(session['user_name'])

    num_emails_left, num_spam, num_legit = (total_number_of_questions - page_number), 5, 5
    correct = False
    selected_option = request.values.get("option")

    # Find if question is legit or not depending on T/F value of is_legitimate property
    if question.is_legitimate: 
        correct_option = 1
    else: 
        correct_option = 0

    if int(selected_option) == int(correct_option): 
        correct = True
    else: 
        correct = False

    answer = "Illegitimate" if correct_option == 0 else "Legitimate"

    # Update user score
    if correct:
        utilities.update_user_score(session['user_name'], 1)
    else: 
        question_tag = utilities.get_tag(question.tag)
        utilities.update_user_tags(session['user_name'], question_tag)
  
    return render_template(
        'quiz/module1.html',
        results=True,
        quiz_result=correct,
        correct_option=answer,

        question=question,
        next_page=next_page,
        prev_page=previous_page,
        total_questions=total_number_of_questions,
        current_page=page_number,
        q_list=questions_chunks[page_number],
        num_pages=len(questions_chunks),
        num_emails_left=num_emails_left, num_spam=num_spam, num_legit=num_legit, score=score
    )


resolutions_blueprint = Blueprint('resolutions_bp', __name__)


@resolutions_blueprint.route('/resolutions', methods=['GET'])
def results():
    return render_template(
        'quiz/resolutions.html'

    )


leaderboard_blueprint = Blueprint('leaderboard_bp', __name__)


@leaderboard_blueprint.route('/leaderboard_page', methods=['GET'])
def leaderboard():
    user_name = session['user_name']
    score = utilities.get_user_score(user_name)
    leaderboard = utilities.get_leaderboard()

    return render_template(
        'quiz/leaderboard_page.html',
        score=score,
        leaderboard=leaderboard
    )
