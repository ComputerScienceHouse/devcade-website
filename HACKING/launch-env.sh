#!/bin/bash

set -e

podman run --rm -it --env-file .env -p 8080:8080 devcade-website-dev
