class Radio:
    def colbranhead(self,col,bran,headp,ACpw):
        self.color=col
        self.brand=bran
        self.headphone=head
        self.ACPower=ACpw
    def power_switch(self,status):
        if status==True:
            self.power_led="Green"
        else:
            self.power_led="Red"
    def mode_switch(self,status):
        if status=="AM":
            self.mode_led="AM"
        else:
            self.mode_led="FM"
    def band_tuner(self,x):
        self.frequency=x
    def volume_tuner(self,x):
        self.volume=x
print("Enter the color,brand,Ac Power,Headphone of the Radio")
input(x,y,z,w)
obj1=Radio()
obj1.colbranhead(x,y,z,w)