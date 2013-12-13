import numpy as np


class MessageSentimentCorrelations:

    def __init__(self, message_list):
        self.messages = message_list

    def _sentiment_correlation(self, attr_name):
        points = [(getattr(m, attr_name), m.sentiment) for m in self.messages]
        points = [point for point in points if point[0] is not None and point[1] is not None and point[1] != 0]
        x, y = zip(*points)
        return round(np.corrcoef(x, y)[0][1], 4)

    def by_rating(self):
        return self._sentiment_correlation("rating")

    def by_topic_probability(self):
        return self._sentiment_correlation("topic_probability")

    def by_author_rating(self):
        return self._sentiment_correlation("a_rating")

    def by_author_efficiency(self):
        return self._sentiment_correlation("a_efficiency")

    def by_age(self):
        return self._sentiment_correlation("a_age")

    def print_all(self, file):
        for name, corr in ("Age", self.by_age()),\
                          ("Rating", self.by_rating()),\
                          ("Topic probability", self.by_topic_probability()),\
                          ("Author rating", self.by_author_rating()),\
                          ("Author efficiency", self.by_author_efficiency()):
            file.write(name + "\t" + str(corr) + "\n")
        file.write("\n")
