#! /usr/bin/env python3

import click
import hashlib
import pefile

@click.command()
@click.argument('filepath', type=click.Path(exists=True, readable=True, file_okay=True))
def calculate_rich_header_md5(filepath):
    """Calculate a PE Rich Header MD5 hash"""
    binary = pefile.PE(filepath)
    rich_header_clear = binary.RICH_HEADER.clear_data
    rich_hasher = hashlib.md5(rich_header_clear)
    print(rich_hasher.hexdigest())

calculate_rich_header_md5()