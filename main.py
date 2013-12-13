import codecs
from Message import Message
from MessageSentimentMeans import MessageSentimentMeans
from MessageSentimentCorrelations import MessageSentimentCorrelations

qStatistics = "Data/FullQuestionStatistics.txt"
aStatistics = "Data/FullAnswerStatistics.txt"
qSentiments = "Data/QuestionSentiments.txt"
aSentiments = "Data/AnswerSentiments.txt"
outMeans = "Out/SentimentMeans.txt"
outCorrelations = "Out/SentimentCorrelations.txt"

messages = []
# with codecs.open(qStatistics, "r", "utf-8-sig") as f:
#     messages = [Message.create(line) for line in f.readlines()]
with codecs.open(aStatistics, "r", "utf-8-sig") as f:
    messages.extend([Message.create(line) for line in f.readlines()])
id_to_messages = {message.own_id: message for message in messages}

for name in qSentiments, aSentiments:
    with codecs.open(name, "r", "utf-8-sig") as f:
        splitted_lines = [line.strip().split("\t") for line in f.readlines()]
        for parts in splitted_lines:
            if len(parts) < 2:
                continue
            own_id = int(parts[0])
            sentiment = float(parts[1])
            if own_id in id_to_messages:
                id_to_messages[own_id].sentiment = sentiment

means = MessageSentimentMeans(id_to_messages.values())
with codecs.open(outMeans, "w", "utf-8-sig") as f:
    means.print_all(f)

corr = MessageSentimentCorrelations(id_to_messages.values())
with codecs.open(outCorrelations, "w", "utf-8-sig") as f:
    corr.print_all(f)
