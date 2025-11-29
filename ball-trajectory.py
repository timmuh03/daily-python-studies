'''

11/29/25
Ball Trajectory
Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

The ball always moves in a straight line.
The movement direction is determined by how the ball moved from 1 to 2.
The edges of the matrix are considered walls. If the balls hits a:
top or bottom wall, it bounces by reversing its vertical direction.
left or right wall, it bounces by reversing its horizontal direction.
corner, it bounces by reversing both directions.

'''


def get_next_location(matrix: list[list[int]]) -> list[int]:

    first = ()
    second = ()

    # find previous (first) and current (second) ball positions
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 1:
                first = (r, c)
            elif matrix[r][c] == 2:                
                second = (r, c)

    # predict next pos w/o collision
    vector = [second[0] - first[0], second[1] - first[1]]
    third = [second[0] + vector[0], second[1] + vector[1]]

    # check collision and reverse velocity if true
    if third[0] < 0 or third[0] >= len(matrix):
        vector[0] *= -1
    if third[1] < 0 or third[1] >= len(matrix[0]):   # fixed column bound
        vector[1] *= -1
   
    # final position after bounce
    third = [second[0] + vector[0], second[1] + vector[1]]

    return third

# --------------------------------------------------
# Test cases (only run when file is executed directly)
# --------------------------------------------------
if __name__ == "__main__":
    print("Pong Ball Trajectory — Test Cases\n")

    test1 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 2, 0],
        [0, 0, 0, 0]
    ]
    print("Right → [2, 3]        :", get_next_location(test1))

    test2 = [
        [0, 0, 0],
        [0, 1, 0],
        [2, 0, 0]
    ]
    print("Diagonal into corner → [1, 1]:", get_next_location(test2))

    test3 = [
        [2, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print("Up-left test → [1, 1]  :", get_next_location(test3))