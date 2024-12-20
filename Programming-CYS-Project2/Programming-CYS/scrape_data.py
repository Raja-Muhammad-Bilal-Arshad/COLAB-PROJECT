            # In the mention task Programming for Cyber security  (Second  Script is scrape_data)

# here we call the same library   for the requests   sending HTTP requests to the server
import requests

# BeautifulSoup  is the very populer library is pyhton which is commonly use for webscrapping content from the web page or dashboard
# Importing  BeautifulSoup from bs4 to parse HTML content
from bs4 import BeautifulSoup

# here the same  URL of the dashboard page  ( u can also replace this with the actual URL  according to your requiremnt )
url = "http://cyforsec.co.uk/dashboard"

# here we create a session to maintain the data like the hash or  sever queury that we have performed  or we have to perform further
session = requests.Session()

# The username and password for logging in
username = "admin"
password = "your_password_here"  # here u have to replace the actual password obtained from brute_force.py

# Define a function to scrape logs from the dashboard
# why logs we have to scrape ? bcz, at the backend there always be a logging method that maintain the websites or server related issue logs exist into many form  but commonly (warn,info etc)
def scrape_logs():
    # Following  Step 1: Log in to the website using the provided username and password
    session.post(url, data={"username": username, "password": password})

    # FollowingStep 2: Fetch the content of the dashboard page after logging in
    response = session.get(url)

    # Following Step 3: Parse the HTML content of the dashboard page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    #Following Step 4: Find all paragraph elements (`<p>`) with the class "logs" (these contain the logs we want to scrape)
    logs = soup.find_all("p", class_="logs")
   # above is the step to step procedure  to scrape data form the given dashboard url


    # here we have a done a file handling  (Open a file named "logs.txt" in write mode to save the logs) in this file we are  writing all the logs  to check if any error occur
    with open("logs.txt", "w") as file:
        # Loop through each log found and write its text content to the file
        for log in logs:
            file.write(log.text + "\n") #/n means adding the new line

    # while message displays after saving all the logs
    print("Logs saved to logs.txt")

# Checking  if this script is being run directly (not imported into another program)
if __name__ == "__main__":
    # Call the scrape_logs function to start the scraping process  further
    scrape_logs()
