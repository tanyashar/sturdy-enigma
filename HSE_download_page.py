import urllib.request
#import time
import html

def download_page(pageUrl):
    try:
        #time.sleep(2)
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('ISO-8859-1')
    except:
        print('Error at', pageUrl)
        return
    #print(pageUrl)

commonUrl = 'http://www.forumishqiptar.com/threads/'
for i in range(100, 90000):
    pageUrl = commonUrl + str(i)
    download_page(pageUrl)

test_string = "Петя &amp; Вася"
print(html.unescape(test_string))
print(html.unescape('&quot; &laquo; &raquo; &spades; &hearts; &clubs; &diams;'))

