#!/usr/bin/python3
import requests, csv
iq_session = requests.Session()
iq_session.auth = requests.auth.HTTPBasicAuth("admin", "admin123")
iq_url = "http://localhost:8070"
file_csv = "iq_api.csv"

def outputCSV(api):
    data = iq_session.get(f'{iq_url}{api}').json()
    if isinstance(data, (dict)):
        data = data[list(data.keys())[0]]
    if isinstance(data, (list)):
        data_file = open(file_csv, 'w') 
        csv_writer = csv.writer(data_file) 
        count = 0
        for item in data: 
            if count == 0: 
                header = item.keys()
                csv_writer.writerow(header) 
                count += 1
            csv_writer.writerow(item.values()) 
        data_file.close()

outputCSV('/api/v2/applications')