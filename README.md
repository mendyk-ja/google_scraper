# google_scraper

This project is written in Python programming language. It's based on BeautifulSoup library for web scraping. It allows us to make some automatization during information search in Google.
	
1. Project code starts with importing libraries needed for the rest of the code.
2. It opens keywords.txt file to get information about keywords.
3. After getting each keyword it makes Google query with that keyword and opens it in browser.
4. It scraps information about the total numbers of results.
5. It writes this information into CSV file.
5. It goes in the loop to every container, which storages a link and scraps it.
6. It writes these links into CSV file.
		Program can be improved by:
	- making code more clean through putting functionalities in functions
	- handling exceptions (for excemple, when file keywords.txt doesn't exist)
		Risks associated with using such a program:
	- Google can block IP adress used for running this code (necessity to use VPN/proxy) 
