import webbrowser
import time
import random

for i in range(30):
    url = "https://www.bing.com/search?q=" + str(random.randint(1, 1000000000))
    webbrowser.open(url)
    time.sleep(6)
