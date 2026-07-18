#!/bin/bash

# pytest is baked into the environment image (environment/Dockerfile).
mkdir -p /logs/verifier
pytest --ctrf /logs/verifier/ctrf.json /tests/test_outputs.py -rA
test_status=$?

if [ "$test_status" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

# Harbor reads pass/fail from reward.txt, so verifier execution itself exits 0.
exit 0
