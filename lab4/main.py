
import numpy as np
a = np.reshape(np.arange(300), (3,10,10))
b = np.ones((3,3,10,10))
def sum_f(q, g, f):
    """
    >>> (a[:,:,-1]+b[:,:,:,-1]).shape
    (3, 3, 10)
    >>> (sum_f(a[:,:,-1],b[:,:,:,-1],0)[:,0]==np.array([10.,10.,10.])).all()
    True
    """
    return np.min(q+f+g, axis=1)

def projector_gK(g, k):
    """
    >>> c = np.arange(1,4)[:,None,None,None]*b
    >>> c.shape
    (3, 3, 10, 10)
    >>> idx = np.array([0,1,0,2,0,0,0,0,0,0])
    >>> (projector_gK(c[:,:,:,-1], idx)[0,:]==np.array([1., 2., 1., 3., 1., 1., 1., 1., 1., 1.])).all()
    True
    """
    return np.take_along_axis(g, k[None, None, :], axis=0)[0]

def projector_XK(X, K):
    """
    >>> testx = np.reshape(np.arange(1500), (5,10,10,3))
    >>> k = np.array([[0,1,0,0,0,0,0,0,0,0]]*10)
    >>> (projector_XK(testx, k)[0,:,0]==np.array([  0, 303,   6,   9,  12,  15,  18,  21,  24,  27])).all()
    True
    """
    return np.take_along_axis(X, K[None, :, :, None], axis=0)[0]
