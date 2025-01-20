import argparse
import requests
import time


def get_rate_limit(token):
    endpoint = "https://api.github.com/rate_limit"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {token}",
    }
    r = requests.get(endpoint, headers=headers)

    if r.status_code != 200:
        raise Exception()

    response = r.json()

    return response["rate"]


def populate_file(output_file, rate):
    now = time.time()

    with open(output_file, "a") as f:
        f.write(f"{now} {rate['limit']} {rate['remaining']}\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--token",
        dest="token",
        type=str,
        required=True,
        help="GitHub Token of user to monitor",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_file",
        type=str,
        required=True,
        help="Destination file to write rate limit monitoring",
    )
    args = parser.parse_args()

    print("Starting monitor...")

    while True:
        time.sleep(1)

        print("Get limits...")
        rate = get_rate_limit(args.token)
        print("Populate...")
        populate_file(args.output_file, rate)


if __name__ == "__main__":
    main()
