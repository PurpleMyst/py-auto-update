#!/usr/bin/env python3
import autoupdater

value = 1234


def main():
    autoupdater.initialize()
    print("Value:", value)


if __name__ == "__main__":
    main()
