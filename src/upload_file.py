
import requests

binary_data = bytearray([1, 2, 3, 4])

files = {'file': ('foo.bin', binary_data)}
data = {'job_id': 'job42',
        'client_id': 93}

requests.post('http://localhost:5000/', files=files, data=data)
