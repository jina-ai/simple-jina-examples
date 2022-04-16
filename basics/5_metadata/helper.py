'''
def print_search_results(docs):
    matches = docs[0].matches

    print("\nYour search results")
    print("===================\n")

    for match in matches:
        # Access tags and print "Title" value for the Document
        #print(match.tags["Title"])
        print("-----------")
        print(f"= {match.text}\n")
'''
def print_search_results(docs):
    matches = docs[0].matches

    print("\nYour search results")
    print("-------------------\n")

    for match in matches:
        print(f"- {match.text}")
