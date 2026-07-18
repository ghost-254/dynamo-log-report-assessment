# Dynamo Log Report Assessment

This repository contains the repaired Terminal-Bench 2 (Harbor) task from the Project Dynamo assessment.

The task asks an agent to parse `/app/access.log` and write a JSON traffic summary to `/app/report.json`. The repair corrects the Harbor manifest, pins the approved base image by digest, removes a leaked reference implementation, aligns the instruction and verifier one-to-one, and writes both reward and CTRF output to `/logs/verifier/`.

## Validation

Run from the directory containing `log-report/`:

```bash
harbor run -p log-report -a oracle
harbor run -p log-report --agent nop
```

Verified results:

- Oracle: reward `1.0`, two tests passed, no exceptions.
- Nop: reward `0.0`, two tests failed, no exceptions.
- An intentionally wrong oracle using `total_requests = 5` received reward `0.0`; the value test reported `assert 5 == 6`.
