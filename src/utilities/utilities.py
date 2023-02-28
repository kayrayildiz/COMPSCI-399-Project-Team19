from flask import Blueprint, url_for

import src.adapters.repo as repo
import src.utilities.services as services

utilities_blueprint = Blueprint('utilities_bp', __name__)

# USER
def get_user(user_name: str):
    return services.get_user(repo.repo_instance, user_name)


def update_user_tags(user_name: str, tag: str):
    services.update_user_tags(repo.repo_instance, user_name, tag)


def get_user_tags(user_name: str):
    return services.get_user_tags(repo.repo_instance, user_name)


def get_tag(question_tag: str):
    if question_tag == "prize_scam": return "p"
    elif question_tag == "urgency": return "u"
    elif question_tag == "link": return "l"
    else: return ""


def get_suggestions(user_tags: str):
    list_of_suggestions = []
    for x in user_tags:
        if x == "u": # Urgency
            message = "Look out for a sense of urgency or time pressure in emails. Often Phishers introduce a sense of time pressure/urgency into their message in order to induce a sense of adrenaline in the receiver, hoping to bait the receiver into acting on impulse."
            list_of_suggestions.append(message)
        elif x == "p": # Prize scam
            message = "Commonly, Phishers will try bait a receiver into taking part in a scam by discussing their malicious content into a prize scam. Be wary when emails tell you you have won a competition or prize that commonly seems too outrageous to be true."
            list_of_suggestions.append(message)
        elif x == "l": # Link
            message = "Phishing attacks often trick receivers into thinking they come from a reliable source by using trustworthy names of organisations or people you might know personally. In such cases you should look out for the links attached in the emails and the address that the email has been sent from. Often these links can give away that the message is actually laced with malicious content."
            list_of_suggestions.append(message)
    print("TEST", list_of_suggestions)
    return list_of_suggestions



# QUESTIONS
def get_all_questions():
    return services.get_all_questions(repo.repo_instance)


def get_question(question_id: int):
    return services.get_question(repo.repo_instance, question_id)


def get_chunks(data_array, per_page):
    return services.get_chunks(repo.repo_instance, data_array, per_page)


def get_user_score(user_name):
    return services.get_user_score(repo.repo_instance, user_name)


def update_user_score(user_name, score: int):
    services.update_user_score(repo.repo_instance, user_name, score)


def get_leaderboard():
    return services.get_leaderboard(repo.repo_instance)


def get_10_questions():
    return services.get_10_questions(repo.repo_instance)
