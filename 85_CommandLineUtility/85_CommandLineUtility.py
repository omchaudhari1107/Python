import argparse
import requests


# IMP

def download_file(url, local_filename):
    # local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


parser = argparse.ArgumentParser()

# add command line argument
parser.add_argument("url", help="Url to download")
parser.add_argument("output", help="by which name do you ant to save your file")

# Convert argument strings to objects and assign them as attributes of the namespace. Return the populated namespace.
args = parser.parse_args()

# print(args.url)
download_file(args.url, args.output)
