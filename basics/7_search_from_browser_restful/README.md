# 6. Search from your web browser

In this unit, we:

- Write a new function to use RESTful API, so a web-based front-end can talk to our search engine

Note: Writing the actual front-end is outside the scope of this tutorial. However, we provide a simple `curl` command that accesses the RESTful endpoint.

## Usage

1. Run the `app.py` usign the command `python app.py search_restful` and keep it running in your terminal
2. Open another terminal window
3. Run `curl --request POST 'http://localhost:12345/post' --header 'Content-Type: application/json' -d '{"data": [{"text": "hello world"}],"execEndpoint": "/search"}'`. (`hello world` can be replaced with other search terms.)
4. You'll see the raw JSON output

## Tip

For better formatted output, install [`jq`](https://stedolan.github.io/jq/) and append ` | jq -C | less` to the `curl` command for syntax highlighting and pager.
