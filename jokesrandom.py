import requests
from bs4 import BeautifulSoup
import random

def joke_generator_from_elon():
    url = "https://www.elon.edu/u/imagining/about/kidzone/jokes-laughs/"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Failed to fetch jokes:", e)
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    quick_jokes_section = None
    for h3 in soup.find_all('h3'):
        if "Quick jokes" in h3.get_text():
            quick_jokes_section = h3
            break

    if not quick_jokes_section:
        print("Couldn't find jokes on the page.")
        return

    jokes = []
    current_joke = []
    

    for tag in quick_jokes_section.find_next_siblings():
        if tag.name and tag.name.startswith('h'): 
            break
        if tag.name == 'p':
            text = tag.get_text().strip()
            if text: 
                if text.endswith('?'): 
                    if current_joke:  
                        jokes.append(" ".join(current_joke))
                        current_joke = []
                    current_joke.append(text)
                else: 
                    current_joke.append(text)
    

    if current_joke:
        jokes.append(" ".join(current_joke))

    if not jokes:
        print("No jokes found.")
        return

    selected = random.choice(jokes)
    print("Here's a joke for you:")
    print(selected)

if __name__ == "__main__":
    joke_generator_from_elon()