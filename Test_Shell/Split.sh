#!/bin/bash

TEST_STRING="wlp3
wlp4",

gawk 'BEGIN{FS='\n'} {arrayIdList=($1,$2)'} TEST_STRING
