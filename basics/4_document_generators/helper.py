
def print_search_results(docs):
    matches = docs[0].matches

    print("\nYour search results")
    print("-------------------\n")

    for match in matches:
        print(f"- {match.text}")
