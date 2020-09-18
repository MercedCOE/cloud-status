import json
import requests
import xmltodict


def get_data(url) -> str:
    return requests.request("GET", url).text

def get_google() -> dict:
    gas = 'https://www.google.com/appsstatus/json/en'
    result = json.loads(get_data(gas)[16:-2])
    google = {}
    for service in result['services']:
        google[service['id']] = {}
        google[service['id']]['name'] = service['name']
    for message in result['messages']:
        if not 'message' in google[message['service']]:
            google[message['service']]['message'] = message
        else:
            if message['time'] > google[message['service']]['message']['time']:
                google[message['service']]['message'] = message
    return google

def get_gsuite() -> dict:
    gs = 'https://www.google.com/appsstatus/rss/en'
    result = xmltodict.parse(get_data(gs))
    channel = dict(result['rss']['channel'])
    if 'item' in channel:
        items = dict(channel['item'])
        if type(items) is not 'list':
            items = [items]
        for index, item in enumerate(items):
            items[index] = dict(item)
        posts = [items[0]]
        for item in posts:
            for x in [i['description'] for i in posts]:
                if item['description'] not in x:
                    posts.append(item)
        return posts
    else:
        return None

def get_zoom() -> dict:
    zs = 'https://14qjgk812kgk.statuspage.io/api/v2/summary.json'
    return json.loads(get_data(zs))

def get_apple() -> dict:
    ap = 'https://www.apple.com/support/systemstatus/data/system_status_en_US.js'
    service_classes = {}
    prodjson = get_data(ap)
    service_classes['prod'] = json.loads(prodjson)['services']
    result={}
    for service in service_classes['prod']:
        serviceName = service.get('serviceName')
        if not service.get('events'):
            result[serviceName] = [{'eventStatus': 'up'}]

        else:
            result[serviceName] = service.get('events')
    return result

def get_adobe() -> dict:
    ad = 'https://data.status.adobe.com/adobestatus/currentstatus'
    result = get_data(ad)
    return result