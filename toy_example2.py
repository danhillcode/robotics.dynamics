#calculations:
        #f = ma   
        #????how do you account for fx and fy
        #a = f/m   a = x / 1

        #acceleration(a) = v / t 
        #time = acceleration * velocity
        #t = time??

        #q_dot = Aq + Bu    #velocity
        #q = position

import numpy as np

def non_linear_term(q, dq):
    a0 = 1e-5
    a1 = 1e-4

    return a0*(q**2) +  a1*(dq**2)

#params
#q is 1x4 matrix taking the input
#q = [x, y, x_dot, y_dot]

#u is input parameters
#force comes from u which is Fx Fy
#u = [Fx, Fy]

def Dynamics(q, u, dt=0.01, disturb=False):
        #test input params q = [x, y, x_dot, y_dot]
        mass    = 1.
        gravity = -9.81
        length  =  1.
        
        t = 0   #time
        dt = 0  #change in time ?
        m = 1   #mass   #mass given 1(arbitrary value)

        #     ddq = (1./mass)*(u-gravity)

#     dq += ddq*dt
#     q  += dq*dt

        #q = [x, y, x_dot, y_dot] is multiplied by the A matrix below this gives the next timestep of each

        #Matrix of weights agaisnt input q
        A = [[1,0,t,0],
            [0,1,0,t],
            [0,0,1,0],
            [0,0,0,1]]
                                    
        A = np.matrix(A)
        q = np.matrix(q) 


        Aq = A * q
        #print(A)
        #print(q)
        #print(Aq)


        #check that this is multiplicative in a matrix   
        B = [[0,0],
             [0,0],
             [dt/m,0],
             [0,dt/m]]

        B = np.matrix(B)
        u = np.matrix(u) 

        Bu = B * u
        #print(Bu)

        q_dot = Aq + Bu
        #print(q_dot)
       
        #return velocity
        #print Aq
        print q
        print q_dot

        if disturb:
            q += non_linear_term(q, q_dot)

        return q, q_dot 
     


# def dynamics(q, dq, u, dt=0.01, disturb=False):
#     mass    = 1.
#     gravity = -9.81
#     length  =  1.

# #where does U come from?
# # u is random number
#     ddq = (1./mass)*(u-gravity)

#     dq += ddq*dt
#     q  += dq*dt

#     if disturb:
#         q += non_linear_term(q, dq)
    
#     #taken off 
#     #print(q,dq)

#     return q, dq

        #compute control is the control that the robot performs 
#this will be one control command and to do many it will 
#reuire the robot does multiple to create a trajectory


#qf refers to the final q #position
#dqf refers to the final dq. #velocity
def compute_ctrl(q0, dq0, qf, dqf, correction_dynamics=None):
    '''
    find a control command using the start, final and the dynamics
    at present it is not doing anything, just returning a random control input
    so initially the correction dyanmics is none and later it learns it
    '''
    #Acceleration = force * mass 
    #got position and velocity
    #velocity =  
    #force = 
    
    if correction_dynamics is not None:
        '''
        add the corrected dyanmics to the computed dyanmics
        '''
        #at the moment this is set as random although this 
        #code needs altering
    return np.random.rand()




#this is the second thing that needs altering 
#this is learning the correction after collecting data and saving data 
#see notes for explanation



# def collect_data_and_learn_correction(total_data_points=100):
    
#     for k in range(total_data_points):

#         #u is a recursive call 
#         u = compute_ctrl(q, dq, qf, dqf, dynamics)

#         q_nxt, dq_nxt = dynamics(q=q, dq=dq, u=u, disturb=True)

#         data.append(np.array([q, dq, u, q_nxt, dq_nxt]))

#         q = q_nxt
#         dq = dq_nxt

#     np.savetxt('data.txt', data)

#     '''
#     implement some method that will use this data to learn the correction model
#     for example, 
#     '''

#     return correction_dynamics



def main():
    #q = [x, y, x_dot, y_dot] this is the start
    q = [[0], [0], [0], [0]]
    goal  =  np.pi

    total_data_points = 100

    data = []

    
    dq = 0.

    for k in range(total_data_points):


        u = [[1],[1]]
        #u = [[np.random.rand()],[np.random.rand()]]
        
        next_q,next_dq =  Dynamics(q,u)
        print("this is q", q)
        print("this is dq", dq)


        compute_ctrl(q, dq, next_q, next_dq, correction_dynamics=None)
        



        #data.append(np.array([q, dq, u, q_nxt, dq_nxt]))

        #q = q_nxt
        #dq = dq_nxt

    #np.savetxt('data.txt', data)

    #print "With no disturbance \t", dynamics(q=q, dq=dq, u=u, disturb=False)
    #print "With disturbance \t", dynamics(q=q, dq=dq, u=u, disturb=True)


if __name__ == '__main__':
    
    main()
    #X is 1x4 matrix taking the input
    #x = [x,y,x_dot,y_dot]
    #x = [[1],[1],[1],[1]]

    #u is input parameters
    #u = [Fx, Fy]
    u = [[1],[1]]

    q = [[0], [0], [0], [0]]

    Dynamics(q,u)
    




#notes
#removed pendulum  x_next = 0#(I + A * dt) * x + (B * dt) * u