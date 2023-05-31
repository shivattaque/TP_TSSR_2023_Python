# script de Web ScrapingURL Final v1.0
# to extract the TCP/UDP port list from the website frameip.com
# By shivattaque and ChatGPT (3.5)

# Importing modules
import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage containing the table
address = "https://www.frameip.com/liste-des-ports-tcp-udp/?plage="

# Specify the full file path for the CSV file
csv_path = "C:/Folder/Port_TCP_UDP.csv"

# Open the CSV file in write mode with the specified path, delimited by ";"
with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")

# Iterate through the pages
for page_number in range(1, 10):
    # Build the page URL
    url = address + str(page_number)

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the HTML content of the page
        html_content = response.content

        # Create a BeautifulSoup object from the HTML content
        soup = BeautifulSoup(html_content, "html.parser")

        # Find the table in the HTML page (use class, ID, or other CSS selectors depending on the page structure)
        table = soup.find("table")

        # Check if a table was found
        if table:
            # Iterate through the rows of the table
            rows = table.find_all("tr")
            for row in rows:
                # Extract the cells of each row
                cells = row.find_all("td")

                # Get the content of the cells and write a new row in the CSV file
                row_data = [cell.get_text(strip=True) for cell in cells]
                writer.writerow(row_data)

    else:
        print(f"The request for page {page_number} failed with code", response.status_code)


print("Table extraction completed. The data has been saved in the file Port_TCP_UDP.csv.")
