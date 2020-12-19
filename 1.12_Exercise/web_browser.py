import webbrowser
import time
from random import randint

count = 0
urls = ['https://www.pycorners.com/', 'https://www.pycorners.com/stories', 'https://www.pycorners.com/storie/4/2020/7/26/jwtjson-web-token-django-rest-api',
        'https://www.pycorners.com/storie/3/2020/7/12/ai-assistance-using-python', 'https://www.pycorners.com/notes', 'https://www.pycorners.com/code',
        'https://www.pycorners.com/codes/2/2020/7/13/ai-assistance-using-python', 'https://www.pycorners.com/codes/1/2020/7/4/web-serivces-python']
# chrome_path = '/usr/bin/google-chrome %s'
while count < 2:
    for url in urls:
        index = randint(0, 7)
        time_index = randint(20, 40)
        print(index, time_index)
        webbrowser.open(urls[int(index)])
        time.sleep(time_index)
    count = count+1
else:
    pass