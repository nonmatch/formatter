#!/bin/bash
venv/bin/gunicorn -b :10245 app:app  --timeout 500
