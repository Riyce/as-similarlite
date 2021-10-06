import re

from similar.etl.parser.base import BaseTransportParser


class LightParser(BaseTransportParser):
    URL_SIMILAR = (
        'https://play.google.com/store/apps/collection/' +
        'cluster?clp={clp}&hl={lang}&gl={country}'
    )

    def __init__(self, transport):
        super(LightParser, self).__init__(transport)
        self._RE_APPS = re.compile(r'/store/apps/details\?id=([.\w]+)"><div')

    def extract(self, clp, lang='en_US', country='US'):
        url = self.URL_SIMILAR.format(
            clp=clp,
            lang=lang,
            country=country
        )
        data = self._transport.extract(url, return_notfound='')
        if data is not None:
            if data == '':
                return []

            return self._RE_APPS.findall(data)
