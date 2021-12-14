# Google Scraper
> This project is based on Python3 and BeautifulSoup4 library for web scraping. It allows us to make some automatization during information search in Google.

<!-- > Live demo [_here_](https://www.example.com). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)
<!-- * [License](#license) -->
<!-- * [Features](#features) -->
<!-- * [Screenshots](#screenshots) -->
<!-- * [Setup](#setup) -->
<!-- * [Usage](#usage) -->
<!-- * [Room for Improvement](#room-for-improvement) -->
<!-- * [Acknowledgements](#acknowledgements) -->
<!-- * [License](#license) -->
<!-- * [License](#license) -->


## General Information
- Web scraper, which allows us to make some automatization during information search in Google.
- Script showing scheme for coding web scraper with BeautifulSoup.
- The main purpouse for coding it was getting familiare with BeautifulSoup library.
<!-- You don't have to answer all the questions - just the ones relevant to your project. 
- The main purpouse for
- Why did you undertake it?
-->


## Technologies Used
- Python 3
- BeautifulSoup4 library

<!-- 
## Technologies Used
- Tech 1 - version 1.0
- Tech 2 - version 2.0
- Tech 3 - version 3.0
-->

<!-- 

## Features
List the ready features here:
- Awesome feature 1
- Awesome feature 2
- Awesome feature 3

-->

<!-- 

## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


<!-- 
## Setup
What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.
-->

## Usage
Google can block IP adress used for running this code (necessity to use VPN/proxy).

1. Project code starts with importing libraries needed for the rest of the code.
2. It opens keywords.txt file to get information about keywords.
3. After getting each keyword it makes Google query with that keyword and opens it in browser.
4. It scraps information about the total numbers of results.
5. It writes this information into CSV file.
5. It goes in the loop to every container, which storages a link and scraps it.
6. It writes these links into CSV file.

<!-- 

## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`
-->

## Project Status
Project is:  _complete_,  but some improvement still can be done.

<!-- 

## Project Status
Project is: _in progress_ / _complete_ / _no longer being worked on_. If you are no longer working on it, provide reasons why.

-->

## Room for Improvement

Room for improvement:
- making code more clean through putting functionalities in functions
- handling exceptions (for excemple, when file keywords.txt doesn't exist)

<!-- 

## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2

-->

<!-- 

## Acknowledgements
- This project was inspired by Eric Matthes
- This project was based on [Python Crash Course, 2nd Edition by Eric Matthes](https://nostarch.com/pythoncrashcourse2e).

-->

## Contact
Created by [Jacek Mendyk](https://www.linkedin.com/in/jacekmendyk/) - feel free to contact me!

<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
<!-- 

-->
