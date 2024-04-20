import socket

def get_local_ip():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Connect to an external server
        s.connect(("8.8.8.8", 80))
        
        # Get the local IP address
        local_ip = s.getsockname()[0]
        
        # Close the socket
        s.close()
        
        return local_ip
    except Exception as e:
        print("Error:", e)
        return None

# Get and print the local IP address
local_ip = get_local_ip()
if local_ip:
    print("Your local IP address is:", local_ip)
else:
    print("Failed to retrieve the local IP address.")
