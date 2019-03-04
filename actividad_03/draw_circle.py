import math
import draw_common as com

def dda_circle(xi, yi, xf, yf):

    # draw in blue center
    com.drawPoint([[xi, yi]], 2)

    # draw in red point on the circle
    com.drawPoint([[xf, yf]], 2)

    r2 = math.pow(( xf - xi ), 2) + math.pow(( yf - yi ), 2)
    r = math.sqrt(r2)

    # draw in red point on the circle
    com.drawPoint([[xi, yi + r ]], 0)
    com.drawPoint([[xi, yi - r ]], 0)
    com.drawPoint([[xi + r, xi + r ]], 0)
    com.drawPoint([[xi - r, xi + r ]], 0)

    print("radius is ", r)
    print("radius^2 is ", r2)

    #for x in range(int(xi - r), int(xi + r),1):

        # draw in red point on the circle
        #common.drawPoint([[x, yf]], 0)

