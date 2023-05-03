#loadxmlto elastic reads multiline xml from an url response
#built for a customer to insert documents into elastic directly from an Url scrape
#Satish Bomma
#05.03.2023


import requests
from datetime import datetime
import json
import yaml
import logging
import xmltodict
import xml.etree.ElementTree as ET
from elasticsearch import Elasticsearch

#date time setup for the script
log = logging.getLogger("ProcessLog")
log.info('Setting Datetime:')

now = datetime.now();
dt_string = now.strftime("%m%d%Y %H:%M:%S")
logging.info('Executing Ingest Script:', dt_string)

#functions
def read_from_file():
    with open('config.yml') as f:
        data = yaml.load (f, Loader=yaml.FullLoader)
        return data

#function to execute search


def call_get (url):
    print ("call url", url)
    response12 = requests.get(url)
    return response12.text



# Main function to get executed to process rest of the files
if __name__ == '__main__':
    log = logging.getLogger("scriptlog")
    log.info('Setting Datetime:')

    #read config from yaml file.
    data=read_from_file()
    username = data['username']
    password = data['password']
    url = data['url']
    cloud_id1 = data['cloud_id']
    request_url= data['request_url']
    index_name=data['index_name']

    log.info("username:",username)
    log.info ("username:", username)
    log.info ("password:", password)
    log.info ("url:", url)



    es=Elasticsearch(cloud_id=cloud_id1,basic_auth=(username,password))
    print (es.info())

    response1 = call_get(request_url)
    ida=0
    root = ET.fromstring(response1)
    for doc1 in root.findall('document'):
        doc_xml = ET.tostring(doc1)
        python_dict=xmltodict.parse(doc_xml)
        json_string=json.dumps(python_dict)
        ida = ida+1
        print (ida)

        resp = es.index(index=index_name,id=ida,document=json_string)
        print ("-resp-", resp)


    exit(1)


