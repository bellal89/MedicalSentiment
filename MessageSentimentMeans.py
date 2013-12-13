import numpy as np


class MessageSentimentMeans:
    def __init__(self, message_list):
        self.messages = message_list

    def _sentiment_dist(self, attr_name):
        dist = {}
        for m in self.messages:
            attr_val = getattr(m, attr_name)
            if attr_val is None or m.sentiment == 0:
                continue
            if attr_val not in dist:
                dist[attr_val] = []
            dist[attr_val].append(m.sentiment)
        return dist

    @staticmethod
    def _get_means(dist):
        return {k: (len(v), round(np.mean(v), 4)) for k, v in dist.items()}

    def by_gender(self):
        return self._get_means(self._sentiment_dist("a_gender"))

    def by_topic(self):
        return self._get_means(self._sentiment_dist("topic"))

    def by_category(self):
        return self._get_means(self._sentiment_dist("category"))

    def by_geo(self):
        return self._get_means(self._sentiment_dist("a_geo"))

    @staticmethod
    def print_mean_dist(file, name, dist):
        file.write(name + ":\n")
        file.write(
            "\n".join([(k if isinstance(k, basestring) else str(k)) + "\t" + str(
                v[1]) + "\t" + str(v[0]) for k, v in dist.items()]))
        file.write("\n\n")

    def print_all(self, file):
        for name, dist in ("Gender", self.by_gender()), \
                          ("Topic", self.by_topic()), \
                          ("Category", self.by_category()), \
                          ("Geo", self.by_geo()):
            self.print_mean_dist(file, name, dist)
