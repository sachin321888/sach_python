class Camera:
    def __init__(self,camera_id,resolution):
        self.camera_id = camera_id
        self.resolution = resolution

    def capture(self):
        print(f"capturing the {self.camera_id} camera")

    def display(self):
        print(f"displaying {self.camera_id} {self.resolution}")
              

camera= Camera("XS20","6kopengate")
print(camera.resolution)
print(camera.camera_id)


class Can:
    def __init__(self,channel,budrate):
        self.channel = channel
        self.budrate=budrate

    def connect(self):
        print(f"connecting to chanel {self.channel}")

    def send(self,can_id,data):
        print(f"sending ", hex(can_id),data)

can= Can("CAN1",200000)
can.connect()
can.send(123, {12,3,4})


class IVIAutomation:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def capture_screen(self):
        self.a.capture()

    def send_can(self,can_id,data):
        self.b.send(can_id, data)

    def connect_device(self):
        self.b.connect()

    def display_cam(self):
        self.a.display()

# camera = Camera("CAM01", "1920x1080")
# can = Can("CAN1", 500000)
ivi = IVIAutomation(camera, can)
ivi.capture_screen()
ivi.send_can(132,[0,1,2])
ivi.connect_device()
ivi.display_cam()