# Monitor GitHub API rate limits

## Capturing the rate limits of a GitHub account

```shell
$ python monitor_rate_limits.py --token <gh_token> -o my_capture
```

- Token (classic) must have "user" scope to query the `/rate_limit` endpoint
- Polling occurs every second

## Ploting usage

```shell
$ python plot_graph.py -i my_capture
```

For comparing multiple capture on the same graph:

```shell
$ python plot_graph.py -i my_first_capture -i my_second_capture -i my_third_capture
```

## GitHub API rate limits

https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28
