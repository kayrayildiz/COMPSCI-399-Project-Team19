from flask import Blueprint, render_template

about_blueprint = Blueprint('about_bp', __name__)
@about_blueprint.route('/about', methods=['GET'])
def about():
    content_dict = {'So, what is phishing?':
                        ["\"Amateurs hack systems, professionals hack people\" Bruce Schneier, cryptographer, computer security professional and privacy specialist.", 
                         "This is exactly the case for a type of cyber-attack known as phishing. The category of cyber security can be a daunting one, what with there being an average of over 2,200 cyber- attacks daily, the realm of internet security is becoming more and more important by the second. With 96 percent of phishing attacks arriving by email, and an estimated number of 156 million phishing emails being distributed on a daily basis, the risk of an individual or business being targeted continues to increase impedingly. The education of anti- phishing is one which has never been more important, and yet, such education is not often made readily available to internet users.",
                         "Our goal is to understand better how users interact with simulated examples of legitimate vs illegitimate emails. Because phishing attacks are focused on psychological behaviour, it is imperitive to understand how individuals navigate through the internet, in order to understand how best to combat cyber threats.",
                         "After comprehensive research in the field of cyber security Team 19 has produced \"Catching A Phish\" which uses educational and interactive techniques to help users apply their knowledge derived from our game into their own lives."],
                    'Our Team': "A passionate team of 5 Computer Science students with dedicated to improving internet wellbeing. There is no one size fits all, so we take a tailored and well-defined approach to educating users of internet safety.",
                    'What we\'re all about':
                        ["Catching a Phish is an interactive web-based game application to help you know when something phishing is going on, and what you can do about it."], 
                    }
    return render_template(
        'about/about.html',
        content_dict = content_dict
    ) 
