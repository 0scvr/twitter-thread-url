from utils import replace_url, extract_urls_from_csv, extract_tweet_id, send_post_request
import csv, time

# Task 1: Extract IDs from a list of tweet URLs
tweet_urls = extract_urls_from_csv("input.csv")

tweet_ids = [extract_tweet_id(url) for url in tweet_urls if extract_tweet_id(url)]
print("Found", len(tweet_ids), "tweet IDs.")

# Task 2: Transform the URL strings with replace_url
transformed_urls = [replace_url(id) for id in tweet_ids]

# 3. export them in csv
with open("output.csv", "w", newline="") as outfile:
    w = csv.writer(outfile, delimiter=',')
    header = ['url']
    w.writerow(header)

    for url in transformed_urls:
        w.writerow([url])
print("URLs replaced and saved to", outfile.name)

# Task 4: Call the API with send_post_request for each ID
success_count = 0
print("Calling API...")
for tweet_id in tweet_ids:
    result = send_post_request(tweet_id)
    if result:
        success_count += 1
    time.sleep(1.8) # to avoid being rate limited

print(f"Total threads created: {success_count}/{len(tweet_ids)}")
