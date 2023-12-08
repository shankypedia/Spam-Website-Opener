import webbrowser
import time
import random

def open_random_website():
    # List of websites for developers
    websites = [
        'coderanch.com', 'python.org', 'quora.com', 'nodejs.org', 'github.com',
        'stackoverflow.com', 'stackexchange.com', 'learn-anything.xyz',
        'devrant.com', 'google.com', 'codementor.io', 'codewars.com',
        'w3schools.com', 'hackerrank.com', 'freeCodeCamp.org', 'udemy.com'
        'developer.mozilla.org', 'codecademy.com', 'git-scm.com',
        'visualstudio.com', 'docker.com', 'npmjs.com', 'ruby-lang.org',
        'jetbrains.com', 'dzone.com', 'css-tricks.com', 'heroku.com',
        'golang.org', 'kaggle.com', 'leetcode.com', 'dev.to', 'hashnode.com'
    ]

    selected_website = random.choice(websites)
    print(f"Opening: {selected_website}")
    visit = f"https://{selected_website}"
    webbrowser.open(visit)

def main():
    try:
        # Set the limit for the number of website openings
        limit_openings = 100
        openings_count = 0

        while openings_count < limit_openings:
            open_random_website()
            seconds = random.uniform(5, 10)
            time.sleep(seconds)

            # Increment the counter after opening a website
            openings_count += 1

        print(f"Program stopped after opening {limit_openings} websites.")

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
