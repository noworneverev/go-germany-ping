import logging
import requests
from deta import app
# logging.basicConfig(level=logging.INFO,
#                     format="%(asctime)s [%(levelname)s] %(message)s",
#                     handlers=[
#                         logging.FileHandler("status.log"),
#                         logging.StreamHandler()
#                     ]
#                     )


url = 'https://go-germany-api.onrender.com/status'

def get(url):
    r = requests.get(url)
    print(r)
    # logging.info(r)

@app.lib.cron()
def cron_job(event):
    get(url)
    # return "running on a schedule"

# if __name__ == "__main__":    
#     get(url)
    