import SearchTwitters
import Sentiment

search_url = "https://api.twitter.com/2/tweets/search/recent"
query_params = {'query': 'Kevin Durant', 'tweet.fields': 'author_id', 'max_results': 10}


def main():
    json_response = SearchTwitters.connect_to_endpoint(search_url, query_params)
    texts = []
    for data in json_response['data']:
        texts.append(data['text'])
    positive = 0
    negative = 0
    for text in texts:
        score = Sentiment.analyzer(text).score
        print(score)
        if Sentiment.analyzer(text).score > 0.25:
            positive += 1
        elif Sentiment.analyzer(text).score < -0.25:
            negative += 1
    print("positive : negative = {} : {}".format(positive, negative))


if __name__ == "__main__":
    main()
