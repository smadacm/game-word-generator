#!/usr/bin/env sh

rm gamegen.db3
rm -rf */__pycache__

./manage.py migrate

echo
echo

python data/import.py