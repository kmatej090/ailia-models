import numpy as np
import cv2

__all__ = [
    'batched_nms',
]


def _box_nms(dets, scores, threshold):
    x1, y1, x2, y2 = np.split(dets, 4, axis=1)
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    order = np.argsort(scores)[::-1]

    n = dets.shape[0]
    suppressed = np.zeros(n)

    for _i in range(n):
        i = order[_i]
        if suppressed[i] == 1:
            continue

        ix1 = x1[i]
        iy1 = y1[i]
        ix2 = x2[i]
        iy2 = y2[i]
        iarea = areas[i]

        for _j in range(_i + 1, n):
            j = order[_j]
            if suppressed[j] == 1:
                continue

            xx1 = max(ix1, x1[j])
            yy1 = max(iy1, y1[j])
            xx2 = min(ix2, x2[j])
            yy2 = min(iy2, y2[j])

            w = max(0, xx2 - xx1 + 1)
            h = max(0, yy2 - yy1 + 1)

            inter = w * h
            ovr = inter / (iarea + areas[j] - inter)
            if ovr[0] >= threshold:
                suppressed[j] = 1

    return np.nonzero(suppressed == 0)[0]


def batched_nms(boxes, scores, idxs, threshold, max_num=0):
    total_mask = np.zeros(scores.size, dtype=np.bool)

    for id in np.unique(idxs):
        mask = (idxs == id).nonzero()[0]
        keep = _box_nms(boxes[mask], scores[mask], threshold)
        total_mask[mask[keep]] = True
    keep = total_mask.nonzero()[0]

    ind = scores[keep].argsort()[::-1]
    keep = keep[ind]

    if max_num > 0:
        keep = keep[:max_num]

    return keep
