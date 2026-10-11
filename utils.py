import numpy as np

def calculate_biomechanical_angle(a, b, c):
    """Calculates joint angles like knee flexion or spine angle using MediaPipe keypoints."""
    a = np.array(a) # First point (e.g., Hip/Shoulder)
    b = np.array(b) # Mid point (e.g., Knee/Mid-spine)
    c = np.array(c) # End point (e.g., Ankle/Head)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return round(angle, 2)