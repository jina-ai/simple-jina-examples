from docarray import Document, DocumentArray


def print_search_results(response):
    matches = response[0].data.docs[0].matches

    print("\nYour search results")
    print("-------------------\n")

    for match in matches:
        print(f"- {match.text}")
