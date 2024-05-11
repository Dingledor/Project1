from tkinter import *
from logic import *


class GUI:
    def __init__(self, window, logic):
        self.window = window
        window.image_power = PhotoImage(file="images/powerbutton.png")
        window.image_remote = PhotoImage(file="images/remotebase.png")
        window.image_volume_up = PhotoImage(file="images/volumeup.png")
        window.image_volume_down = PhotoImage(file="images/volumedown.png")
        window.image_channel_up = PhotoImage(file="images/channelup.png")
        window.image_channel_down = PhotoImage(file="images/channeldown.png")
        window.image_mute = PhotoImage(file="images/mutebutton.png")

        self.canvas = Canvas(self.window, width=174, height=665)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=window.image_remote, anchor='nw')
        self.button_power = Button(self.window, bd='0', command=logic.power, image=window.image_power,
                                   background='black', activebackground='black')
        self.button_power.place(x=20, y=20)
        self.button_volume_up = Button(self.window, bd='0', command=logic.volume_up, image=window.image_volume_up,
                                       background='black', activebackground='black')
        self.button_volume_up.place(x=21, y=268)
        self.button_volume_down = Button(self.window, bd='0', command=logic.volume_down, image=window.image_volume_down,
                                         background='black', activebackground='black')
        self.button_volume_down.place(x=21, y=311)
        self.button_channel_up = Button(self.window, bd='0', command=logic.channel_up, image=window.image_channel_up,
                                        background='black', activebackground="black")
        self.button_channel_up.place(x=114, y=266)
        self.button_channel_down = Button(self.window, bd='0', command=logic.channel_down,
                                          image=window.image_channel_down, background='black', activebackground="black")
        self.button_channel_down.place(x=114, y=309)
        self.button_mute = Button(self.window, bd='0', image=window.image_mute, command=logic.mute,
                                  background='black', activebackground='black')
        self.button_mute.place(x=66, y=320)

        self.tv = TV(Toplevel(self.window))
        self.tv.window.geometry("980x715+%d+%d" % (self.window.winfo_x() + 200, self.window.winfo_y()))


class TV:
    def __init__(self, window):
        self.window = window
        self.channel = StringVar(value='')
        self.volume = StringVar(value='')
        self.volumeprogress = StringVar(value='')
        window.title("Television")
        window.geometry("980x715")
        window.image_channels = (PhotoImage(file="images/channel0television.png"),
                                 PhotoImage(file="images/channel1television.png"),
                                 PhotoImage(file="images/channel2television.png"),
                                 PhotoImage(file="images/channel3television.png"))
        window.image_television = PhotoImage(file="images/television.png")
        window.image_indicator = PhotoImage(file="images/indicator.png")
        self.canvas = Canvas(self.window, width=980, height=715)
        self.canvas.pack(fill='both', expand=True)
        self.canvas_television = self.canvas.create_image(0, 0, image=window.image_television, anchor='nw')
        self.label_indicator = Label(self.canvas, image=window.image_indicator, bd='0', bg="black")

        self.label_channel = Label(self.window, textvariable=self.channel, background="black",
                                   foreground="white", font=("Terminal", 40))
        self.label_channel.place(x=100, y=100)
        self.label_volume = Label(self.window, textvariable=self.volume, background="black",
                                  foreground="white", font=("Terminal", 40))
        self.label_volume.place(x=100, y=170)
        self.frame_volumebar = Frame(self.window, background="black", width=275, height=35)
        self.label_volumebar = Label(self.frame_volumebar, textvariable=self.volumeprogress, background="black",
                                     foreground="white", font=("Terminal", 20))
        self.frame_volumebar.pack_propagate(False)
        self.frame_volumebar.place(x=100, y=230)
        self.label_volumebar.pack(side=LEFT)
