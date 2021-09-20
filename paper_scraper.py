import requests


class ExamMatePaper(object):
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
        self.cookies = {}

    def return_link(self):
        return self.link

    def scrape_paper_auto(self):
        session = requests.Session()
        response = session.get(self.link, headers={'User-Agent': 'Mozilla/5.0'}, cookies=self.cookies)
        webpage = response.text
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


class PDFPaper(object):
    def __init__(self, category="", subject_code="", year="", season="", time_zone="", paper="", mark_scheme=False):
        self.category = category  # "A Levels", "Cambridge IGCSE"
        self.subject_code = subject_code
        self.year = year
        self.season = season  # "summer", "winter"
        self.time_zone = time_zone
        self.mark_scheme = mark_scheme
        self.paper = paper
        self.season_count = set()
        self.link = ""
        self.subject = self.subject_finder()
        self.partial_link = ""

    def subject_finder(self):
        session = requests.Session()
        response = session.get(f"https://papers.gceguide.com/{self.category}/", headers={'User-Agent': 'Mozilla/5.0'})
        webpage = response.text
        for line in webpage.split('\n'):
            if self.subject_code in line:
                subject_line = line
                index = subject_line.find(self.subject_code)
                subject = subject_line[:index+5]
                subject = subject[::-1]
                subject = subject[:subject.find("'")]
                subject = subject[::-1]
                subject = subject.replace(" ", "%20")
                return subject

    def print_link(self):
        print(self.link)

    def input_year(self, year):
        self.year = year
        self.partial_link = f"https://papers.gceguide.com/{self.category}/{self.subject}/{self.year}/"
        self.scan_seasons()

    def create_link(self):
        if self.mark_scheme:
            ms = "ms"
        else:
            ms = "qp"
        self.link = f"https://papers.gceguide.com/{self.category}/{self.subject}/{self.year}/" \
                    f"{self.subject_code}_{self.season[0]}{self.year[-2:]}_{ms}_{self.paper}{self.time_zone}.pdf"

    def scrape_paper(self):
        # downloads the paper with link self.link
        pass

    def scan_seasons(self):
        ms = "q" if self.mark_scheme else "m"
        session = requests.Session()
        response = session.get(self.partial_link, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = response.text
        temp = ""
        for line in webpage.split('\n'):
            if "file" in line:
                temp += line
        line = temp
        for count, value in enumerate(line):
            if count + 10 > len(line):
                break
            if (value == "s" or value == "w" or value == "m") and (line[count+4] in ms):
                temp = value+line[count+7]+line[count+8]
                self.season_count.add(temp)
