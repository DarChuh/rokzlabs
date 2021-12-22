
import numpy as np
def tests():
    """
    >>> a = np.reshape(np.arange(300), (3,10,10))
    >>> b = np.ones((3,3,10,10))
    >>> (a[:,:,-1]+b[:,:,:,-1]).shape
    (3, 3, 10)
    >>> c = np.arange(1,4)[:,None,None]*b[:,:,:,-1]
    >>> idx = np.array([0,1,0,2,0,0,0,0,0,0])
    >>> np.take_along_axis(c, idx[None,None,:], axis=0)[0][0].astype(int)
    array([1, 2, 1, 3, 1, 1, 1, 1, 1, 1])
    >>> np.min(a[:,:,-1]+b[:,:,:,-1], axis=1)[:, 0]
    array([10., 10., 10.])
    >>> (np.min(a[:,:,-1]+b[:,:,:,-1], axis=0)[:, 0].astype(int) == np.array([10, 110, 210])).all()
    True
    """
