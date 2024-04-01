#!/bin/bash
curl -sI $1 | grep "content-Length" | cut -d " " -f2
