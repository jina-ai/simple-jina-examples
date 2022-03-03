from jina import Document, DocumentArray


def print_search_results(response, number=5):
    matches = docs[0].matches

    print("\nYour search results")
    print("===================\n")

    for match in matches[0:number]:
        print(match.tags["Title"])
        print("-----------")
        print(f"= {match.text}\n")
