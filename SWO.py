import webbrowser
import time
import random

while True:
    sites = sorted([
        'coderanch.com', 'python.org', 'quora.com', 'nodejs.org', 'github.com',
        'stackoverflow.com', 'stackexchange.com', 'learn-anything.xyz',
        'devrant.com', 'google.com', 'codementor.io', 'codewars.com'
    ])
    
    visit = f"https://{random.choice(sites)}"
    webbrowser.open(visit)

    seconds = random.randrange(5, 10)
    time.sleep(seconds)
