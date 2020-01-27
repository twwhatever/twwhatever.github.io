Title: Languages for writing Deep Learning models
Date: 2020-01-15 20:30
Category: vanity, j, julia, python

# Languages for writing Deep Learning models

I've been dealing with some PyTorch Deep Learning models at work recently.  PyTorch is a great library, but I find myself tracing through code across multiple files even for relatively standard network architectures.

I once puzzled out the core of a valid convolution in J, and was surprised how short it was.

```
(+/ % #)@:,@:(*&k) ;._3 a
```

`a` is the input matrix and `k` is the convolution matrix.  I wouldn't be particularly surprised to learn there's a much better way of writing it.  What particularly impressed me is that the whole thing (including spaces) is only 25 characters.  The word "convolution" itself is 11 characters, so we're within an order of magnitude of space to define the operation as to name it.

Reading right to left, the expression does something like 
  1. View the `a` matrix as a collection of overlapping matrices with the same dimension as `k`
  2. Multiply the entries of the `k` matrix with the entries of the corresponding submatrix of `a`
  3. Unroll the resulting matrices
  4. Average the unrolled matrices

A rough equivalent to this in Python would be something like

```python
s = tuple(np.subtract(a.shape, k.shape) + 1)
v = tuple(np.subtract(a.shape, s) + 1) + s
t = a.strides + a.strides

m = np.lib.stride_tricks.as_strided(a, v, t)
np.einsum('ij,ijkl->kl', k, m)
```

Some of the difference is just due to the fact that J has very sophisticated operations for matching up dimensions in a useful way: the arcane magic of `;_3` vs. the manual computation necessary to set up the call to `as_strided`.  That could all be stuffed in a function:

```python
def sr(a, k):
    s = tuple(np.subtract(a.shape, k.shape) + 1)
    v = tuple(np.subtract(a.shape, s) + 1) + s
    t = a.strides + a.strides
    return np.lib.stride_tricks.as_strided(a, v, t)

np.einsum('ij,ijkl->kl', k, sr(a, k))
```

The final expression is on the order of the J expression, especially if we reduce np.einsum to a shorter name.


Julia also seems to be gaining some popularity in Machine Learning circles recently.  
