from flask import request, session

from flask import Blueprint, render_template

import src.utilities.utilities as utilities
from src.domain.model import Question2

q1 = Question2(1,
               "Which one of the statements is correct?",
               "If people are distracted by a hurricane or a flu pandemic, they might be less likely to read emails carefully.",
               "Phishers often take advantage of current events, such as natural disasters, health scares, or political elections, and send messages with those themes to play on people's fears.",
               "Phishing emails reach more people if they are worried about the weather.",
               "If people go without power due to a storm or other natural disaster, they will be excited about communication being restored and they will respond to the emails they receive once power is back.",
               2,
               "Attackers often take advantage of their victims when they are in some sort of distraught as people are much likely to make mistakes")
q2 = Question2(2,
               "What is a phishing attack called when it is designed to look like an email from a user's superior within the organization?",
               "Whale phishing.",
               "Spear phishing.",
               "Deceptive phishing.",
               "In-session phishing",
               2,
               "Phishing attacks like these come from inside the organisation such as a trusted user.")
q3 = Question2(3,
               "Which one of the statements is correct?",
               "A spoof is another name for an illegitimate website.",
               "A whaling attack is highly personalized to the recipient and that builds trust by using personal details often gleaned from social media accounts and other sources.",
               "Disconnecting from the internet is an effective method of reversing a phishing attack because perpetrators no longer have access to your network.",
               "If you recieve a phishing email from someone you know, you shouldn't try to contact them via some alternative means of communication(phone or text message) to confirm it.",
               1,
               "Website spoofing, aka domain spoofing, occurs when a scammer creates a fraudulent website, mimicking a trusted company, oftentimes with the goal of stealing visitors' personal information.")
q4 = Question2(4,
               "Which one of the statements is correct?",
               "Phishing emails tend to grow more sophisticated each day, thus we must all take precaution upon viewing them",
               "Most firms have several security precautions in place, but they don't control individual users' non-corporate devices.",
               "You most likely receive phishing emails on your personal email accounts as well, so it pays to be aware.",
               "All of the above.",
               4,
               "While this is a good answer, the others are just as important. We receive phishing scams on our personal email, texts and also social media accounts on the daily, which is hard for corporations to ")
q5 = Question2(5,
               "You have been sent a phishing email. What should you do?",
               "Click on the link to claim your million dollars and quit your job.",
               "Ignore the email and delete it.",
               "Let the IT department know that you have been sent a phishing email.",
               "All of the above",
               2,
               "It is best practice to just ignore any phishing emails as the IT department probably deals with numerous phishing emails already.")
q6 = Question2(6,
               "What are the possible outcomes if you have clicked on a phishing link?",
               "The link could potentially download and install malware which can cause damage to the company.",
               "The attacker will be able to gain access to sensitive company information.",
               "The attacker sends you the iphone he/she promised.",
               "1 and 2",
               4,
               "The attacker will definitely not give you an iphone.")
q7 = Question2(7,
               "Which of the following practices should IT employ for an email phishing test?",
               "Include executives and management.",
               "Mimic the tactics of typical phishing attacks.",
               "Extract as much user data as possible.",
               "All of the above",
               4,
               "While this is a correct answer, however, we should also create an environment that mimics a phishing attack and use this opportunity to get user data for further studies")
q8 = Question2(8,
               "What is a phishing attack called when it is based on SMS/Text?",
               "Smishing.",
               "Spear phishing.",
               "Text phishing.",
               "Vishing.",
               1,
               "Smishing is a phishing cybersecurity attack carried out over mobile text messaging, also known as SMS phishing.")
q9 = Question2(9,
               "What are the most common signs of a phishing scams?",
               "Attractive layout and nice graphics.",
               "Perfect use of spelling and grammar.",
               "Sender creates a sense of urgency and tries to panic the recipient.",
               "All of the above.",
               3,
               "Attackers always create a sense of urgency to make the victim panic and make mistakes such as clicking a scam link.")
q10 = Question2(10, 
                "What is the most common kind of phishing attack?",
                "Contact them via phone or email to discuss the job position further.", 
                "Smishing", 
                "Email based.", 
                "Vishing",
                3,
                "About 3.4 billion phishing emails are sent daily"
                )


qlist = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]  # the list stores all the Questions
wrongQ = []


quiz_blueprint2 = Blueprint('quiz_bp2', __name__)


@quiz_blueprint2.route('/quiz2', methods=['GET', 'POST'])
def quiz2():

    # implements pagination or do we really need it?
    total_number_of_questions = len(qlist)
    question_chunks = utilities.get_chunks(qlist, 1)

    page_number = request.args.get("page_number")

    if page_number is None:
        page_number = 0

    page_number = int(page_number)
    if page_number == 0:
        previous_page = 0
    else:
        previous_page = page_number - 1

    if page_number == len(question_chunks) - 1:
        next_page = len(question_chunks) - 1
    else:
        next_page = page_number + 1

    question = qlist[page_number]
    # question = utilities.get_question(page_number + 1)
    score = utilities.get_user_score(session['user_name'])

    return render_template(
        'quiz/module2.html',
        questionlist=qlist,
        question=question,
        next_page=next_page,
        prev_page=previous_page,
        total_questions=total_number_of_questions,
        current_page=page_number,
        q_list=question_chunks[page_number],
        num_pages=len(question_chunks),
        score=score,

    )


submit_blueprint2 = Blueprint("submit_bp2", __name__)


@submit_blueprint2.route('/submitquiz2', methods=['POST', 'GET'])
def submit2():

    total_number_of_questions = len(qlist)
    questions_chunks = utilities.get_chunks(qlist, 1)
    page_number = request.args.get("page_number")

    if page_number is None:
        page_number = 0

    page_number = int(page_number)
    if page_number == 0:
        previous_page = 0
    else:
        previous_page = page_number - 1

    if page_number == len(questions_chunks) - 1:
        next_page = len(questions_chunks) - 1
    else:
        next_page = page_number + 1

    question = qlist[page_number]  # return an object!

    score = utilities.get_user_score(session['user_name'])

    num_emails_left, num_spam, num_legit = (total_number_of_questions - page_number), 5, 5
    correct = False
    selected_option = request.values.get("option")
    correct_option = str(question.get_correct_option())

    if selected_option == correct_option:
        correct = True
    else:
        correct = False
        wrongQ.append(question)

    # Update user score
    if correct: utilities.update_user_score(session['user_name'], 1)

    return render_template(
        'quiz/module2.html',
        results=True,
        quiz_result=correct,
        correct_option=correct_option,

        question=question,
        next_page=next_page,
        prev_page=previous_page,
        total_questions=total_number_of_questions,
        current_page=page_number,
        q_list=questions_chunks[page_number],
        num_pages=len(questions_chunks),
        num_emails_left=num_emails_left, num_spam=num_spam, num_legit=num_legit, score=score
    )


resolutions_blueprint2 = Blueprint('resolutions_bp2', __name__)


@resolutions_blueprint2.route('/resolutions2', methods=['GET'])
def results2():
    return render_template(
        'quiz/resolutions2.html'

    )


solution_blueprint = Blueprint("solution_bp", __name__)


@solution_blueprint.route('/solution', methods=['GET'])
def solution():
    return render_template(
        'quiz/resolutions.html',
        wrong_question=wrongQ

    )
