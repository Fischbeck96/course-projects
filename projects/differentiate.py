import numpy as np


def differentiate(u: np.ndarray, dt: float) -> np.ndarray:
    disc=np.zeros(len(u))
    for i in range(len(u)):
        if dt*i==0:
            disc[i]=(u[1]-u[0])/dt
        elif 1<=i<len(u)-1:
            disc[i]=((u[i+1]-u[i-1])/(2*dt))
        else:
            disc[i]=(u[i]-u[i-1])/dt
    return disc

tt= np.linspace(0,1,10)    
print(differentiate(tt**2,0.1))


def differentiate_vector(u: np.ndarray, dt: float) -> np.ndarray:
    d= np.zeros(len(u))
    d[0]=(u[1]-u[0])/dt
    
    d[1:-1] = (u[2:] -u[0:-2])/(2*dt)
    
    d[-1]=(u[-1]-u[-2])/dt
        
    #d[1:N_t]=(u[2:N_t+1] -u[0:N_t-1])/(2*dt)
    return d
print("hi",differentiate_vector(tt**2,0.1))
def test_differentiate():
    t = np.linspace(0, 1, 10)
    dt = t[1] - t[0]
    u = t**2
    du1 = differentiate(u, dt)
    du2 = differentiate_vector(u, dt)
    assert np.allclose(du1, du2)

if __name__ == '__main__':
    test_differentiate()