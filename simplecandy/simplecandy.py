#!/usr/bin/env python

import opc


class SimpleCandy(object):

    def __init__(self, server_id_port, numpixels=50):
        self.pixels = [(0, 0, 0)] * numpixels
        self.client = opc.Client(server_id_port)

    def off(id=None):
        if id:
            self.pixels = [(0, 0, 0)] * numpixels
        else:
            self.pixels[id] = (0, 0, 0)
        self.__paint()

    def lightOn(self, id, r, g, b):
        self.pixels[id] = (0xff * r, 0xff * g, 0xff * b)
        self.__paint()

    def __paint(self):
        self.client.put_pixels(self.pixels)
