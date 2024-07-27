import sys
import requests

if len(sys.argv) not in [2, 3]:
    print(
        """
        Improper number of arguments: at least one is required and not more 
        than two are allowed: 
        - http server's address (required)
        - port number (defaults to 80 if not specified)
        """
    )
    sys.exit(1)

try: 
    port = sys.argv[2]
except IndexError: 
    port = 80

try: 
    port = int(port) 
    assert port in range(1, 65535)
except:  
    print("Port number is invalid - exiting.")
    sys.exit(2)

server_addr = sys.argv[1]

url = f"http://{server_addr}:{port}" 

try:
    response = requests.head(url)
except requests.exceptions.InvalidURL:
    print("The given URL '" + sys.argv[1] + "' is invalid.")
    exit(3)
except requests.exceptions.ConnectionError:
    print("Cannot connect to '" + server_addr + "'.")
    exit(4)
except requests.exceptions.RequestException:
    print("Some problems appeared - sorry.")
    exit(5)

print(response.status_code,  response.reason)

