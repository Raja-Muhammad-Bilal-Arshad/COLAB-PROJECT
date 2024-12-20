        # In the mention task Programming for Cyber security  (Third   Script is extract ips )

#  here import the 're' pyhton module for working with regular expressions (what is reguler expression & why its need ? bcz, every Ip is bases some particuler reguler expression )  in this task we are extarcting the ip
import re

# here we define the function  to extract IP addresses from a log file (log file which we had done with file handling in the scrape data  file)
def extract_ips():
    # followed  1: Open the "logs.txt" file in the read mode we use r   (just reading data from the files)
    with open("logs.txt", "r") as file:
        logs = file.read()  # here reading  the entire file content into the 'logs' variable that we stored during dashboard scraping

    # Step 2: Define a regular expression pattern to match IPv4 addresses
    # - \b ensures the match starts and ends at a word boundary (e.g., no extra characters around the IP)
    # - \d{1,3} matches 1 to 3 digits (representing each part of the IP)
    # - \. matches the literal dot separating IP address segments
    ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

    # Step 3: Use re.findall() to find all matches of the pattern in the log content
    # - This returns a list of all matching IP addresses  here re means return all the ip pattern from the logs file
    ips = re.findall(ip_pattern, logs)

    # followed  4: we Open "ips.txt" in write mode to save  all the extracted IP addresses
    with open("ips.txt", "w") as file:
        # Loop through the list of IP addresses
        for ip in ips:

            file.write(ip + "\n")  # writing each ip address to the file with the next line

    #followed Step 5: Then print a confirmation message after saving the IP addresses
    print("IP addresses saved to ips.txt")

# Check if this script is being run directly (not imported into another program)
if __name__ == "__main__":
    # Call the extract_ips function to start the extraction process
    extract_ips()
