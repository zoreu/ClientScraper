# ClientScraper
client scraper in python

## Requirements

python 2.7+
requests

## Example:
```python
from ClientScraper import cfscraper
r = cfscraper.get('https://olhardigital.com.br')
print(r.text)
```

