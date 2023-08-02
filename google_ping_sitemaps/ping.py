from time import sleep

import requests
from loguru import logger


def ping():
    urls = [
        'https://example.com/sitemap.xml',
    ]
    base = 'https://www.google.com/ping?sitemap='

    for url in urls:
        url = f'{base}{url}'
        logger.info(f'Requesting url {url}')
        r = requests.get(url)
        if r.status_code == 200:
            logger.info(f'\t >>> Good. Sitemap sent.')
        else:
            logger.warning(f'Bad request. Status code: {r.status_code}')
        sleep(0.2)  # sleep for 0.2 seconds to be less spammy


if __name__ == '__main__':
    ping()
