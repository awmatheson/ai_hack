#!/usr/bin/env python
# -*- coding: utf-8 -*-

from newspaper import Article
import newspaper
import os
import pandas as pd
import csv
import re
import nltk
import requests
import urllib2
from bs4 import BeautifulSoup


def get_page_data(url):

	# get html
	response = urllib2.urlopen(url, timeout=5)
	html = response.read()

	# make soup
	soup = BeautifulSoup(html)
	clickers = soup.findAll("td", { "class" : "f" })
	next_url = clickers[0].a
	next_url = next_url.get('href')
	print(next_url)

	# download urls
	paper = newspaper.build(url)

	date = url.split('/')[4]
	# with open("urls.txt", 'rb') as f:
	# 	urls = f.readlines()
	all_urls = soup.findAll("a")
	urls = []

	for article in all_urls:
		href = article.get('href')
		if 'articles/' in href:
			href = 'http://' + href
			urls.append(href.replace('http://http://','http//').replace('http:///','http://'))

	print(urls)

	with open('notebooks/onion/{}_onion_output.csv'.format(date), 'wb') as csvfile:
	    fieldnames = ['text','title']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    writer.writeheader()

	    for url in urls:
	    	if '/video/' not in url:
				a = Article(url)

				a.download()
				a.parse()

				text = ''.join(re.sub('[£—""…\n\"%]', ' ', a.text))
				title = re.sub('[£—""…\n\"%]', ' ',a.title.strip())
				print(title)

				writer.writerow({'text':text.encode('utf-8'),'title':title.encode('utf-8')})

	if next_url is None:
		print('no url')
	else:
		get_page_data(next_url)

if __name__ == '__main__':
	url = 'http://web.archive.org/web/20110403100226/http://www.theonion.com/'
	get_page_data(url)

