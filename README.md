# gsvdm2py
A Python wrapper for MATLAB's gsvd function (generalized singular value decomposition). 

Installation instructions:

1. Make sure MATLAB is installed.

2. ```pip install matlabengine```.

3. ```pip install gsvdm2py```

This was made as a quick work-around to address the lack of a GSVD code in Python that (1) works in call cases of matrix dimensions (2) is easy to install. 

Some links to existing Python GSVD implementations:
- [pygsvd](https://github.com/bnaecker/pygsvd): a Python wrapper for LAPACK's gsvd. Should work in all cases.
- [pygensvd](https://github.com/vanandrew/pygensvd): same as above, but uses cmake for compilation. Should work in all cases.
- [trips-py](https://github.com/mpasha3/trips-py/blob/main/trips/utilities/decompositions.py): a native Python implementation. Requires that left-most dimensions of both input matrices are greater than or equal to their shared rightmost dimension.



# Example usage

```python
import numpy as np
from gsvdm2py import gsvd

# Size of test matrices
m = 200
p  = 195
n = 100

# Draw random test matrices with standard Gaussian entries
A = np.random.normal(size=(m,n))
B = np.random.normal(size=(p,n))

# Compute GSVD. Can specify mode="econ" for economic, or pass a matlab.engine object to eng to use a pre-existing engine.
eng = None
U, V, X, C, S = gsvd(A, B, mode="full", eng=eng) 

# Validate the decomposition? The GSVD outputs are such that:
#     A = U @ C @ X.T.conj()
#     B = V @ S @ X.T.conj()
#     C.T.conj() @ C + S.T.conj() @ S = I 

# These should be near zero
print(np.linalg.norm( A - (U @ C @ X.T.conj() )))
print(np.linalg.norm( B - (V @ S @ X.T.conj() )))
print(np.linalg.norm( (C.T.conj() @ C) +  (S.T.conj() @ S) - np.eye(C.shape[1])) )

```


