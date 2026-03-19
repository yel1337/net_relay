from net_ssl.ssl_utils import SSL_Utils as su
import argparse

class Net():
    def main():
        parser = argparse.ArgumentParser(prog='net_relay', description='%(prog)s')
        parser.add_argument('h', type=str, help='site hostname')
        parser.add_argument('p', type=int,  help='site port')
        args = parser.parse_args()

        x = su.get_cert(args.h, args.p)
        return print(x)

    if __name__ == "__main__":
        main()