def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """
    if angle > 180:
        while angle > 180:
            angle -= 360
        return angle
    elif angle <  - 180:
        while angle < -180:
            angle += 360
        return angle
    else:
        return angle


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """

    # Bound all angles
    first_angle = bound_to_180(first_angle)
    middle_angle = bound_to_180(middle_angle)
    second_angle = bound_to_180(second_angle)

    # Ideal Scenario: first and second angles are either in the top or bottom half

    # First case: first and middle angle in first two quadrants 
    if first_angle >= 0 and second_angle >= 0:
        if first_angle < second_angle:
            return first_angle < middle_angle < second_angle
        else:
            return second_angle < middle_angle < first_angle 

    # Second Case: first and middle angle in last two quadrants
    elif first_angle < 0 and second_angle < 0:
        if first_angle < second_angle:
            return first_angle < middle_angle < second_angle
        else:
            return second_angle < middle_angle < first_angle

    # Unideal Scenario: First angle and second angle are split between top and bottom half
    # Would have to check for reflex angle

    # First case: first angle is in top half while second angle is on the bottom half
    if first_angle > second_angle:
        angle_between = first_angle - second_angle

        if angle_between < 180:
            return second_angle < middle_angle < first_angle
        else:
            return first_angle < middle_angle < (second_angle + 360)
    
    # Second case: first angle is in bottom half while second angle is on top  
    if second_angle > first_angle:
        angle_between = second_angle - first_angle
        if angle_between < 180:
            return first_angle < middle_angle < second_angle
        else:
            return second_angle < middle_angle + 360 < (first_angle + 360)


