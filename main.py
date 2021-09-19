import paper_scraper as ps

if __name__ == '__main__':
    # loop through year
        # loop through pages
    year = [2009, 2010, 2011, 2012, 2013, 2014, 2015]  # 2016 onwards is locked
    for year in year:
        print(year)
        for page_number in range(0, 10):
            print(year, page_number)
            ig_maths = ps.pastPaper(category=3, subject=11, year=year, website_page=page_number)
            ig_maths.scrape_paper_auto()
            if not ig_maths.question_found:
                break

#  2016, 2017, 2018, 2019, 2020, 2021
