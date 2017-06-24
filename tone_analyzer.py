import json
from watson_developer_cloud import ToneAnalyzerV3
import os

tone_analyzer = ToneAnalyzerV3(
  username="1a206506-067d-41e9-b44c-1de167d657e3",
  password='hnscmOzyYOmU',
  version='2016-05-19'
)

with open('tone.txt') as f:
	text = ' '.join([x.strip() for x in f.readlines()])
	print(text)
	tone = tone_analyzer.tone(text)

	print(document_tone)

print(json.dumps(tone, indent=2))