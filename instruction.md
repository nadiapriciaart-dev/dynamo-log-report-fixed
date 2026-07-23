Analyze the Apache-style access log at `/app/access.log` and write a JSON
summary to `/app/report.json`.

The output must be a JSON object containing exactly these keys:

- `total_requests`: the number of non-empty lines in `/app/access.log`
- `unique_ips`: the number of distinct client IP addresses, where the client
  IP is the first whitespace-delimited field of each non-empty log line
- `top_path`: the request path occurring most frequently in the quoted HTTP
  request on each log line

1. `/app/report.json` exists, is valid JSON, and contains exactly the keys
   `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` is `6`.
3. `unique_ips` is `3`.
4. `top_path` is `"/index.html"`.
