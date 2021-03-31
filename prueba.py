import requests
api = requests.get("https://api-escapamet.vercel.app/")

answers = [(api.json()[0]["objects"][2]["game"]["questions"][0]["answers"][x]) for x in range (5)]
print(answers)