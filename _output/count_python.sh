#!/bin/bash
# This script counts the number of lines containing the word "python" in all CSV files.

grep -i "python" *.csv | wc -l

