import feedparser
import csv
parsedFeed = feedparser.parse("https://techcrunch.com/feed/")



with open('rssFeed.csv', 'w') as file:
    f = csv.writer(file)
    f.writerow(['Title', 'Summary', 'Published Date'])
    for entry in parsedFeed.entries:
        s = [entry['title'], entry['summary'], entry['published']]
        f.writerow(s)




# keys = ['title', 'title_detail', 'links', 'link', 'comments', 'authors', 'author', 'author_detail', 'published', 'published_parsed', 'tags', 'id', 'guidislink', 'summary', 'summary_detail', 'content', 'wfw_commentrss', 'slash_comments', 'post-id']