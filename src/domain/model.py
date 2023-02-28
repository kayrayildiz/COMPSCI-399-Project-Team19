class User:

    def __init__(self, user_name: str, password: str, score: int = 0, frequently_incorrect: str = ""):
        if user_name == "" or not isinstance(user_name, str):
            self.__user_name = None
        else:
            self.__user_name = user_name.strip()

        if password == "" or not isinstance(password, str) or len(password) < 7:
            self.__password = None
        else:
            self.__password = password

        if score == None or not isinstance(score, int):
            self.__score = 0
        else:
            self.__score = score

        if frequently_incorrect == None or not isinstance(frequently_incorrect, str):
            self.__frequently_incorrect = ""
        else:
            self.__frequently_incorrect = frequently_incorrect

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def score(self) -> int:
        return self.__score

    @property
    def frequently_incorrect(self) -> str:
        return self.__frequently_incorrect

    def add_score(self, score: int):
        self.__score += score
    
    def add_frequently_incorrect(self, tag: str):
        if tag not in self.__frequently_incorrect:
            self.__frequently_incorrect = self.__frequently_incorrect + tag
        
    def __repr__(self):
        return f'<User {self.user_name}>'

    def __repr__(self):
        return f'<User {self.user_name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.user_name == self.user_name

    def __lt__(self, other):
        return self.user_name < other.user_name

    def __hash__(self):
        return hash(self.user_name)


class Question:
    def __init__(self, q_id: int, sender_address: str, email_subject: str, email_content: str, is_legitimate: bool, reason: str, tag: str):
        if q_id == "" or not isinstance(q_id, int):
            self.__q_id = None
        else:
            self.__q_id = q_id

        if sender_address == "" or not isinstance(sender_address, str):
            self.__sender_address = None
        else:
            self.__sender_address = sender_address.strip()

        if email_subject == "" or not isinstance(email_subject, str):
            self.__email_subject = None
        else:
            self.__email_subject = email_subject.strip()

        if email_content == "" or not isinstance(email_content, str):
            self.__email_content = None
        else:
            self.__email_content = email_content.strip()

        if is_legitimate == "" or not isinstance(is_legitimate, bool):
            self.__is_legitimate = None
        else:
            self.__is_legitimate = is_legitimate

        if reason == "" or not isinstance(reason, str):
            self.__reason = None
        else:
            self.__reason = reason.strip()

        if tag=="" or not isinstance(tag, str) or tag=="legitimate":
            self.__tag = "legitimate"
        else:
            self.__tag = tag

    @property
    def question_id(self):
        return self.__q_id

    @property
    def sender_address(self):
        return self.__sender_address

    @property
    def email_subject(self):
        return self.__email_subject

    @property
    def email_content(self):
        return self.__email_content

    @property
    def email_content_list_of_lists(self):
        list_of_lists = self.email_content.split("\n")

        for x in range(len(list_of_lists)):
            if "[user_name]" in list_of_lists[x]:
                index = list_of_lists[x].find("[user_name]")
                list_of_lists[x] = list_of_lists[x][:index] + str("session['user_name']") + list_of_lists[x][index+1+len("[user_name]"):]

        return list_of_lists
        
    @property
    def is_legitimate(self):
        return self.__is_legitimate

    @property
    def reason(self):
        return self.__reason

    @property
    def tag(self):
        return self.__tag

    def __repr__(self):
        return f'<Question id: {self.question_id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.question_id == other.question_id

    def __lt__(self, other):
        return self.question_id < other.question_id

    def __hash__(self):
        return hash(self.question_id)


'''
class Question2:
    def __init__(self, q_id: int, question: str, option1: str, option2: str, correctoption: int):
        self.option1 = option1 
        self.option2 = option2
        self.q_id = q_id
        self.question = question
        self.correctoption = correctoption

    def getQ_id(self):
        return self.q_id

    def getQuestion(self):
        return self.question

    def getOption1(self):
        return self.option1

    def getOption2(self):
        return self.option2

    def getCorrectionOption(self):
        return self.correctoption

    def get_correct_option(self):
        if self.correctoption == 1:
            return self.option1
        elif self.correctoption == 2:
            return self.option2

'''


class Question2:
    def __init__(self, q_id: int, question: str, option1: str, option2: str, option3: str, option4: str,
                 correctoption: int, reason: str):
        self.q_id = q_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correctoption = correctoption
        self.reason = reason

    def getQ_id(self):
        return self.q_id

    def getQuestion(self):
        return self.question

    def getOption1(self):
        return self.option1

    def getOption2(self):
        return self.option2

    def getOption3(self):
        return self.option3

    def getOption4(self):
        return self.option4

    def get_correct_option(self):
        return self.correctoption

    def get_reason(self):
        return self.reason
