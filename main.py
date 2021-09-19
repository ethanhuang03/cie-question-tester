import paper_scraper as ps

if __name__ == '__main__':
    # loop through year
        # loop through pages
    year = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    for year in year:
        print(year)
        ig_maths = ps.pastPaper(category=3, subject=11, year=year)
        ig_maths.scrape_paper()

