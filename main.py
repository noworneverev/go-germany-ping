# import subprocess

# host = "www.goo12345gle.com"
host = "go-germany-api.onrender.com"

# ping = subprocess.Popen(
#     ["ping", "-c", "4", host],
#     stdout = subprocess.PIPE,
#     stderr = subprocess.PIPE
# )

# out, error = ping.communicate()
# print (out)

# import platform    # For getting the operating system name
# import subprocess  # For executing a shell command
import logging
import requests
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler("status.log"),
                        logging.StreamHandler()
                    ]
                    )

# def ping(host):
#     """
#     Returns True if host (str) responds to a ping request.
#     Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
#     """

#     # Option for the number of packets as a function of
#     param = '-n' if platform.system().lower()=='windows' else '-c'

#     # Building the command. Ex: "ping -c 1 google.com"
#     command = ['ping', param, '1', host]

#     return subprocess.call(command) == 0

if __name__ == "__main__":
    # res = ping(host)
    r = requests.get('https://go-germany-api.onrender.com/status')
    logging.info(r)
    # if res:
    #     logging.info(f"Ping {host} successfully.")
    # else:
    #     logging.warning(f"{host} does not respond.")
