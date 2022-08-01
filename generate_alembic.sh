#!/usr/bin/env sh

export PYTHONPATH=.

# Run migrations
alembic revision --autogenerate -m "create table product_category"

