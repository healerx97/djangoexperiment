import feedparser
import csv
import sys
parsedFeed = feedparser.parse(sys.argv[1])

# print(parsedFeed.entries[0].keys())


def main(feedUrl):
    parsedFeed = feedparser.parse(feedUrl)
    print(parsedFeed.entries[0].keys())



main(sys.argv[1])
# with open('rssFeed.csv', 'w') as file:
#     f = csv.writer(file)
#     f.writerow(['Title', 'Summary', 'Published Date'])
#     for entry in parsedFeed.entries:
#         s = [entry['title'], entry['summary'], entry['published']]
#         f.writerow(s)




# keys = ['title', 'title_detail', 'links', 'link', 'comments', 'authors', 'author', 'author_detail', 'published', 'published_parsed', 'tags', 'id', 'guidislink', 'summary', 'summary_detail', 'content', 'wfw_commentrss', 'slash_comments', 'post-id']