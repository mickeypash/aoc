#!/usr/bin/env bash

day="$1"

curl "https://adventofcode.com/2022/day/$day/input" \
  -H "Cookie: session=53616c7465645f5fc031190f2a6fe593e29b86be507397faf4bbcfc7f627713990f97e5d4b2a93024e5be591accf1ad59e44dd178c046cc662c856ddd0a8ee62" \
  -H "Referer: https://adventofcode.com/2022/day/$day" \
  -H "Upgrade-Insecure-Requests: 1" \
  --compressed --output input$day.txt
