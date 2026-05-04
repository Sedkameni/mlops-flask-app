import argparse
import requests
import json

def main():
    parser = argparse.ArgumentParser(description='Sentiment Analysis CLI Tool')
    parser.add_argument('--text', type=str, required=True, help='Text to analyze sentiment')
    parser.add_argument('--url', type=str, default='http://localhost:8080', help='Service URL')
    args = parser.parse_args()

    payload = {'text': args.text}
    response = requests.post(f'{args.url}/predict', json=payload)
    print(json.dumps(response.json(), indent=4))

if __name__ == "__main__":
    main()