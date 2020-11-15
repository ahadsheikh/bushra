import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

nltk.data.path.append('nlp/nltk-data')
nltk.download('vader_lexicon', download_dir='nlp/nltk-data')


def check_sentiment(news):
    sia = SIA()
    headline = news['headline']
    body = news['body']
    head_pol_score = sia.polarity_scores(headline)['compound']
    body_pol_score = sia.polarity_scores(body)['compound']
    pol_score = 0.5 * head_pol_score + 0.5 * body_pol_score
    if pol_score > 0.2:
        return True
    return False
