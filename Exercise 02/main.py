import numpy as np

def diffDrive(x, y, theta, v_l, v_r, t, l):
    coor_init = np.array([x, y, theta]).T

    if v_l != v_r:
        w = (v_r - v_l) / l
        r_c = 2 * (v_l + v_r) / ((v_r - v_l) * l)

        theta_trav = w * t

        icc = np.array([x - r_c*np.sin(theta), y + r_c*np.cos(theta), 0]).T

        transformer = np.array([
            [np.cos(theta_trav), -np.sin(theta_trav), 0],
            [np.sin(theta_trav), np.cos(theta_trav), 0],
            [0, 0, 1]
        ])

        coor_final = np.dot(transformer, (coor_init - icc)) + (icc + np.array([0, 0, theta_trav]).T)

    if v_l == v_r:
        coor_final = coor_init + np.array([v_l * t * np.cos(theta), v_l * t * np.sin(theta), 0]).T

    return (coor_final[0], coor_final[1], coor_final[2])

coor = (1.5, 2, np.pi/2)
moves = [(0.3, 0.3, 3), (0.1, -0.1, 1), (0.2, 0, 2)]
l = 0.5
for move in moves:
    # print(*coor, *move, l)

    coor = diffDrive(*coor, *move, l)
    print(tuple(map(lambda x: round(float(x), 6), coor)))