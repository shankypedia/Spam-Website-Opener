import webbrowser
import time
import random

while True:
    sites = random.choice(['google.com', 'python.org', 'youtube.com', 'nodejs.org', 'github.com', 'gmail.com', 'minecraft.net'])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 10)
    time.sleep(seconds)
