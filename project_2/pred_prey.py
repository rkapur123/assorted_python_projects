__author__ = 'RahulKapur'

def prey_future(pred_now, prey_now, A, B, C,D, n):

    for n in range(0,n): #loop n times
        x = prey_now #store the old prey_now value
        prey_now = prey_next(pred_now, x, A, B) #use x as a parameter
        pred_now = pred_next(pred_now, x, C, D)# x insures you use the correct value
    return prey_now

def pred_future(pred_now, prey_now, A, B,C, D, n):
    for n in range(0,n): #loop n times
        x = prey_now #store prey_now as x
        prey_now = prey_next(pred_now, x, A, B)
        pred_now = pred_next(pred_now, x, C, D)
    return pred_now

def prey_next( pred_now, prey_now, A, B): #calculation for 1 period
    ratePrey = 1 + A
    ratePred = B * pred_now
    return (prey_now * (ratePrey - ratePred)) #return new value of prey

def pred_next(pred_now, prey_now, C, D): #calculation for 1 period
    ratePredDeath = 1 - C
    ratePredFood = D * prey_now
    return (pred_now * (ratePredDeath + ratePredFood)) # new value of pred