import numpy as np
from scipy import stats


def calculate_slope(ij, img):
    img_8bit = ij.op().convert().uint8(img)
    imp = ij.py.to_imageplus(img_8bit)

    ij.IJ.setAutoThreshold(imp, "Default dark")
    ij.IJ.run(imp, "Convert to Mask", "")

    binary_np = ij.py.from_java(imp.getProcessor().getPixels())
    binary_np = binary_np.reshape(imp.getHeight(), imp.getWidth())

    y_coords, x_coords = np.nonzero(binary_np)

    if len(x_coords) > 1:
        slope, intercept, r_value, p_value, std_err = stats.linregress(
            x_coords, y_coords)
        angle = np.arctan(slope) * 180 / np.pi
        return slope, angle

    return None, None
