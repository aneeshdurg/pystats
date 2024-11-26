#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import click

@click.group()
def cli():
    pass

def get_data_from_stream():
    data = []
    while True:
        try:
            l = input()
            data.append(float(l))
        except EOFError:
            break
    return np.array(data)

@cli.command
def histogram():
    plt.stairs(*np.histogram(np.array(get_data_from_stream())))
    plt.show()

@cli.command
def avg():
    print(np.mean(get_data_from_stream()))

@cli.command
def std():
    print(np.std(get_data_from_stream()))

@cli.command
def max():
    print(np.max(get_data_from_stream()))

@cli.command
def min():
    print(np.min(get_data_from_stream()))

@cli.command
def sum():
    print(np.sum(get_data_from_stream()))
