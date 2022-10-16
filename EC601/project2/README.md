# Twitter APIs

---

This is a test for Twitter APIs, including get twitter, search twitter and botometer to check if the user is a bot. You can use postman to test  the api or use the demo code on Github served by Twitter.

## Prerequisites

---

* Sign up for Twitter developer account and receive approval
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials 

## environment set up

---

* You need to install some packages at first by using this command in terminal.

	```python
	pip install requests
	pip install requests-oauthlib
	```

* Then import these packages in your code.

	```python
	from requests_oauthlib import OAuth1Session
	import os
	import json
	```

* You also need to set the env virable in terminal or replace the varivable in the code

	```python
	consumer_key = os.environ.get("CONSUMER_KEY")
	consumer_secret = os.environ.get("CONSUMER_SECRET")
	```

	```python
	bearer_token = os.environ.get("BEARER_TOKEN")
	```

## APIs

---

### Get Twitters:

* You can get twitters by twitter ids(can be a single id or a collection of ids). You can also specify the fields of twitters you want to get.

	```python
	params = {"ids": "1278747501642657792", "tweet.fields": "created_at"}
	```

* The result is like:

	```python
	Response code: 200
	{
	    "data": [
	        {
	            "created_at": "2020-07-02T17:48:57.000Z",
	            "edit_history_tweet_ids": [
	                "1278747501642657792"
	            ],
	            "id": "1278747501642657792",
	            "text": "It's been a year since Twitter's Developer Labs launched.\n\nAs we build towards the next generation of the #TwitterAPI (coming VERY soon), see what we've learned and changed along the way. https://t.co/WvjuEWCa6G"
	        }
	    ]
	}
	```

* Now you get the text and created time of the twitter with id you give.

### Search Twitters:

* You can search twitters by key words as string and the max results is between 10 - 100

	```python
	query_params = {'query': '(Boston University) OR #twitterdev','tweet.fields': 'author_id', 'max_results': 100}
	```

* The result is like:

	```python
	200
	{
	    "data": [
	        {
	            "author_id": "1370602357344632835",
	            "edit_history_tweet_ids": [
	                "1581754189348098049"
	            ],
	            "id": "1581754189348098049",
	            "text": "@birdbiddness emory university in atlanta, boston university, cuny macaulay honors (CRAZY REACH like 3% acceptance rate), rutgers university in jersey"
	        },
	        {
	            "author_id": "796862414792880128",
	            "edit_history_tweet_ids": [
	                "1581752470631350273"
	            ],
	            "id": "1581752470631350273",
	            "text": "RT @WilliamAEden: This lab from Boston University is taking the Omicron spike protein and adding it to wildtype COVID:\n\n\u201cIn K18-hACE2 mice,\u2026"
	        },
	        ...
	    ]
	}
	```

	### Botometers:

	* You can check the user by its id or screen name

		```python
		# Check a single account by screen name
		result = bom.check_account('@clayadavis')
		
		# Check a single account by id
		result = bom.check_account(1548959833)
		```

	* The result is like:

		```python
		{
		    "cap": {
		        "english": 0.8018818614025648,
		        "universal": 0.5557322218336633
		    },
		    "display_scores": {
		        "english": {
		            "astroturf": 0.0,
		            "fake_follower": 4.1,
		            "financial": 1.5,
		            "other": 4.7,
		            "overall": 4.7,
		            "self_declared": 3.2,
		            "spammer": 2.8
		        },
		        "universal": {
		            "astroturf": 0.3,
		            "fake_follower": 3.2,
		            "financial": 1.6,
		            "other": 3.8,
		            "overall": 3.8,
		            "self_declared": 3.7,
		            "spammer": 2.3
		        }
		    },
		    "raw_scores": {
		        "english": {
		            "astroturf": 0.0,
		            "fake_follower": 0.81,
		            "financial": 0.3,
		            "other": 0.94,
		            "overall": 0.94,
		            "self_declared": 0.63,
		            "spammer": 0.57
		        },
		        "universal": {
		            "astroturf": 0.06,
		            "fake_follower": 0.64,
		            "financial": 0.3133333333333333,
		            "other": 0.76,
		            "overall": 0.76,
		            "self_declared": 0.74,
		            "spammer": 0.47
		        }
		    },
		    "user": {
		        "majority_lang": "en",
		        "user_data": {
		            "id_str": "11330",
		            "screen_name": "test_screen_name"
		        }
		    }
		}
		```

	* We can focus on cap the see the possibility this user is a bot, or see the detailed information in display_scores

	

	













