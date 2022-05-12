#!/bin/sh

searchdir=./config/dmu/noti

for entry in $searchdir/*

do
    echo $entry
    python main.py --config_path $entry
done
