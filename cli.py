import argparse
import requests
import json

def main():
     parser = argparse.ArgumentParser(description='ML Ops CLI Tool')
     parser.add_argument('--weight', type=int, required=True, help='Weight of the MLB player in pounds')
     args = parser.parse_args()

     payload = {'Weight': args.weight}
     response = requests.post('http://localhost:8080/predict', json=payload)
     print(json.dumps(response.json(), indent=4))

if __name__ == "__main__":
     main()