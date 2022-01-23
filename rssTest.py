import feedparser

parsedFeed = feedparser.parse("https://techcrunch.com/feed/")

entry = parsedFeed.entries[2]
print(entry.keys())



# for entry in parsedFeed.entries:
#     print(entry['content'])