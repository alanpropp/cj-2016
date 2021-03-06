#Databases

##http://www.data.gov/
- This website's strengths include the fact that it is possible to browse topics in order to narrow down the choices from which you
  search. It also allows you to further narrow by location. While the website is rather slow, it does also allow the user to narrow
  based on type of file. It has nearly 200,000 databases - a respectable number - and the UI allows the user to easily see what types
  of file he/she can download. However, the fact that the website places such an emphasis on "updates" is rather irritating and not 
  likely what the user is looking for

##http://www.opendatanetwork.com/
- This website has a pretty UI/splash page, and also allows the user to immediately and rapidly filter based on topic AND geographic
  region on the homepage. It seems to be weaker once the user has looked up a keyword - they can subsequently only filter by publisher
  and category, but not geographic region. It is also unclear how many total databases the website contains. While it is nice to be able
  to combine categories searched, data.gov has more filtering options and is easier to browse if there isn't something explicit in mind.

##http://data.cityofpaloalto.org/home
- This website is **extremely** unintuitive and difficult to filter based on category, narrow geographic location, anything along those lines.
  It is relatively slow and unclear at first glance in what formats the data is able to be downloaded. Once viewing the actual dataset
  online it is fine and readable, but getting to that point and downloading the data for use in python seems unwieldy and unintuitive.
  The dataset quantity appears understandably limited, as well. Overall, it seems relatively inaccessible without an extensive acquaintance
  period.

##http://www.fec.gov/data/DataCatalog.do?format=html
- This website has a limited number of datasets, although it is easy to see at first glance in what formats they are available to be 
  downloaded. It's also relatively easy to toggle between years for different datasets. It also handily allows to customize data and
  see data summaries/field descriptions. Overall, however, the website is relatively clunky and not super easy on the eye, and the 
  databases are not that easy to actually read online

##https://data.gov.uk/
- The splash page is (to me) not as impressive as either of the first 2 databases listed above, but once you get into the 'datasets'
  portion, it is relatively easy to navigate based on theme, format, API, etc. - anything you would really need. In fact, it allows 
  the user to filter on a lot more criteria than the other sites. And, the specific database pages are simply laid out with all relevant 
  information and easy to find download buttons. Overall, easy to navigate, and simplistic.

#Find stop-and-frisk: Giancarlo Esposito
- To find the record, we first know (from the article) that the stop-and-frisk must have occurred in 2012 or before, so we ignore the     2013-2015 archives. Then, I would loop through the CSV zip files (they all have the same formatted link:   www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/YEAR_sqf_csv.zip, with whatever year between 2003-2015 substituted in for YEAR; thus, looping would be a simple replacement of 1 or 2 characters in a string each time) and open them. I would open each zip file - working from 2012 backwards - and go line by line down through the CSV. For each line I would see if the following were true: dob = 4261958 (given that that is probably the most distinguishing feature of the actor). If so, I would confirm that sex = M, race = B, frisked = Y, ht_feet = 5, 6<ht_inch<10. If all that is true, we can most likely safely assume that it is Giancarlo Esposito, thus confirming that line as the true record for Esposito.
