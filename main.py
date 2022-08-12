from mindstorms import MSHub, Motor

class MSTools():
    def __init__(self):
        self.MSHub = MSHub()
        self.connected = True
        self.motors = []

    def __move_and_start__(port: str, speed: int, time: int):
        motor = Motor(port) # Create the motor class and assign it

        motor.start() # Start the motor
        motor.set_default_speed(speed) # Set the speed of the motor eg: 75
        
        motor.run_for_time(time) # Run for the specified amount of time
        motor.stop() # Stop the motor


    def move(self, ports: list, speeds: list, times: list):
        for port, speed, time in zip(ports, speeds, times):
            try:
                self.__move_and_start__(port, speed, time)
            except Exception:
                return
        

        

# Initiliaze the hub
hub = MSHub()

# Motor Port 1 (left motor)
motor1 = Motor('A')

# Motor Port 2 (left motor)
motor2 = Motor('B')

