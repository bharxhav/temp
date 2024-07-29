import numpy as np


def calculate_distance(ij, img):
    img_8bit = ij.op().convert().uint8(img)
    imp = ij.py.to_imageplus(img_8bit)

    ij.IJ.setAutoThreshold(imp, "Default dark")
    ij.IJ.run(imp, "Convert to Mask", "")

    binary_np = ij.py.from_java(imp.getProcessor().getPixels())
    binary_np = binary_np.reshape(imp.getHeight(), imp.getWidth())

    y_coords, x_coords = np.nonzero(binary_np)

    if len(x_coords) > 1:
        distances = np.sqrt(np.diff(x_coords)**2 + np.diff(y_coords)**2)
        return np.sum(distances)

    return -1
