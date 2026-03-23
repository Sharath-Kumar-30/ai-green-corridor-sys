#!/usr/bin/env bash

# Use this script to wait for a service to be available.
# Example usage: ./wait-for-it.sh <host>:<port> -- <command>

set -e

TIMEOUT=15
WAITFORIT_CMD="nc -z"

if [ "$1" == "--help" ]; then
  echo "Usage: $0 <host>:<port> [--timeout=<timeout>] [--] <command>"
  exit 0
fi

while [[ $# -gt 0 ]]; do
  case "$1" in
    --timeout=*)
      TIMEOUT="${1#*=}"
      shift
      ;;
    --)
      shift
      break
      ;;
    *)
      HOST_PORT="$1"
      shift
      ;;
  esac
done

HOST="${HOST_PORT%:*}"
PORT="${HOST_PORT#*:}"

echo "Waiting for $HOST:$PORT..."

for i in $(seq $TIMEOUT); do
  if $WAITFORIT_CMD "$HOST" "$PORT"; then
    echo "$HOST:$PORT is available!"
    break
  fi
  echo "Waiting for $HOST:$PORT... ($i/$TIMEOUT)"
  sleep 1
done

if ! $WAITFORIT_CMD "$HOST" "$PORT"; then
  echo "Timeout waiting for $HOST:$PORT"
  exit 1
fi

if [ "$#" -gt 0 ]; then
  exec "$@"
fi