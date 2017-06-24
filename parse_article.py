from newspaper import Article
import os

print([os.path.abspath(name) for name in os.listdir(".") if os.path.isdir(name)])

url = 'http://www.telegraph.co.uk/business/2017/06/24/north-sea-debt-battle-drag-oil-price-forecasts-slashed/'

a = Article(url)

a.download()
a.parse()

print(' '.join([x.strip() for x in a.text.split()]))