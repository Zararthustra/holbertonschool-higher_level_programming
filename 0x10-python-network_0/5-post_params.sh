#!/bin/bash
#sends a POST request
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1" 
