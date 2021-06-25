#!/usr/bin/env python
# -*- coding: utf-8 -*-
from WindowUtilFor360WebCam.WindowUtilFor400CAM084 import WindowUtilFor400CAM084


class WindowUtilFor360WebCam(object):
    def __init__(self, webcam_model='400-CAM084', use_autochange=True):
        print('WebCam Model : ' + webcam_model)
        if webcam_model == '400-CAM084':
            self._window_util = WindowUtilFor400CAM084(use_autochange)
        else:
            assert False, 'Invalid webcam_model specified'

        print('Auto Mode Change : ' + str(use_autochange))
        self._use_autochange = use_autochange

    def __call__(
        self,
        image,
    ):
        image_list = self._window_util(image)
        return image_list

    def set_mode(self, mode):
        self._window_util.set_mode(mode)
        return

    def get_mode(self):
        return self._window_util.get_mode()

    def set_autochange_flag(self, autochange_flag):
        return self._window_util.set_autochange_flag(autochange_flag)
