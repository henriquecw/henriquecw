import requests

def main():
	base = input("First Currency: ")
	other = input("Second Currency: ")
	access_key = "b483138f2ed2772152115a9dd776efc2"
	#res = requests.get("http://api.fixer.io/latest?base=USD&symbols=EUR")
	res = requests.get("http://data.fixer.io/api/latest", params={"base": base, "symbols": other, "access_key": access_key })

	if res.status_code != 200:
		raise Exception("ERROR: API request unsuccessful.")
	data = res.json()
	rate = data["rates"][other]
	print(f" 1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
	main()