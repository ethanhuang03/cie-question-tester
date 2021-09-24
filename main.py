import paper_scraper as ps


def scrape_exam_mate(year_list, category=3, subject=17):  # cat 3: IG, subject 11: Maths
    for year in year_list:
        for season in ["summer", "winter"]:
            for time_zone in [1, 2, 3]:
                for paper in [1, 2]:  # create algorithm to find how many papers
                    for page_number in range(0, 100):
                        paper = ps.ExamMatePaper(category=category, subject=subject, year=year, season=season,
                                                 time_zone=time_zone, paper=paper, website_page=page_number)
                        paper.scrape_paper()
                        if not paper.question_found:
                            break


def scrape_pdf_paper(category, subject_code, years, mark_scheme=False):
    # year, season, time_zone, paper,
    years = [str(x) for x in years]
    seasons = ["summer"]
    time_zones = ["1"]
    past_paper = ps.PDFPaper(category=category, subject_code=subject_code)

    for year in years:
        past_paper.input_year(year)
        codes = past_paper.season_count
        for season in seasons:
            for time_zone in time_zones:
                for paper in range(1, 2):
                    code = season[0]+str(paper)+time_zone
                    if code in codes:
                        past_paper = ps.PDFPaper(category=category, subject_code=subject_code,
                                                 year=year, season=season, time_zone=time_zone, paper=paper,
                                                 mark_scheme=mark_scheme)
                        past_paper.create_link()
                        print(past_paper.link)
                        past_paper.scrape_paper()


if __name__ == '__main__':
    years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    scrape_exam_mate(year_list=years)
    # scrape_pdf_paper(category="Cambridge%20IGCSE", subject_code="0470", years=years)
