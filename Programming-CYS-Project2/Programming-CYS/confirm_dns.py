       # In the mention task Programming for Cyber security  (Fourth Script is confirm dns )

# socket is very populer pyhton library  of networking  why we are using here ? bcz when we send request to the server  we have to chose specific ports it happens in all caese while docker to docker communication or simple ssh connection  etc  every socket have its own default post while we have to run on different port we can change by using chmod or by port number
# Importing  the socket module for network-related operations
import socket

# here we define the function to check that ip we extracted earlies in the third file ip etxract.py
def syn_scan(host):
   # further we specifies the Tcp connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

     # here to set  the Timeout built in function
        sock.settimeout(1)  # Timeout set to 1 second  u can chnage the time

       # here i try to connect on the port 53 of  dns server
        result = sock.connect_ex((host, 53))   # it return 0 if successful  like if its connect properly

        # And also return true if connection is built other wise its return false
        return result == 0

# here we define the function  to perform reverse DNS lookup for  each IP address
def reverse_dns(ip):
    try:
        # in the following scenerio i try another way but, its working in that case  so that's why here   we are providing  gethostbyaddr to resolve the IP to a domain name
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        # if there is no record then simply it's return none or nUll
        return None

# to breakdowning the code here is the seperate function to confirm DNS servers from a list of IP addresses that we extracted in the extrach ip's file
def confirm_dns():
    # here again Open the file "ips.txt" in read mode and read all lines  seperate
    with open("ips.txt", "r") as file:
        ips = file.readlines()  # read all the list of the ip's

    # In above the we read the all the ips now  create the seperate file  to store the that which ip (ip that we extracted)  is working  or not
    with open("confirmed_dns.txt", "w") as file:

        for ip in ips:
            ip = ip.strip()  # here use strip to remove the white space  or newline

          # here  Perform a SYN scan on port 53 (here port 53 we already set )of the current IP
            if syn_scan(ip):
                # here is the checking statemnt if port 53 is open then make reverse dns lookup
                domain = reverse_dns(ip)

                # simply if  domain name is resolved, save the result to the file (confirmed_dns.txt)
                if domain:
                    file.write(f"DNS Server at {ip} : {domain}\n")

  # here we print the successful message after  process all  the ip's
    print("DNS servers saved to confirmed_dns.txt")

# Main function
if __name__ == "__main__":
    # to call the confirm_dns function to start the DNS confirmation process
    confirm_dns()
