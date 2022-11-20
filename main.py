import json

def lambda_handler(event, context):
    # can pass event/context into the main function
    # if required
    return main()

def main():
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

if __name__ == '__main__':
    # If main takes an event and context a mock version for local
    # testing should be passed in
    print(main())
