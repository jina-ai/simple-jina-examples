# 🚧 This repository is depricated! 🚧

# Jina Simple Examples

## What are these examples for?

These examples are intended to give you hands-on experience with the basic concepts you need to get up and running with [Jina](https://github.com/jina-ai/jina/). 

Each step adds another small feature on top of the previous step, so be sure to go through each step in order.

## What are they not for?

- They're not meant to be comprehensive
- They aren't for production ready applications

## What do I need to get started?

- Have basic to intermediate Python skill
- Read [Jina fundamentals](https://docs.jina.ai/) on our docs
- Install Jina on [Mac, Linux](https://docs.jina.ai/get-started/install/), or [Windows](https://docs.jina.ai/advanced/experimental/windows/)

## Let's go!

1. Ensure you're in a virtual environment
2. `pip install -r requirements.txt`
3. `cd basics/1_minimum_example`
4. `python app.py`

Then take a look at the code. The apps in themselves do very little, but slowly build up to a more complex app. After you've finished the first section, move onto section 2 and so on.

## Troubleshooting

**First** run:

- `git pull` to ensure you're using the latest code for these examples
- `pip install -U jina` to ensure you're using the latest release of Jina

### `Flow is aborted due to ['xxx'] can not be started`

This may be a timeout error. Add `timeout_ready=240000` to the Executor in your Flow:

```python
flow = Flow().add(uses="foo", timeout_ready=240000)
```
### Any error 
This may be due to using older versions of Hub Executors. Please delete your cache using `rm -rf ~/.jina` and then try running again.

Also, [stop any Jina Docker containers](https://linuxhint.com/stop_docker_containers/) that are currently running.

### I'm still having trouble!

- Join our [Slack](https://slack.jina.ai) and ask there.
