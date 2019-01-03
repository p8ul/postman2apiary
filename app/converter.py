"""
    Tool for generating Blueprint API markup or the Apiary API
    from a Postman collection
    Author: Paul Kinuthia
"""

import json
from urllib.parse import urlparse


class PostmanToApiary:
    def __init__(self, data={}):
        self.file = data.get('postman_collection')
        self.data = {}
        self.name = ''
        self.description = ''
        self.domain = ''
        self.api_version = '/api/v1'
        self.output_file = data.get('output_file')
        self.file_format = 'FORMAT: 1A'
        self.requests = []
        self.get_data()

    def get_data(self):
        try:
            with open(self.file, encoding='utf-8') as f:
                self.data = json.loads(f.read())
        except Exception as e:
            print('[x] :( Some error occurred')
            print(e)
            exit(0)
        self.name = self.data.get('name', '')
        self.description = self.data.get('description', '')
        self.get_url_info()

    def write(self):
        # write document introduction
        doc = open(self.output_file, 'w+')
        doc.write(self.file_format + '\n')
        doc.write('HOST: ' + self.domain + '\n\n')
        doc.write('# ' + self.name + '\n\n')
        if self.description:
            doc.write(self.description)
        doc.close()

        for request in self.data.get('requests'):
            self.process_requests(request)

    def process_requests(self, request):
        url = urlparse(request.get('url'))
        path = url.path.replace(self.api_version, '')
        self.domain, description = url, request.get('description')
        method, name = request.get('method', ''), request.get('name', '')
        content_type = 'application/json'
        collection_name = '## ' + name + ' [' + path + ']\n'
        title = '### ' + name + ' [' + method + ']'
        req = '+ Request (' + content_type + ')'
        resp = '+ Response 201 (' + content_type + ')'

        doc = open(self.output_file, 'a')
        doc.write(collection_name + '\n\n')
        doc.write(title + '\n')
        doc.write(description + '\n\n')
        try:
            if method == "POST":
                doc.write(req + '\n\n')
                json_data = json.loads(request.get('rawModeData'))
                json.dump(json_data, doc, indent=8, sort_keys=True, ensure_ascii=False)
                doc.write('\n\n\n')
        except Exception as e:
            pass

        doc.write(resp + '\n\n\n')
        doc.close()

    def get_url_info(self):
        url = self.data.get('requests')[0].get('url')
        domain = urlparse(url)
        self.domain = url.replace(domain.path, '') + self.api_version


if __name__ == "__main__":
    app = PostmanToApiary('data.json')
    # app.main()

