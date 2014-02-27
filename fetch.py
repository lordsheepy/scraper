import requests
import sys


def create_sample_1br():
    f = fetch_search_results(query='belltown', bedrooms=1)
    with open('apartments.html', 'w') as outfile:
        outfile.write(f[0])
    return


def fetch_search_results(
    query=None, minAsk=0, maxAsk=None, bedrooms=None
):
    search_params = {
        key: val for key, val in locals().items() if val is not None
    }
    if not search_params:
        raise ValueError("No valid keywords")

    base = 'http://seattle.craigslist.org/search/apa'
    resp = requests.get(base, params=search_params, timeout=3)
    resp.raise_for_status()
    return resp.content, resp.encoding


if __name__ == '__main__':
    create_sample_1br()
