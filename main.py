import logging
import requests
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler("status.log"),
                        logging.StreamHandler()
                    ]
                    )


if __name__ == "__main__":    
    r = requests.get('https://go-germany-api.onrender.com/status')
    logging.info(r)