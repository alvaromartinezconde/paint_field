#%%

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle

def pintar_campo(color_campo):
    ax = plt.axes()
    bottom, width, lenght= 0., 100, 100
    
    pitch_width, pitch_length=68., 105
    
    goal_width, goal_length, goal_bottom, goal_top =10.76, 1.9, 44.62, 55.38
    
    six_yard_width, six_yard_length, six_yard_left =26.4, 5.8, 5.8

    six_yard_right, six_yard_bottom, six_yard_top=94.2, 36.8, 63.2

    penalty_left, penalty_right=11.5, 88.5
    penalty_area_width, penalty_area_length, penalty_area_left=57.8 ,17.0, 17.

    penalty_area_right, penalty_area_bottom, penalty_area_top=83., 21.1, 78.9

    center_width, center_length, circle_diameter=50., 50, 17.68

    coord_x = [center_length, center_length, width, width,
                  penalty_area_right, penalty_area_right, width,
                  width, six_yard_right, six_yard_right, width,
                  width, bottom, bottom, penalty_area_left,
                  penalty_area_left, bottom, bottom, six_yard_left,
                  six_yard_left, bottom, bottom, center_length, ]
    coord_y = [bottom, lenght, lenght, penalty_area_bottom,
                  penalty_area_bottom, penalty_area_top, penalty_area_top,
                  six_yard_bottom, six_yard_bottom, six_yard_top,
                  six_yard_top, bottom, bottom, penalty_area_top,
                  penalty_area_top, penalty_area_bottom, penalty_area_bottom,
                  six_yard_top, six_yard_top, six_yard_bottom,
                  six_yard_bottom, lenght, lenght, ]

    plt.plot(coord_x, coord_y, color_campo)
    circulo_central = plt.Circle((50,50), radius=10, fill=False, color=color_campo)
    ax.add_patch(circulo_central)

    circulo_central = plt.Circle((50, 50), radius=.5, fill=True, color=color_campo)
    ax.add_patch(circulo_central)

    punto_penalti1 = plt.Circle((11, 50), radius=.5, fill=True, color=color_campo)
    ax.add_patch(punto_penalti1)

    punto_penalti2 = plt.Circle((89, 50), radius=.5, fill=True, color=color_campo)
    ax.add_patch(punto_penalti2)

    arq_izq = Arc((11,50),20, 20,theta1=310,theta2=50,color=color_campo)
    arq_dcho = Arc((89,50),20,20,theta1=130,theta2=230,color=color_campo)
    ax.add_patch(arq_izq)
    ax.add_patch(arq_dcho)

    plt.plot(coord_x, coord_y, color_campo) 
    plt.show() 
    return ax

# %% 



ax = pintar_campo("blue")
