import requests

def main():
	#res = requests.get("http://api.fixer.io/latest?base=USD&symbols=EUR")
	res = requests.get("http://data.fixer.io/api/latest?base=EUR&symbols=EUR&access_key=b483138f2ed2772152115a9dd776efc2")
	if res.status_code != 200:
		raise Exception("ERROR: API request unsuccessful.")
	data = res.json()
	print(data)

if __name__ == "__main__":
	main()