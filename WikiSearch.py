from bs4 import BeautifulSoup
import urllib
import urllib.request
import re
import wikipedia
import time
import speech_recognition as sr
import pyttsx3
def search(query):
    address = "http://www.bing.com/search?q=%s" % (urllib.parse.quote_plus(query))
    getRequest = urllib.request.Request(address, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})
    urlfile = urllib.request.urlopen(getRequest)
    htmlResult = urlfile.read(200000)
    urlfile.close()
    soup = BeautifulSoup(htmlResult,'lxml')
    [s.extract() for s in soup('span')]
    results = soup.find_all('li', { "class" : "b_algo" })
    for result in results:
        if result is not None:
            links = str(result.find('a' ).get('href'))
            wikilink = " "
            if 'wikipedia' in  links:
                wikilink = links
                break;
            else:
                print("No wikipedia page for this keyword try another one")
                
    url = wikilink
    url = re.split("\/" , url)
    tag = url[len(url)-1]
    print(tag)
    textdata = wikipedia.summary(tag)
    print(textdata)
    engine = pyttsx3.init()
    engine.say(textdata)
    engine.runAndWait()
    



r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say the search keyword!")
    audio = r.listen(source)
 

try:
    text = r.recognize_google(audio)
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

searchtext = text + "wikipedia"
search(searchtext)
