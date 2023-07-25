import tensorly as tl
import numpy as np
from tensorly.decomposition import tucker
from matplotlib import pyplot as plt
from tensorly.base import unfold
from tensorly.tenalg import multi_mode_dot, mode_dot
from tensorly.tucker_tensor import tucker_to_tensor, TuckerTensor, validate_tucker_rank, tucker_normalize
from tensorly.decomposition import non_negative_parafac, non_negative_tucker

def non_negative_tucker_core(tensor, rank,mcore,mfactors,ntensor, n_iter_max=1000, init='svd', tol=10e-6,
                        random_state=None, verbose=False, return_errors=False,
                        normalize_factors=False):
    """Non-negative Tucker decomposition

        Iterative multiplicative update, see [2]_

    Parameters
    ----------
    tensor : ``ndarray``
    rank : None, int or int list
        size of the core tensor, ``(len(ranks) == tensor.ndim)``
        if int, the same rank is used for all modes
    n_iter_max : int
        maximum number of iteration
    init : {'svd', 'random'}
    random_state : {None, int, np.random.RandomState}
    verbose : int , optional
        level of verbosity
    ranks : None or int list
    size of the core tensor
    normalize_factors : if True, aggregates the core which will contain the norms of the factors.

    Returns
    -------
    core : ndarray
            positive core of the Tucker decomposition
            has shape `ranks`
    factors : ndarray list
            list of factors of the CP decomposition
            element `i` is of shape ``(tensor.shape[i], rank)``

    References
    ----------
    .. [2] Yong-Deok Kim and Seungjin Choi,
       "Non-negative tucker decomposition",
       IEEE Conference on Computer Vision and Pattern Recognition s(CVPR),
       pp 1-8, 2007
    """
    rank = validate_tucker_rank(tl.shape(tensor), rank=rank)

    epsilon = 10e-12

    # Initialisation
    if init == 'svd':
        core, factors = tucker(tensor, rank)
        #core1,factors=tucker(ntensor,rank)
        nn_factors = [tl.abs(f) for f in factors]
        nn_core = tl.abs(core)
    else:
        rng = tl.check_random_state(random_state)
        core = tl.tensor(rng.random_sample(rank) + 0.01, **tl.context(tensor))  # Check this
        factors = [tl.tensor(rng.random_sample(s), **tl.context(tensor)) for s in zip(tl.shape(tensor), rank)]
        nn_factors = [tl.abs(f) for f in factors]
        nn_core = tl.abs(core)

    norm_tensor = tl.norm(tensor, 2)
    rec_errors = []
    nn_core=tl.abs(mcore)#
    #nn_factors[2]=mfactors[2] #
    for iteration in range(n_iter_max):
        for mode in range(tl.ndim(tensor)):
            B = tucker_to_tensor((nn_core, nn_factors), skip_factor=mode)
            B = tl.transpose(unfold(B, mode))

            numerator = tl.dot(unfold(tensor, mode), B)
            numerator = tl.clip(numerator, a_min=epsilon, a_max=None)
            denominator = tl.dot(nn_factors[mode], tl.dot(tl.transpose(B), B))
            denominator = tl.clip(denominator, a_min=epsilon, a_max=None)
            nn_factors[mode] *= numerator / denominator

        numerator = tucker_to_tensor((tensor, nn_factors), transpose_factors=True)
        numerator = tl.clip(numerator, a_min=epsilon, a_max=None)
        for i, f in enumerate(nn_factors):
            if i:
                denominator = mode_dot(denominator, tl.dot(tl.transpose(f), f), i)
            else:
                denominator = mode_dot(nn_core, tl.dot(tl.transpose(f), f), i)
        denominator = tl.clip(denominator, a_min=epsilon, a_max=None)
        #nn_core *= numerator / denominator#

        rec_error = tl.norm(tensor - tucker_to_tensor((nn_core, nn_factors)), 2) / norm_tensor
        rec_errors.append(rec_error)
        if iteration > 1 and verbose:
            print('reconstruction error={}, variation={}.'.format(
                rec_errors[-1], rec_errors[-2] - rec_errors[-1]))

        if iteration > 100 and abs(rec_errors[-2] - rec_errors[-1]) < tol:
            if verbose:
                print('converged in {} iterations.'.format(iteration))
            break
        if normalize_factors:
            nn_core, nn_factors = tucker_normalize((nn_core, nn_factors))
    tensor = TuckerTensor((nn_core, nn_factors))
    if return_errors:
        return tensor, rec_errors
    else:
        print("rec_errors")
        print(rec_errors)
        return tensor
