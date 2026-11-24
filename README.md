# Charm the Commuter: Forecast a City That Isn't

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/itzalisha99/commuter-forecast-city/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/itzalisha99/commuter-forecast-city/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

A make.fun entry for **Charm the Commuter: Forecast a City That Isn't**: one line of weather forecast, at most 140 characters, for a city that does not exist — judged by a bored commuter at a rainy bus stop.

## The forecast

> In Upsidownia, rain falls upwards from 3pm — commuters are advised to hold their umbrellas underneath them.

Why this line: it reads as a real broadcast forecast (place, time, advisory language), the impossible weather *is* the joke rather than the setup for one, and the umbrella-underneath detail gives the invented city one concrete image a commuter smiles at on one reading.

## How it works

`main.py` (Python stdlib only, deterministic) writes the forecast to `/output/entry.txt`. It validates the text against the bounty gate first: 1–140 characters, UTF-8, a single line, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
