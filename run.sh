#!/bin/bash
gunicorn -b :10245 app:app  --timeout 500
