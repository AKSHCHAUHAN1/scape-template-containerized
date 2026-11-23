# SCAPE Containerized API template

A runtime-neutral Docker API starter for SCAPE. This sample uses Python's standard library so you can replace it with any runtime supported by a Dockerfile.

## Contract

- The container listens on `0.0.0.0` using `PORT` (defaults to `3000`).
- `GET /health` returns HTTP 200 and `{ "status": "ok" }`.
- The root `Dockerfile` must build without private credentials.

## Run locally

```sh
python3 app.py
curl http://localhost:3000/health
docker build -t scape-containerized-api .
docker run --rm -p 3000:3000 scape-containerized-api
```

Replace the sample app or its runtime as needed, keeping the port and health endpoint contract.
