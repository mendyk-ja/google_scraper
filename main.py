from bs4 import BeautifulSoup
import requests
import csv

headers = {
    'User-agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

with open('keywords.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    html = requests.get(f"https://www.google.com/search?hl=en&q=site%3Ahttps%3A%2F%2Fwww.searchenginejournal.com%2F+"
                        f"{line}", headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    result_stats = soup.find('div', class_='appbar').text.replace(',', '')
    result_stats = result_stats[6:-24]
    csv_file = open("number_of_results.csv", 'a', newline="")
    tup = (line.strip(), result_stats.strip())
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(tup)
    csv_file.close()
    google_results = soup.find_all('div', class_='g')
    for google_result in google_results:
        link = google_result.find('a')['href']
        if link[0] == 'h':
            csv_file = open("links.csv", 'a', newline="")
#aby zrobic jednoelementowa tupie trzeba użyć składni:
#tup2 = (link.strip(),)
            tup2 = (line.strip(), link.strip())
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(tup2)
            csv_file.close()
