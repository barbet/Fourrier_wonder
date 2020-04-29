# Fourrier wonder

This repository originally aims at reproducing visualisation from [3Blue1Brown channel](https://www.youtube.com/watch?v=-qgreAUpPwM)

Everything is written in python. Because the notebook contains animation, it cannot be rendered within github. You can play with it on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/barbet/Fourrier_wonder/master).


## 1. Animating a fourrier series

The first part of the notebook creates a `FourrierCurve` object. This is mostly a dictionnary frequency: complex coefficient. 
It computes the trajectory of this serie within the complex plan.
This enables us to draw or animate the drawing.

## 2. Reverse

This part aims at finding fourrier coefficient for an arbitrary (looped) curve. The object `polygon` takes a list of coordinates and can export a `FourrierCurve`.

## 3. Custom drawing

This part is a cell utility, that enables the user to draw an arbitrary line. 
To start drawing you need to click, then draw with your mouse, and click again to stop.
You can then find the `FourrierCurve` fitting your drawing.
Some drawings of my own are available in "/drawings/" for illustration purpose

## Miscellaneous

export env with `conda env export --no-builds -f environment.yml`

