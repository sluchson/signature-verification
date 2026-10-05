import numpy as np


def eer(pos_scores, neg_scores):
    thresholds = np.sort(np.concatenate([pos_scores, neg_scores]))
    best_diff, best_eer, best_t = None, None, None
    for t in thresholds:
        frr = np.mean(pos_scores < t)
        far = np.mean(neg_scores >= t)
        if best_diff is None or abs(far - frr) < best_diff:
            best_diff, best_eer, best_t = abs(far - frr), (far + frr) / 2, t
    return best_eer, best_t


def far_frr(pos_scores, neg_scores, threshold):
    frr = np.mean(pos_scores < threshold)
    far = np.mean(neg_scores >= threshold)
    return far, frr