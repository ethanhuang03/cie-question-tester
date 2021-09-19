import urllib.request, urllib.error, urllib.parse


class pastPaper(object):
    def __init__(self, category="", subject="", year="", season="", paper="", time_zone="", chapter="",
                 website_page=""):
        self.question_found = False
        self.category = category  # 3: IGCSE, 5: A Level, 7: IB Diploma
        self.subject = subject  # still need to be decoded
        self.year = year  # past paper year
        self.season = season  # "winter" or "summer,winter"
        self.paper = paper  # dependant on subject, input can also be "1", "1,2" etc.
        self.time_zone = time_zone  # 0 is IB only, input can also be "1", "1,2,3,4,5" etc.
        self.chapter = chapter  # still need to be decoded
        self.offset = website_page * 20  # 0 for first page, 20 for second page, 40 for third
        self.link = f"https://www.exam-mate.com/topicalpastpapers/?cat={self.category}&subject={self.subject}" \
                    f"&years={self.year}&seasons={self.season}&paper={self.paper}&zone={self.time_zone}" \
                    f"&chapter={self.chapter}&order=asc&offset={self.offset}"

    def print_link(self):
        print(self.link)

    def find_offset(self):
        response = urllib.request.urlopen(self.link)
        webpage = response.read().decode('utf-8')
        for line in webpage.split('\n'):
            if "offset=" in line:
                print(line)

    def scrape_paper_auto(self):
        response = urllib.request.urlopen(self.link)
        webpage = response.read().decode('utf-8')
        for line in webpage.split('\n'):
            if "/questions" in line:
                self.question_found = True
                parsed = line[line.find("/questions"):]
                parsed = parsed.replace("""');">Question</a>""", "")
                parsed = parsed.replace("""');">Answer</a>""", "")
                parsed = parsed.replace("', '", " ")
                final = parsed.split()[0] + " " + ' '.join(parsed.split()[2:])
                print(final)

    def scrape_paper_manual(self, file):  # cos some of exam mate stuff is locked without subscription. I can manually download questions html file from 2016 onwards
        file = open(file, 'r')
        file_lines = file.readlines()
        for line in file_lines:
            if "/questions" in line:
                self.question_found = True
                parsed = line[line.find("/questions"):]
                parsed = parsed.replace("""');">Question</a>""", "")
                parsed = parsed.replace("""');">Answer</a>""", "")
                parsed = parsed.replace("', '", " ")
                final = parsed.split()[0] + " " + ' '.join(parsed.split()[2:])
                print(final)

