#!/usr/bin/env sh

export PYTHONPATH=.

# Run migrations
alembic revision --autogenerate -m "add table user"

