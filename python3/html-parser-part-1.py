# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if len(attrs)!= 0:
            for i in attrs:
                print("-> {0} > {1}".format(i[0],i[1]))
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if len(attrs)!= 0:
            for i in attrs:
                print("-> {0} > {1}".format(i[0],i[1]))

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
