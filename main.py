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


def scrape_pdf_paper(category, subject_code, mark_scheme=False):
    # year, season, time_zone, paper,
    years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    for year in years:
        for season in ["summer", "winter"]:
            for time_zone in [1, 2, 3]:
                for paper in range(0, 6):
                    past_paper = ps.PDFPaper(category=category, subject_code=subject_code,
                                        year=year, season=season, time_zone=time_zone, paper=paper, mark_scheme=mark_scheme)
                    past_paper.subject_finder()
                    past_paper.create_link()
                    print(past_paper.link)


if __name__ == '__main__':
    #scrape_pdf_paper(category="Cambridge IGCSE", subject_code=0620)
    #  scrape_exam_mate()
    past_paper = ps.PDFPaper(category="Cambridge IGCSE", subject_code="0620",
                             year=2020, season="summer", time_zone="1", paper="1", mark_scheme=False)
    past_paper.subject_finder()
