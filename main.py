#!/usr/bin/env python3
"""
Simple Utils — small Python tool by Igor
"""

import datetime, random

def quote_of_the_day():
    quotes = [
        "Keep pushing forward.",
        "Every line of code counts.",
        "Discipline beats motivation.",
        "Ship > perfect."
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print(f"🕓 {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
    print("💬", quote_of_the_day())
