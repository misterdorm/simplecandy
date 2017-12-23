#!/usr/bin/env python

import opc


class SimpleCandy(object):

    def __init__(self, server_id_port, numpixels=50):
        self.client = opc.Client(server_id_port)
        self.numpixels = numpixels
        self.lightOff()

    def lightOff(self, id=None):
        self.lightOn(0, 0, 0, id)

    def lightOn(self, r, g, b, id=None):
        if id is not None:
            self.pixels[id] = (0xff * g/100, 0xff * r/100, 0xff * b/100)
        else:
            self.pixels = [(0xff * g/100, 0xff * r/100, 0xff * b/100)] * self.numpixels
        self.__paint()

    def pixels(self, pixels):
        self.pixels = pixels
        self.__paint()

    def __paint(self):
        self.client.put_pixels(self.pixels)
