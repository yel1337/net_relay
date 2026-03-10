import ssl
import socket

# Just to start it off 
# fetching server's certificate
class SSL_Utils:
    def get_cert():
        hostname="www.google.com"
        ctx = ssl.create_default_context()
        conn = ctx.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
        port = 443
        conn.connect((hostname, port))
        # Print cert 
        return f"{conn.getpeercert()}"
    