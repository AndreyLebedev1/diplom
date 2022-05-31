import cv2
import os
import numpy as np

def bytescaling(data, cmin=None, cmax=None, high=255, low=0):
    if data.dtype == np.uint8:
        return data
    if high > 255:
        high = 255
    if low < 0:
        low = 0
    if high < low:
        raise ValueError("`high` should be greater than or equal to `low`.")
    if cmin is None:
        cmin = data.min()
    if cmax is None:
        cmax = data.max()
    cscale = cmax - cmin
    if cscale == 0:
        cscale = 1
    scale = float(high - low) / cscale
    bytedata = (data - cmin) * scale + low
    return (bytedata.clip(low, high) + 0.5).astype(np.uint8)


class analisiss():

    def GetAver(self):
        return None

