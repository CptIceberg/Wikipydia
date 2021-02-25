#!/usr/bin/env python3

import requests
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('query', type=str, help="You query")
parser.add_argument("-l", "--language", dest="language", default="en", help="Language selection (eg 'fr', 'en' etc...)")
parser.add_argument("-v", "--verbose", dest="verbose", help="Show the first 10 lines of the article", action='store_true')
parser.add_argument("-f", "--full", dest="full", help="Show the full article", action='store_true')
args = parser.parse_args()

if args.verbose:
    v = "&exsentences=10"
elif args.full:
    v = ""
else:
    v = "&exintro"

response = requests.get(f"https://{args.language}.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext{v}&titles={args.query}&format=json")
data = list(response.json()['query']['pages'].values())[0]
if "extract" in data :
    print(data['extract'])
else:
    print(f"No result found for {args.query}, you can also try with another language parameter.")


