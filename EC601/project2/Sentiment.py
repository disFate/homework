"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse

from google.cloud import language_v1


def analyzer(text):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(
        content=text, type=language_v1.Document.Type.PLAIN_TEXT
    )
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    return sentiment


def main():
    text = "Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the " \
           "new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users " \
           "love their new Android phones. "
    sentiment = analyzer(text)
    print("Text: {}".format(text))
    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))


if __name__ == "__main__":
    main()
