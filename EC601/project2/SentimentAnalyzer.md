# Sentiment Analyzer

## Users

* researcher
* journalist
* manager

## User Stories

* as a research, I want to get the statistics about public sentiment about the news to make a model
* as a journalist, I want to know public attitude towards news to write my article 
* as a manager, I want to know others perspective on the policy to help me adjust the strategy

## MVP

* By serving a keyword about a news, users can get the result of sentiment analyzation on this word

## Modules

* SearchTwitters: use twitter API to get twitters by keywords*
* Botometers(next sprint): filter some twitters if the users is possible to be a bot
* Sentiment: use Google NLP API to analyze the sentiment of twitters 

## Result

```python
search_url = "https://api.twitter.com/2/tweets/search/recent"
query_params = {'query': 'Kevin Durant', 'tweet.fields': 'author_id', 'max_results': 50}
```

![result](C:\Users\Tsuna\Desktop\homework\homework\EC601\project2\result.png)

we can see that the positive news about Kevin Durant is more than negative one