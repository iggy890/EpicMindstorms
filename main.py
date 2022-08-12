from mindstorms import MSHub, Motor

class MSTools():
    def __init__(self):
        self.MSHub = MSHub()
        self.connected = True
        self.motors = []

    def move_on_port(self, speed: int = 100, port: str = "A", time: int = 1000, degree: int = 0):
        motor = Motor(port) # Create the motor class on the given port
        

        motor.start() # Start the motor
        motor.set_default_speed(speed) # Set the speed of the motor eg: 75

        motor.run_for_seconds(time, speed) # Run for the specified amount of time and speed
        motor.run_for_degrees(degree, speed) # Run at the given degree and speed

        motor.stop() # Stop the motor

        

# Initiliaze the hub
hub = MSHub()

# Motor Port 1 (left motor)
motor1 = Motor('A')

# Motor Port 2 (left motor)
motor2 = Motor('B')

