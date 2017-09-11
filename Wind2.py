import urllib
from bs4 import BeautifulSoup

url = "https://www.wunderground.com/US/MA/Quincy.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
for num in range(len(text)):
    if text[num]=='G':
        if text[num+1] == 'u':
            if text[num+2] == 's':
                if text[num+3] == 't':
                  if text[num+4] == 's':
                      Direction = str(text[num - 3] + text[num - 2] + text[num - 1]).strip()
                      if not text[num-4].isspace():
                          if text[num-5].isspace():
                              Direction = str(text[num - 4] + text[num - 3] + text[num - 2] + text[num - 1]).strip()
                          if text[num-6].isspace():
                            Direction = str(text[num - 5] + text[num - 4] + text[num - 3] + text[num - 2] + text[num - 1]).strip()
                          else:
                              Direction = str(text[num - 6] + text[num - 5] + text[num - 4] + text[num - 3] + text[num - 2] + text[num - 1]).strip()

                      for number in range(num, 0, -1):
                        if text[number].isdigit():
                            Speed = (text[number-3] + text[number-2] + text[number -1] + text[number]).strip()
                            WindSpeed = float(Speed)
                            break
                      for dex in range(num, len(text)):
                          if text[dex].isdigit():
                            Gust = (text[dex] + text[dex + 1] + text[dex + 2]).strip()
                            Gusts = float(Gust)
                            break
print "WindSpeed: ", WindSpeed, "Gusts: ", Gusts, "Direction: ", Direction



#print text


