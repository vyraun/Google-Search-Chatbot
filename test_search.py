from google import google

search_results = google.search("message")

for x in search_results:

	print(x.description)
	
print("----------------")

print(search_results[1].description)