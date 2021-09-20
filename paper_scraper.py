import urllib.request, urllib.error, urllib.parse
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

    def return_link(self):
        return self.link

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


class PDFPaper(object):
    def __init__(self, category, subject_code, year, season, time_zone, paper, mark_scheme=False):
        self.category = category  # "A Levels", "Cambridge IGCSE"
        self.subject_code = subject_code
        self.year = year
        self.season = season  # "summer", "winter"
        self.time_zone = time_zone
        self.mark_scheme = mark_scheme
        self.paper = paper
        self.link = ""
        self.subject = ""

    def print_link(self):
        print(self.link)

    def subject_finder(self):
        '''
        traverse through html of " (refer to above)
        find string self.subject_code
        do some string manipulation

        self.subject = f"{subject} ({self.subject_code})"  # as a string: eg Economics (9708)
        '''
        print(f"https://papers.gceguide.com/{self.category}/")
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
                print(subject)

    def create_link(self):
        if self.mark_scheme:
            ms = "ms"
        else:
            ms = "qp"
        self.link = f"https://papers.gceguide.com/{self.category}/{self.subject}/{self.year}/" \
                    f"{self.subject_code}_{self.season[0]}{self.year[-2:]}_{ms}_{self.paper}{self.time_zone}"

    def scrape_paper(self):
        # downloads the paper with link self.link
        pass
