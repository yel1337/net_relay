import ssl
import socket

# Just to start it off 
# fetching server's certificate
class SSL_Utils:
    def __init__(self):
        self.ca_path = "/etc/ssl/certs/ca-bundle.crt"
    def get_cert(self, hostname, port):
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        # ctx.load_verify_locations(self.ca_path)
        conn = ctx.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
        conn.connect((hostname, port))
        # Return site's certificate
        return f"{conn.getpeercert()}"

    def _validate(self, hostname, port):
        # Validate server certificate againts root CA stored in /etc/ssl/certs/ca-bundle.crt
        try:
            cert_val = ssl.get_server_certificate(hostname, port, ca_certs = self.ca_path)
            if cert_val:
                return 1 
        except ssl.SSLVerificationError as e:
            return f"{e}"