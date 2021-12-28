import matplotlib.pyplot as plt
def crop(img, i, i_, j, j_, shape):
    """
    >>> (crop(x1, 0,0,0,0, (30,30))==x1).all()
    True
    """
    h, w = shape
    return img[i*h:(i_+1)*h, j*w:(j_+1)*w]

def split(flag, N, f, gvh, i, i_, j, j_, n):
    result = []
    for n1 in N:
        for n2 in N:
            if flag == 'v':
                for i__ in range(i, i_):
                    res = all([f[i, i__, j, j_, n1],
                               (n1, n2, n) in gvh,
                               f[i__+1, i_, j, j_, n2]])
                    result.append(res)
            elif flag == 'h':
                for j__ in range(j, j_):
                    res = all([f[i, i_, j, j__, n1],
                               (n1, n2, n) in gvh,
                               f[i, i_, j__+1, j_, n2]])

                    result.append(res)
    return any(result)

def rename(T, f, g, i, i_, j, j_, n):
    result = []
    for t in T:
        result.append(all([f[i, i_, j, j_, t], (t, n) in g]))
    return any(result)

def state(N, f, cols):
    if f[0, 2, 0, cols-1, 'I']:
        for n_ in N:
            if f[0, 2, 0, 0, n_]:
                res = int('_' in n_)
                print("Right expression:", res)
    else:
        print("Incorrect expression")

def check(img, X, rules):
    h, w = X[0].shape
    cols = int(len(img[0]) / w)
    f = dict()
    for i in range(3):
        for j in range(cols):
            for i_ in range(i, 3):
                for j_ in range(j, cols):
                    for t in rules['T']:
                        block = crop(img, i, i_, j, j_, (h, w))
                        if block.shape == (h, w):
                            f[i, i_, j, j_, t] = (block==X[t,:]).all()
                        else:
                            f[i, i_, j, j_, t] = False
                    for n in rules['N']:
                        f[i, i_, j, j_, n] = False

    for S in range(1, 3 * cols + 1):
        for i in range(3):
            for j in range(cols):
                for i_ in range(i, 3):
                    j_ = int(S/(i_+1-i)) + j -1
                    if (S%(i_+1-i))==0 and j_ < cols:
                        for n in rules['N']:
                            ver = False if (i_ == i) else split('v', rules['N'], f, rules['gv'], i, i_, j, j_, n)
                            hor = False if (j_ == j) else split('h', rules['N'], f, rules['gh'], i, i_, j, j_, n)
                            ren = rename(rules['T'], f, rules['g'], i, i_, j, j_, n)
                            f[i, i_, j, j_, n] = any([f[i, i_, j, j_, n], hor, ver, ren])

    state(rules['N'], f, cols)
    return plt.imshow(img)
