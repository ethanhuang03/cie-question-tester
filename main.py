import paper_scraper as ps


def scrape_exam_mate(category=3, subject=11):  # cat 3: IG, subject 11: Maths
    #  2016, 2017, 2018, 2019, 2020, 2021
    year = [2009, 2010, 2011, 2012, 2013, 2014, 2015]  # 2016 onwards is locked
    for year in year:
        print(year)
        for page_number in range(0, 10):
            print(year, page_number)
            paper = ps.ExamMatePaper(category=category, subject=subject, year=year, website_page=page_number)
            paper.scrape_paper_auto()
            if not paper.question_found:
                break


if __name__ == '__main__':
    scrape_exam_mate()

