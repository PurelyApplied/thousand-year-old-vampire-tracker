#!/usr/bin/env bash

rm db.sqlite3
rm tracker/migrations/0*py

manage makemigrations
manage migrate

manage createsuperuser