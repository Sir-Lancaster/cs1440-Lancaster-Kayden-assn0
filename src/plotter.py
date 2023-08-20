#!/usr/bin/python3

import math


def plot(name, fn, xrange=(-5.0, 5.0), yrange=(-5.0, 5.0), cols=78, lines=14):
    print(name)
    xsize = abs(xrange[1] - xrange[0]) / float(cols)
    ysize = abs(yrange[1] - yrange[0]) / float(lines)
    for line in range(lines + 1):
        print('\x1b[0m|', end='\x1b[1;33m')
        for col in range(cols + 1):
            x = xrange[0] + (col * xsize)
            y = fn(x)
            l = round((yrange[1] - y) / ysize)
            if l == line:
                print('*', end='')
        print('\x1b[0m')
    print('+', '-' * (cols + 1), "\n", sep='')


def square(x):
    return x * x


def cube(x):
    return x * x *x


if __name__ == '__main__':
    options ="abcdefghijq"
    menu = """\
Terminal Function Plotter
-------------------------
a) sin(x)
b) cos(x)
c) tan(x)
d) x^2
e) x^3
f) abs(x)
g) floor(x)
h) sqrt(x)
i) log10(x)
j) exp(x)
q) Quit

> """

    while True:
        o = input(menu).lower().rstrip()
        if o in options:
            if o == 'a':
                plot("y = sin(x)", math.sin, yrange=(-1.5, 1.5))
            elif o == 'b':
                plot("y = cos(x)", math.cos, yrange=(-1.5, 1.5))
            elif o == 'c':
                plot("y = tan(x)", math.tan)
            elif o == 'd':
                plot("y = x^2", square, yrange=(0, 10))
            elif o == 'e':
                plot("y = x^3", cube, yrange=(-4, 4))
            elif o == 'f':
                plot("y = abs(x)", abs, yrange=(-0.5, 5))
            elif o == 'g':
                plot("y = floor(x)", math.floor)
            elif o == 'h':
                plot("y = sqrt(x)", math.sqrt, xrange=(0, 100.0), yrange=(0, 10.0))
            elif o == 'i':
                plot("y = log10(x)", math.log10, xrange=(.000001, 100000), yrange=(-2.0, 5.0))
            elif o == 'j':
                plot("y = exp(x)", math.exp, xrange=(.001, 5.0), yrange=(1.0, 150.0))
            elif o == 'q':
                break
        else:
            print(f"Unrecognized option '{o}'\n")
