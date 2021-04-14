from datetime import date, datetime
from itertools import groupby
from operator import itemgetter
from typing import Optional


def string_to_date(datestring: str) -> Optional[date]:
    try:
        return datetime.strptime(datestring, '%Y-%m-%d').date()
    except ValueError:
        return None


def parse_analytics_date(request) -> dict:
    raw_date_from = request.GET.get('date_from')
    raw_date_to = request.GET.get('date_to')
    dates = dict()
    if raw_date_from:
        dates['created_at__date__gte'] = string_to_date(raw_date_from)
    if raw_date_to:
        dates['created_at__date__lte'] = string_to_date(raw_date_from)
    return dates


def analytics_prettify_data(raw_data):
    data = list()
    for key, value in groupby(raw_data, key=itemgetter('date')):
        data.append({'date': key, 'posts': [{'post': x['post'], 'likes': x['likes']} for x in list(value)]})
    return data
