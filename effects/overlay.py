import cv2
import numpy as np


def overlay_png(background, overlay, x, y):
    """
    Draw an RGBA PNG onto a BGR image.

    background : camera image
    overlay    : PNG with alpha
    x,y        : center position
    """

    if overlay is None:
        return background

    h, w = overlay.shape[:2]

    # Position from center
    x = int(x - w / 2)
    y = int(y - h / 2)

    # Completely outside
    if x >= background.shape[1] or y >= background.shape[0]:
        return background

    if x + w <= 0 or y + h <= 0:
        return background

    # Clip to screen
    x1 = max(x, 0)
    y1 = max(y, 0)

    x2 = min(x + w, background.shape[1])
    y2 = min(y + h, background.shape[0])

    overlay_x1 = x1 - x
    overlay_y1 = y1 - y

    overlay_x2 = overlay_x1 + (x2 - x1)
    overlay_y2 = overlay_y1 + (y2 - y1)

    roi = background[y1:y2, x1:x2]

    overlay_crop = overlay[
        overlay_y1:overlay_y2,
        overlay_x1:overlay_x2
    ]

    rgb = overlay_crop[:, :, :3]

    alpha = overlay_crop[:, :, 3] / 255.0

    alpha = alpha[:, :, np.newaxis]

    result = roi * (1 - alpha) + rgb * alpha

    background[y1:y2, x1:x2] = result.astype(np.uint8)

    return background