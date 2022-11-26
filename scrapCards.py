major = ["The Fool","magician","The High Priestess","The Empress","The Emperor","The Hierophant","The Lovers","The Chariot","The Strength","The Hermit","The Wheel of Fortune","The Justice","The Hanged Man","The Death","The Temperance","The Devil","The Tower","The Star","The Moon","The Sun","The Judgement","The World"]
minor = ['Ace of Swords', 'Ace of Wands', 'Ace of Pentacles', 'Ace of Cups', '2 of Swords', '2 of Wands', '2 of Pentacles', '2 of Cups', '3 of Swords', '3 of Wands', '3 of Pentacles', '3 of Cups', '4 of Swords', '4 of Wands', '4 of Pentacles', '4 of Cups', '5 of Swords', '5 of Wands', '5 of Pentacles', '5 of Cups', '6 of Swords', '6 of Wands', '6 of Pentacles', '6 of Cups', '7 of Swords', '7 of Wands', '7 of Pentacles', '7 of Cups', '8 of Swords', '8 of Wands', '8 of Pentacles', '8 of Cupss', '9 of Swords', '9 of Wands', '9 of Pentacles', '9 of Cups', '10 of Swords', '10 of Wands', '10 of Pentacles', '10 of Cups', 'Page of Swords', 'Page of Wands', 'Page of Pentacles', 'Page of Cups', 'Knight of Swords', 'Knight of Wands', 'Knight of Pentacles', 'Knight of Cups', 'Queen of Swords', 'Queen of Wands', 'Queen of Pentacles', 'Queen of Cups', 'King of Swords', 'King of Wands', 'King of Pentacles', 'King of Cups']

fullDeck = major + minor

from bs4 import BeautifulSoup as bs
import requests
from PIL import Image


r = requests.get("https://tarotx.net/tarot-card-meanings/rider-waite/").text

soup =bs(r,'lxml')

images =soup.find_all('img', alt =True)


for image in images:

    for card in fullDeck:
        
        if card.lower() == image['alt'].lower():
            image_url =image['src']
            print(image_url)
            img = Image.open(requests.get(image_url, stream = True).raw)
            img.save(image['alt'] + '.png')

   


