# Cambridge International Exams Papers Quiz System
An attempt at creating a past paper quiz app. Basically Save-My-Exams but with a self grading twist.
## Decomposition of CIEPQS / To Do:
* Scrape past papers
* Identify the useful information in the past paper
    * Find questions and diagrams related to questions
    * Find answers corresponding to the questions
* Store identified information in a central database
    * Attributes (not normalised) perhaps goes like:
        * ENTITY(Subject, Year, Season, Time Zone, Topic, Question, Answer)
* Select Subject, Year, Season, Time Zone, Topic
* Input number of questions to be tested on
* Compare user imputed questions to answer in database
    * Multi-choice: direct comparison
    * Long answers: check for keywords or formulae
* Award marks accordingly
* Predict grade
