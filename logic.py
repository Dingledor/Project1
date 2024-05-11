from gui import *


class Logic:
    MIN_VOLUME = 0
    MAX_VOLUME = 11
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, window) -> None:
        """
        Set default variables for television status, muted, volume and channel then initialize remote window
        """
        self.__status = False
        self.__muted = False
        self.__volume = Logic.MIN_VOLUME
        self.__channel = Logic.MIN_CHANNEL
        self.gui = GUI(window, self)

    def power(self) -> None:
        """
        Toggle power on or off
        """
        if self.__status:
            self.__status = False
            self.gui.tv.canvas.itemconfig(self.gui.tv.canvas_television, image=self.gui.tv.window.image_television)
            self.gui.tv.volumeprogress.set('')
            self.gui.tv.label_indicator.place_forget()
            self.gui.tv.volume.set("")
            self.gui.tv.channel.set("")
        else:
            self.__status = True
            self.gui.tv.canvas.itemconfig(self.gui.tv.canvas_television,
                                          image=self.gui.tv.window.image_channels[self.__channel])
            self.gui.tv.label_indicator.place(x=660, y=677)
            self.gui.tv.channel.set(f"CHANNEL: {self.__channel}")
            self.gui.tv.volume.set(f"VOLUME: {self.__volume}")
            self.gui.tv.volumeprogress.set('█' * self.__volume)

    def mute(self) -> None:
        """
        Toggle muted status on or off
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.gui.tv.volume.set(f"VOLUME: {self.__volume}")
                self.gui.tv.frame_volumebar.place(x=100, y=230)
                self.gui.tv.label_volumebar.pack(side=LEFT)
            else:
                self.__muted = True
                self.gui.tv.volume.set(f"MUTED")
                self.gui.tv.volumeprogress.set('' * self.__volume)
                self.gui.tv.frame_volumebar.place_forget()

    def channel_up(self) -> None:
        """
        Increase channel number and reset to min channel if at max
        """
        if self.__status:
            if self.__channel < Logic.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Logic.MIN_CHANNEL
            self.gui.tv.canvas.itemconfig(self.gui.tv.canvas_television,
                                          image=self.gui.tv.window.image_channels[self.__channel])
            self.gui.tv.channel.set(f'CHANNEL: {self.__channel}')

    def channel_down(self) -> None:
        """
        Decrease channel number and reset to max channel if at min
        """
        if self.__status:
            if self.__channel > Logic.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Logic.MAX_CHANNEL
            self.gui.tv.canvas.itemconfig(self.gui.tv.canvas_television,
                                          image=self.gui.tv.window.image_channels[self.__channel])
            self.gui.tv.channel.set(f'CHANNEL: {self.__channel}')

    def volume_up(self) -> None:
        """
        Increase volume number unless volume is at max
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume < Logic.MAX_VOLUME:
                self.__volume += 1
            self.gui.tv.volumeprogress.set('█' * self.__volume)
            self.gui.tv.volume.set(f'VOLUME: {self.__volume}')

    def volume_down(self) -> None:
        """
        Decrease volume number unless volume is at min
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume > Logic.MIN_VOLUME:
                self.__volume -= 1
            self.gui.tv.volume.set(f'VOLUME: {self.__volume}')
            self.gui.tv.volumeprogress.set('█' * self.__volume)