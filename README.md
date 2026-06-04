# Python Arithmetic Operators

A small collection of reusable Python math helper functions.

## Functions

`math_functions.py` includes helpers for:

- Basic arithmetic: `add`, `subtract`, `multiply`, `divide`, `modulo`, `floor_divide`
- Powers and roots: `power`, `square`, `cube`, `square_root`, `cube_root`, `nth_root`
- Number helpers: `absolute`, `reciprocal`, `factorial`, `gcd`, `lcm`, `is_even`, `is_odd`, `is_prime`
- Trigonometry: `degrees_to_radians`, `radians_to_degrees`, `sine`, `cosine`, `tangent`
- Logarithms: `logarithm`, `natural_log`, `log10`
- Aggregates and percentages: `mean`, `median`, `product`, `percentage`, `percentage_change`
- Utility helpers: `clamp`, `round_to`

## Example

```python
import math_functions as mf

print(mf.add(2, 3))
print(mf.square_root(81))
print(mf.percentage_change(100, 125))
```

## Run tests

```bash
python -m unittest
```
