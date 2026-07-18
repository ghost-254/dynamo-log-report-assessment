Read the Apache-style access log at /app/access.log and write the traffic summary to /app/report.json.

1. /app/report.json must be a valid JSON object containing exactly these fields: total_requests (integer), unique_ips (integer), and top_path (string).
2. total_requests must count all non-empty log records, unique_ips must count distinct source IP addresses, and top_path must be the HTTP request-target appearing most often. The supplied log has a unique most-frequent request-target.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
