
from bs4 import BeautifulSoup
import re

clean1 = BeautifulSoup(open("./posts_1.html"), "lxml").text
clean2 = BeautifulSoup(open("./posts_2.html"), "lxml").text

pre1 = clean1.index("Dear Blueno updated their status.")
pre2 = clean2.index("Dear Blueno updated their status.")

cleaned = (clean1[pre1:] + clean2[pre2:]).replace("Dear Blueno updated their status.", "\n").replace("Dear Blueno shared a link.", "\n").replace(". ", "").replace(", ", "").strip()

cleaned = re.sub(r'\"?\d+\*? - ', '', cleaned)
cleaned = re.sub(r'[A-Z][a-z]+ \d+:\d+ [PA]M', '', cleaned)

file = open("./cleaned.txt", "w")
file.write(cleaned)
file.close()

print(cleaned)