# Postman2Apiary

 Tool for generating Blueprint API markup or the Apiary API from a Postman collection. 

Edit your postman collection requests with relevant names and description. Import postman_collection.json from postman2apiary/app/ for a quick demo on how to name and describe your requests.
Expected output should be something like [Polls api documentation](https://apiblueprint.org/documentation/examples/polls-api.html)

## Prerequisites
    python version 3+

## Installation
    ```
    git clone https://github.com/p8ul/postman2apiary.git
    cd app
    ```
## Usage
    CLI application Application takes three arguments.
    USAGE: $ python run.py [postman.json-file] [output-file.apid]

    postman.json-file: Json file exported from Postman collection
    output-file.apid: Name of your api markup file to be generated.

## Contribution
Contributions are greatly appreciated. What is most lacking is indentation on request & response expected json.
Tests would be super-greatly appreciated too.

### License
Postman2apiary is [MIT Licensed](https://github.com/p8ul/postman2apiary/blob/master/LICENSE)
