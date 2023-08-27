import json

with open("sampledata/Userdata.json", "r", encoding="utf-8") as json_file:
    userData = json.load(json_file)
with open("sampledata/StreamingHistory.json", "r", encoding="utf-8") as json_file:
    userData = json.load(json_file)
with open("sampledata/Inferences.json", "r", encoding="utf-8") as json_file:
    userData = json.load(json_file)
