

import server
import sys


def main():
    inp = sys.argv[1]

    if (not inp.isdigit()):
        print("Wrong input format. Expected integer.")

    port = int(inp)
    if not (1024 <= port <= 64000):
        print("Error: expected a port number between 1024 and 64000 inclusive.")
        exit(-1)

    server.init(port)
    server.run()


if __name__ == "__main__":
    main()

