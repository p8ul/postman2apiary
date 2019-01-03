import sys
from random import randint
from converter import PostmanToApiary


def msg():
    """ Print application usage """
    print("""
    Tool for generating Blueprint API markup or the Apiary API
    from a Postman collection.
    Application takes three arguments. Use python3
    USAGE: python run.py [postman.json-file] [output-file.apid]\n
    postman.json-file: Json file exported from Postman collection
    output-file.apid: Name of your api markup file to be generated.\n\n""")
    return True


def main():
    if len(sys.argv) < 3:
        msg()
        exit(0)

    data = dict()
    data['postman_collection'] = sys.argv[1] if sys.argv[1] else 'postman_collection.json'
    data['output_file'] = sys.argv[2] if sys.argv[2] else 'apiary' + str(randint(0, 9)) + '.apid'

    print(' * Generating api markup')
    app = PostmanToApiary(data)
    app.write()
    print(' * Done...:)')
    print(' * OUTPUT FILE: ' + data['output_file'])


if __name__ == '__main__':
    main()
