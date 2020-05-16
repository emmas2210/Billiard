Square Billiard
===================
Billiard's animation with words:
^^^^^^^^^^^^^^^^^^^^^
This package allow us to words associated to trajectories:
We start with an empty word. Then, when the ball hit the top or bottom part we add an H (H for horizontal) and when the ball hit the left or right part, we add a V (V for vertical). 
Then, we perform a statistical analysis of the words creating depending on the angle use to start the trajectory (we restrict to words of size <2000).

Canvas Widget:
^^^^^^^^^^^^^^^^^^^^^
This package allows to run an animation representing the ball's trajectory in a square billiard. 
    In this animation you can :
    - change the ball's speed and its trajectory by clicking on the computer mouse wheel
    - enlarge the ball by clicking on the left button of the computer mouse
    - shrink the ball by clicking on the right button of the computer mouse
    - leave the animation clicking on the "esc" button

Classes and functions
^^^^^^^^^^^^^^^^^^^^^^^^^^
Canvas Widget:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: Billiard.square.class_square_billiard
    :members:

Billiard's animation with words:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: Billiard.square.square_billiard_code
    :members: