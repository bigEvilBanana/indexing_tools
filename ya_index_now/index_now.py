import json
import time

import requests
from loguru import logger


class IndexNowRequester:
    def __init__(self, host: str, key: str):
        self.host = host
        self.key = key

    def get_urls_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]

    def request_index_now(self, urls):
        data = {
            "host": self.host,
            "key": self.key,
            "keyLocation": f"https://{self.host}/{self.key}.txt",
            "urlList": urls
        }

        while True:
            response = requests.post("https://yandex.com/indexnow", data=json.dumps(data))
            if response.status_code == 200:
                response_json = response.json()
                logger.info(f'Response status code {response.status_code}, message: {response_json}')
                return response_json
            elif response.status_code == 202:
                logger.info(f'Response status code {response.status_code}, retrying in 5 seconds...')
                time.sleep(5)
            else:
                response.raise_for_status()

    def index_now(self, file_path):
        urls = self.get_urls_from_file(file_path)
        self.request_index_now(urls)


def main():
    host = "example.com"  # put your domain here
    key = "ZZZYYYwIIMnPDYIUlPKMJKlleYQicC3kjlzvkoEGPoIyq"  # put your api key here
    file_path = "urls.txt"  # path to file with urls to index

    requester = IndexNowRequester(host, key)
    requester.index_now(file_path)


if __name__ == '__main__':
    main()
