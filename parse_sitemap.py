import xml.etree.ElementTree as ET

import requests
from loguru import logger


class SitemapParser:
    def __init__(self, sitemap_url: str):
        self.url = sitemap_url

    def parse_sitemap(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            sitemap_content = response.text
            root = ET.fromstring(sitemap_content)

            urls = [url_elem.text for url_elem in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
            logger.info(f"Successfully extracted {len(urls)} URLs from the sitemap.")
            return urls
        else:
            logger.error(f"Failed to retrieve the sitemap. Status code: {response.status_code}")

    @staticmethod
    def save_urls_to_file(urls):
        with open('sitemap_urls.txt', 'w') as file:
            file.write('\n'.join(urls))
            logger.success(f'Saved {len(urls)} urls to file.')


def main():
    url = 'https://example.com/sitemap.xml'  # put your path to sitemap here

    sitemap_parser = SitemapParser(url)
    urls = sitemap_parser.parse_sitemap()
    sitemap_parser.save_urls_to_file(urls)


if __name__ == '__main__':
    main()
