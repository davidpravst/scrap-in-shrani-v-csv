import requests
from BeautifulSoup import BeautifulSoup

page = requests.get("https://scrapebook22.appspot.com/")

#print page.content

soup = BeautifulSoup(page.content)

#print soup.html.head.title.string

with open("podatki.csv", "w+") as podatki_file:
    for link in soup.findAll("a"): #najdi vse html elemente a (linke) in jih sprintaj
        if link.string == "See full profile":
            #print link
            #print link.string
            #print "https://scrapebook22.appspot.com/" + link["href"]
            osebna_stran = requests.get("https://scrapebook22.appspot.com/" + link["href"])
            #print osebna_stran.content
            osebna_stran_soup = BeautifulSoup(osebna_stran.content)
            #print osebna_stran_soup.html.head.title.string
            #print osebna_stran_soup.find("span", attrs={"class": "email"}).string

            podatki_file.write(osebna_stran_soup.findAll("h1")[1].string)
            podatki_file.write(",")
            podatki_file.write(osebna_stran_soup.find("span", attrs={"data-gender": True}).string)
            podatki_file.write(",")
            podatki_file.write(osebna_stran_soup.findAll("li")[1].string[5:7])
            podatki_file.write(",")
            podatki_file.write(osebna_stran_soup.find("span", attrs={"data-city": True}).string)
            podatki_file.write(",")
            podatki_file.write(osebna_stran_soup.find("span", attrs={"class": "email"}).string)
            podatki_file.write("\n")
print "Podatki so zapisani v datoteko \"podatki.csv\"!"

