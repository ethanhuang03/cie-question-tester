import paper_scraper as ps


def scrape_exam_mate(category=3, subject=11):  # cat 3: IG, subject 11: Maths
    #
    year = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]  # 2016 onwards is locked
    for year in year:
        print(year)
        for page_number in range(0, 10):
            print(year, page_number)
            paper = ps.ExamMatePaper(category=category, subject=subject, year=year, website_page=page_number)
            paper.scrape_paper_auto()
            if not paper.question_found:
                break


def scrape_pdf_paper(category, subject_code, years, mark_scheme=True):
    # year, season, time_zone, paper,
    years = [str(x) for x in years]
    past_paper = ps.PDFPaper(category=category, subject_code=subject_code)

    for year in years:
        past_paper.input_year(year)
        codes = past_paper.season_count
        for season in ["march", "summer", "winter"]:
            for time_zone in ["1", "2", "3"]:
                for paper in range(1, 7):
                    code = season[0]+str(paper)+time_zone
                    if code in codes:
                        past_paper = ps.PDFPaper(category=category, subject_code=subject_code,
                                                 year=year, season=season, time_zone=time_zone, paper=paper,
                                                 mark_scheme=mark_scheme)
                        past_paper.create_link()
                        print(past_paper.link)


if __name__ == '__main__':
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    scrape_pdf_paper(category="Cambridge%20IGCSE", subject_code="0455", years=years)
    '''
    scrape_exam_mate()
    past_paper = ps.PDFPaper(category="Cambridge%20IGCSE", subject_code="0452",
                             year="2011", season="summer", time_zone="1", paper="1", mark_scheme=True)
    past_paper.subject_finder()
    past_paper.partial_link()
    past_paper.scanner()
    '''