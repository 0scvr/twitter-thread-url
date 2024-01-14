import csv, re, requests

API_URL = 'https://twitter-thread.com/api/unroll-thread'
TWITTER_PATTERN = r'https:\/\/twitter\.com\/.+\/status\/(\d+)'
X_PATTERN = r'https:\/\/x\.com\/.+\/status\/(\d+)'

# replaces a twitter.com URL with a twitter-thread.com URL string
def replace_url(tweet_id):
    return 'https://twitter-thread.com/t/' + tweet_id

# reads a csv file and extracts the URLs
def extract_urls_from_csv(csv_file):
    url_list = []

    with open(csv_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            url = row["url"]
            if url:
                url_list.append(url)

    return url_list

# extracts the tweet id from a tweet URL string
def extract_tweet_id(url):
    match = re.match(TWITTER_PATTERN, url)
    if match:
        return match.group(1)
    else:
        match = re.match(X_PATTERN, url)
        if match:
            return match.group(1)
    return None

# call twitter-thread API with given tweet_id to create a thread for it. Returns 1 if successful, None otherwise
def send_post_request(tweet_id):
    response = requests.post(API_URL, params={'id': tweet_id}, headers={'Authority': 'twitter-thread.com'})
    if response.status_code == 200:
        print(f"Thread for tweet {tweet_id} successfully created.")
        return 1
    else:
        print(f"Error creating thread for tweet {tweet_id}")
        return None
