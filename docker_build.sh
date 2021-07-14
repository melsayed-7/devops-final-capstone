#!/bin/bash
docker build -t melsayed7/capestone:${CIRCLE_WORKFLOW_ID:0:7} .
