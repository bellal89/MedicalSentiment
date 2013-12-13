from datetime import datetime


class Message:
    def __init__(self, own_id, parent_id, category, rating, date_added, topic, topic_probability, text, a_email,
                 a_rating, a_efficiency, a_birthday, a_geo, a_gender):
        self.own_id = own_id
        self.parent_id = parent_id
        self.category = category
        self.rating = rating
        self.date_added = date_added
        self.topic = topic
        self.topic_probability = topic_probability
        self.text = text
        self.a_email = a_email
        self.a_rating = a_rating
        self.a_efficiency = a_efficiency
        self.a_birthday = a_birthday
        self.a_geo = a_geo
        self.a_gender = a_gender.strip() if a_gender.strip() != '' else 'Unknown'
        self.sentiment = 0

        self.a_age = None
        if self.date_added is not None and self.a_birthday is not None:
            self.a_age = (self.date_added - self.a_birthday).days / 365

    @staticmethod
    def create(line):
        ps = line.split("\t")
        return Message(Message.get_int(ps[0]), Message.get_int(ps[1]), ps[2], Message.get_int(ps[3]),
                       Message.get_datetime(ps[4]), Message.get_int(ps[5]), Message.get_float(ps[6]),
                       ps[7], ps[8], Message.get_int(ps[9]), Message.get_float(ps[10]), Message.get_datetime(ps[11]),
                       ps[12].lower(), ps[13])

    @staticmethod
    def get_datetime(text):
        if text == "":
            return None
        d = datetime.strptime(text, "%d.%m.%Y %H:%M:%S")
        if d.year <= 1920:
            return None
        return d

    @staticmethod
    def get_int(text):
        if text == '':
            return 0
        return int(text)

    @staticmethod
    def get_float(text):
        if text == '':
            return 0
        return float(text)

