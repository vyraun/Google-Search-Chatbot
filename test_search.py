from google import google

search_results = google.search("message")

for x in search_results:

	print(x.description)
	
print("----------------")

print(search_results[1].description)


## Will add some more stuff later. 
# pip install pyjokes
# import pyjokes 
# print(pyjokes.get_joke())
