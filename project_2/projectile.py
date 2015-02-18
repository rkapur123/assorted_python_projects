__author__ = 'RahulKapur'
import decimal

def g(h): #calculate gravity based on altitude
    G = 6.6742 * (10**-11)
    mass_Earth = 5.9736 * (10**24)
    radius_Earth = 6371000
    return (G * mass_Earth) / ((radius_Earth + h)**2)

def s_next (s_current, v_current, delta_t): # return new displacement
    return s_current + (v_current * delta_t)

def v_next(s_current, v_current, delta_t):# return new velocity
    height = g(s_current) #find new gravity at altitude
    return (v_current - (height * delta_t))

def s_sim(t, v_init, s_init, delta_t): #simulated s with varying gravity
    total_time = 0
    s_current1 = s_init # store initial values
    v_current1 = v_init
    while (total_time < t):#while based on time
        s_current = s_next(s_current1, v_current1, delta_t)
        v_current = v_next(s_current1, v_current1, delta_t)
        v_current1 = v_current # new velocity for next iteration of loop
        s_current1 = s_current # new displacement
        total_time = total_time + delta_t #increment time

    return s_current1

def s_standard(t,v_init): #standard formula
    g = 9.81
    time_squared = t**2
    return ((-0.5 * g * time_squared) + (v_init * t))

def s_extra(t , v_init, s_init, delta_t):
    s_current1 = s_init
    v_current1 = v_init
    total_time = 0.0
    list = []
    while s_current1 >= 0: #while loop to find when the projectile returns
        while (total_time < t):
            s_current = s_next(s_current1, v_current1, delta_t)
            v_current = v_next(s_current1, v_current1, delta_t)
            v_current1 = v_current
            s_current1 = s_current
            total_time = total_time + delta_t
        t = t + 1
        list.append(s_current1) # append the s value to the outer while loop

    return list
