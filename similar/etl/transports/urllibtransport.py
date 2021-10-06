import urllib.request
import urllib.error

from similar.etl.transports.exceptions import NotFound


class UrllibTransport:
    _REPEATS = 3
    _TIMEOUT = 10

    def extract(self, url, return_notfound=None):
        repeats = self._REPEATS

        while repeats:
            try:
                with urllib.request.urlopen(url, timeout=self._TIMEOUT) as f:
                    data = f.read().decode('utf-8')
                    return data
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    if return_notfound is not None:
                        return return_notfound
                    else:
                        raise NotFound()
                # raise e
            # except http.client.IncompleteRead as e:
            except OSError as e:
                pass
                # raise e

            repeats -= 1
