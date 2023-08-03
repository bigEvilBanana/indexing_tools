import csv
import json
import time

import httplib2
from loguru import logger
from oauth2client.service_account import ServiceAccountCredentials


class GoogleIndexationAPI:
    def __init__(self, key_files: list[str], urls_file_path: str):
        self.key_files = key_files
        self._key_file_index = 0
        self.urls_list = urls_file_path
        self._urls_processed = 0

    @property
    def key_file(self):
        return self.key_files[self._key_file_index]

    @property
    def urls_processed(self):
        return self._urls_processed

    @urls_processed.setter
    def urls_processed(self, value):
        self._urls_processed = value

    def update_key_file_index(self):
        self._key_file_index += 1
        logger.warning('Key file updated')
        if self._key_file_index > len(self.key_files) - 1:
            logger.error("Key files are ended. Start the script tomorrow.")
            raise StopIteration()
        logger.error("Sleeping for 5 seconds.")
        time.sleep(5)

    def get_urls(self):
        try:
            with open(self.urls_list, 'r', encoding='utf-8') as f:
                urls = [line.strip() for line in f]
            return urls
        except Exception as e:
            logger.error(f'Error while reading urls from file ::: {e}')
            exit()

    def send_request(self, url):
        """
        Makes a request to Google Indexing API
        :return: Content: Response from API
        """
        api_scopes = ["https://www.googleapis.com/auth/indexing"]
        api_endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.key_file, scopes=api_scopes)
        method = 'URL_UPDATED'
        try:
            http = credentials.authorize(httplib2.Http())
            r_content = json.dumps({"url": url, "type": method}).encode('utf-8')
            response, content = http.request(api_endpoint, method="POST", body=r_content)
            log = [url, method, response.status, content.decode('utf-8')]
            return log
        except Exception as e:
            logger.error(f'{e}, {type(e)}')
            return None

    def parse_response(self, content):
        """Parses error response"""
        try:
            json_line = json.loads(content)
            result = [json_line['error']['message'], json_line['error']['status'], self.key_file]
        except Exception as e:
            result = ['API response parse error', e]
        return result

    def indexation_worker(self):
        logger.info('Processing... Please wait')

        urls = self.get_urls()

        with open('report_log.csv', 'w', encoding='utf-8', newline='') as f:
            my_csv = csv.writer(f, delimiter='\t')
            header = ['URL', 'METHOD', 'STATUS_CODE', 'ERROR_MESSAGE', 'ERROR_STATUS', 'KEY FILE']
            my_csv.writerow(header)

            for url in urls:
                logger.debug(f'Sending {url}')
                result = self.send_request(url)
                if not result:
                    logger.info('Empty response, skipping the url')
                    continue

                log = result[0:3]

                if result[2] == 200:
                    self.urls_processed += 1
                elif result[2] == 429:
                    self.update_key_file_index()

                if result[2] != 200:
                    log.extend(self.parse_response(result[3]))

                my_csv.writerow(log)
                logger.debug(log)


def index_api():
    # NOTE: add ALL your account credits json files
    key_files = [
        'credits/your-credits-example.json',
    ]

    # NOTE: put your urls that you want to index to the file
    urls_file = 'urls.txt'

    api = GoogleIndexationAPI(key_files=key_files, urls_file_path=urls_file)
    try:
        api.indexation_worker()
    except StopIteration:
        logger.error("Exiting...")

    logger.info(f"Done! We've sent {api.urls_processed} URLs to Googlebot. You can check report in report_log.csv")


if __name__ == '__main__':
    index_api()
