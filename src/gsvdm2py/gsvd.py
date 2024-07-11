import numpy as np

# Try to import matlab.engine
try:
    import matlab.engine
except:
    raise Exception("Error with matlab.engine, make sure it is installed correctly.")


def gsvd(A, B, mode="full", eng=None):
    """Computes the GSVD of A and B.

    mode: full or econ.
    eng: matlabengine instance, if have already started one. Otherwise starts and closes engine for computation.
    """

    assert mode in ["full", "econ"], "invalid mode!"

    # Start engine?
    if eng is None:
        eng_passed = False
        eng = matlab.engine.start_matlab()
    else:
        eng_passed = True

    # Cast to MATLAB
    _A = matlab.double(A)
    _B = matlab.double(B)

    # Call MATLAB GSVD
    if mode == "full":
        _U, _V, _X, _C, _S = eng.gsvd(_A, _B, nargout=5)
    else:
        _U, _V, _X, _C, _S = eng.gsvd(_A, _B, "econ", nargout=5)

    # Cast as numpy
    U = np.array(_U)
    V = np.array(_V)
    X = np.array(_X)
    C = np.array(_C)
    S = np.array(_S)

    # Close engine if need to
    if eng_passed:
        pass
    else:
        eng.close()


    return U, V, X, C, S
