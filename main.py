import socket

from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from functools import partial

HOST = "192.168.0.1"
PORT = 53484

header = bytes.fromhex("030B534F4E59000000B00000")

status = bytes.fromhex("030B534F4E59000000B0000012535441546765742043555252454E54203500")

ret = str.encode("STATset POWER TOGGLE")

com = header + (len(ret)).to_bytes(1, 'big') + ret

class StressCanvasApp(App):

    def getCommand(self, label, wid, m, *largs):
        s = socket.socket()
        s.settimeout(0.1)
        try:
            s.connect((HOST, PORT))
        except:
            label.text = 'Failed: Cannot Connect with Monitor'
            return

        label.text = 'Connected'

        # Status Command
        ret = b'\x00'

        if(m == "Status"):
            return status


        # --- Navigation Commands --- #

        # Menu Command
        if(m == "Menu"):
            ret = str.encode("INFObutton MENU ")
        # Enter Command
        if(m == "Enter"):
            ret = str.encode("INFObutton MENUENT ")


        # Up Command
        if(m == "Up"):
            ret = str.encode("INFObutton MENUUP ")
        # DownCommand
        if(m == "Down"):
            ret = str.encode("INFObutton MENUDOWN ")

        # Numberpad Enter
        if(m == "Ent"):
            ret = str.encode("INFObutton ENTER ")
        # Numberpad Delete
        if(m == "Del"):
            ret = str.encode("INFObutton DELETE ")

        # Number 0
        if(m == "0"):
            ret = str.encode("INFObutton 0 ")
        # Number 1
        if(m == "1"):
            ret = str.encode("INFObutton 1 ")
        # Number 2
        if(m == "2"):
            ret = str.encode("INFObutton 2 ")
        # Number 3
        if(m == "3"):
            ret = str.encode("INFObutton 3 ")
        # Number 4
        if(m == "4"):
            ret = str.encode("INFObutton 4 ")
        # Number 5
        if(m == "5"):
            ret = str.encode("INFObutton 5 ")
        # Number 6
        if(m == "6"):
            ret = str.encode("INFObutton 6 ")
        # Number 7
        if(m == "7"):
            ret = str.encode("INFObutton 7 ")
        # Number 8
        if(m == "8"):
            ret = str.encode("INFObutton 8 ")
        # Number 9
        if(m == "9"):
            ret = str.encode("INFObutton 9 ")


        # --- Modification Command --- #

        # Power Command
        if(m == "Power"):
            ret = str.encode("STATset POWER TOGGLE")

        # Degauss Command
        if(m == "Degauss"):
            ret = str.encode("STATset DEGAUSS TOGGLE")

        if(m == "ScanMode"):
            ret = str.encode("STATset SCANMODE TOGGLE")
        if(m == "HorizDelay"):
            ret = str.encode("STATset HDELAY TOGGLE")
        if(m == "VertDelay"):
            ret = str.encode("STATset VDELAY TOGGLE")
        if(m == "Mono"):
            ret = str.encode("STATset MONOCHR TOGGLE")
        if(m == "Comb"):
            ret = str.encode("STATset COMB TOGGLE")
        if(m == "CharMute"):
            ret = str.encode("STATset CHARMUTE TOGGLE")
        if(m == "ColorTemp"):
            ret = str.encode("STATset COLADJ TOGGLE")
        if(m == "Aspect"):
            ret = str.encode("STATset ASPECT TOGGLE")
        if(m == "ExtSync"):
            ret = str.encode("STATset EXTSYNC TOGGLE")
        if(m == "BlueOnly"):
            ret = str.encode("STATset BLUEONLY TOGGLE")
        if(m == "RedCut"):
            ret = str.encode("STATset RCUTOFF TOGGLE")
        if(m == "BlueCut"):
            ret = str.encode("STATset BCUTOFF TOGGLE")
        if(m == "GreenCut"):
            ret = str.encode("STATset GCUTOFF TOGGLE")
        if(m == "Marker"):
            ret = str.encode("STATset Marker TOGGLE")
        if(m == "ChromaUp"):
            ret = str.encode("STATset CHROMAUP TOGGLE")

        if ret == b'\x00':
            print("Warning, not a recognized command. Might have unexpected effects")
            return

        # Return properly formatted command (header + payload length + payload)
        com = header + (len(ret)).to_bytes(1, 'big') + ret

        # Send Command
        s.send(com)
        data = s.recv(1024)
        if data == b'\x03\x0bSONY\x00\x00\x01\xb0\x00\x00\x00':
            print("Command Recieved Successfully")

    def build(self):
        wid = Widget()

        label = Label(text='Waiting for input...')

        # Row 1
        btn_power = Button(text='Power',
                            on_press=partial(self.getCommand, label, wid, "Power"))
        btn_degauss = Button(text='Degauss',
                            on_press=partial(self.getCommand, label, wid, "Degauss"))
        btn_menu = Button(text='Menu',
                            on_press=partial(self.getCommand, label, wid, "Menu"))
        btn_enter = Button(text='Enter',
                            on_press=partial(self.getCommand, label, wid, "Enter"))
        btn_up = Button(text='Up',
                            on_press=partial(self.getCommand, label, wid, "Up"))
        btn_down = Button(text='Down',
                            on_press=partial(self.getCommand, label, wid, "Down"))
        layout1 = BoxLayout(size_hint=(1, .2), height=50)
        layout1.add_widget(btn_power)
        layout1.add_widget(btn_degauss)
        layout1.add_widget(btn_menu)
        layout1.add_widget(btn_enter)
        layout1.add_widget(btn_up)
        layout1.add_widget(btn_down)

        # Row 2
        btn_0 = Button(text='0',
                            on_press=partial(self.getCommand, label, wid, "0"))
        btn_1 = Button(text='1',
                            on_press=partial(self.getCommand, label, wid, "1"))
        btn_2 = Button(text='2',
                            on_press=partial(self.getCommand, label, wid, "2"))
        btn_3 = Button(text='3',
                            on_press=partial(self.getCommand, label, wid, "3"))
        btn_4 = Button(text='4',
                            on_press=partial(self.getCommand, label, wid, "4"))
        btn_5 = Button(text='5',
                            on_press=partial(self.getCommand, label, wid, "5"))
        btn_6 = Button(text='6',
                            on_press=partial(self.getCommand, label, wid, "6"))
        btn_7 = Button(text='7',
                            on_press=partial(self.getCommand, label, wid, "7"))
        btn_8 = Button(text='8',
                            on_press=partial(self.getCommand, label, wid, "8"))
        btn_9 = Button(text='9',
                            on_press=partial(self.getCommand, label, wid, "9"))
        layout2 = BoxLayout(size_hint=(1, .2), height=50)
        layout2.add_widget(btn_0)
        layout2.add_widget(btn_1)
        layout2.add_widget(btn_2)
        layout2.add_widget(btn_3)
        layout2.add_widget(btn_4)
        layout2.add_widget(btn_5)
        layout2.add_widget(btn_6)
        layout2.add_widget(btn_7)
        layout2.add_widget(btn_8)
        layout2.add_widget(btn_9)

        # Row 3
        btn_nument = Button(text='NumberPad Enter',
                            on_press=partial(self.getCommand, label, wid, "Ent"))
        btn_numdel = Button(text='NumberPad Delete',
                            on_press=partial(self.getCommand, label, wid, "Del"))
        layout3 = BoxLayout(size_hint=(1, .2), height=50)
        layout3.add_widget(btn_nument)
        layout3.add_widget(btn_numdel)

        # Row 4
        btn_169 = Button(text='16:9',
                            on_press=partial(self.getCommand, label, wid, "Aspect"))
        btn_extsync = Button(text='ExtSync',
                            on_press=partial(self.getCommand, label, wid, "ExtSync"))
        btn_blueonly = Button(text='B Only',
                            on_press=partial(self.getCommand, label, wid, "BlueOnly"))
        btn_redcut = Button(text='R Off',
                            on_press=partial(self.getCommand, label, wid, "RedCut"))
        btn_bluecut = Button(text='B Off',
                            on_press=partial(self.getCommand, label, wid, "BlueCut"))
        btn_greencut = Button(text='G Off',
                            on_press=partial(self.getCommand, label, wid, "GreenCut"))
        layout4 = BoxLayout(size_hint=(1, .2), height=50)
        layout4.add_widget(btn_169)
        layout4.add_widget(btn_extsync)
        layout4.add_widget(btn_blueonly)
        layout4.add_widget(btn_redcut)
        layout4.add_widget(btn_bluecut)
        layout4.add_widget(btn_greencut)

        # Row 5
        btn_scanmode = Button(text='Scan',
                            on_press=partial(self.getCommand, label, wid, "ScanMode"))
        btn_hdelay = Button(text='H. Delay',
                            on_press=partial(self.getCommand, label, wid, "HorizDelay"))
        btn_vdelay = Button(text='V. Delay',
                            on_press=partial(self.getCommand, label, wid, "VertDelay"))
        btn_mono = Button(text='Mono',
                            on_press=partial(self.getCommand, label, wid, "Mono"))
        btn_comb = Button(text='Comb',
                            on_press=partial(self.getCommand, label, wid, "Comb"))
        btn_colortemp = Button(text='Col. Temp',
                            on_press=partial(self.getCommand, label, wid, "ColorTemp"))

        layout5 = BoxLayout(size_hint=(1, .2), height=50)
        layout5.add_widget(btn_scanmode)
        layout5.add_widget(btn_hdelay)
        layout5.add_widget(btn_vdelay)
        layout5.add_widget(btn_mono)
        layout5.add_widget(btn_comb)
        layout5.add_widget(btn_colortemp)

        # Row 6
        layout6 = BoxLayout(size_hint=(1, .2), height=50)
        layout6.add_widget(label)

        # Row 7
        layout7 = BoxLayout(size_hint=(1, .2), height=50)
        label1 = Label(text='AndEmu15-r: Simple BKM-15r Emulator')
        layout7.add_widget(label1)

        # Row 8
        layout8 = BoxLayout(size_hint=(1, .2), height=50)
        label2 = Label(text='Written by Andy Gatza (AKA 144a)')
        layout8.add_widget(label2)


        #layout2.add_widget(label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)

        root.add_widget(layout7)
        root.add_widget(layout8)
        root.add_widget(layout5)
        root.add_widget(layout4)
        root.add_widget(layout2)
        root.add_widget(layout3)
        root.add_widget(layout1)
        root.add_widget(layout6)

        return root


if __name__ == '__main__':
    StressCanvasApp().run()
