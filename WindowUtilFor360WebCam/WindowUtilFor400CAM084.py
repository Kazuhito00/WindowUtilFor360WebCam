#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy

import cv2 as cv
import numpy as np


class WindowUtilFor400CAM084(object):
    def __init__(self, use_autochange=True):
        self._use_autochange = use_autochange

        self._capture_mode = 0
        self._select_mode = self._capture_mode

        self._capture_mode_set = [
            self._capture_mode_00,
            self._capture_mode_01,
            self._capture_mode_02,
            self._capture_mode_03,
            self._capture_mode_04,
            self._capture_mode_05,
            self._capture_mode_06,
        ]

    def __call__(
        self,
        image,
    ):
        if self._use_autochange is True:
            mode_image_list = self._get_mode_image(image)
            self._capture_mode = self._analysis_mode_image(mode_image_list)

        image_list = self._capture_mode_set[self._capture_mode](image)

        return image_list

    def set_mode(self, mode):
        if 0 <= mode <= (len(self._capture_mode_set) - 1):
            self._select_mode = mode
            self._capture_mode = self._select_mode
        return

    def get_mode(self):
        return self._capture_mode

    def set_autochange_flag(self, autochange_flag):
        self._use_autochange = autochange_flag
        return

    def _capture_mode_00(self, image):
        image01 = copy.deepcopy(image)
        return [image01]

    def _capture_mode_01(self, image):
        image_width, image_height = image.shape[1], image.shape[0]

        y_offset = 5

        image01 = copy.deepcopy(image[y_offset:int(image_height / 2),
                                      0:image_width])
        image02 = copy.deepcopy(image[int(image_height / 2) +
                                      y_offset:image_height, 0:image_width])

        return [image01, image02]

    def _capture_mode_02(self, image):
        image_width, image_height = image.shape[1], image.shape[0]

        image01 = copy.deepcopy(image[int(image_height * 3 /
                                          8):int(image_height * 5 / 8),
                                      0:image_width])
        return [image01]

    def _capture_mode_03(self, image):
        image_width, image_height = image.shape[1], image.shape[0]

        y_offset = 3

        image01 = copy.deepcopy(image[0:int(image_height * 1 / 4) - y_offset,
                                      0:image_width])
        image02 = copy.deepcopy(image[int(image_height * 1 / 4) +
                                      y_offset:image_height, 0:image_width])

        return [image01, image02]

    def _capture_mode_04(self, image):
        image_width, image_height = image.shape[1], image.shape[0]

        y_offset = 3
        x_offset = 3

        image01 = copy.deepcopy(image[0:int(image_height * 1 / 4) - y_offset,
                                      0:image_width])
        image02 = copy.deepcopy(
            image[int(image_height * 1 / 4) + y_offset:image_height,
                  0:int(image_width / 2) - x_offset])
        image03 = copy.deepcopy(
            image[int(image_height * 1 / 4) + y_offset:image_height,
                  int(image_width / 2) + x_offset + 1:image_width])

        return [image01, image02, image03]

    def _capture_mode_05(self, image):
        image01 = copy.deepcopy(image)
        return [image01]

    def _capture_mode_06(self, image):
        image01 = copy.deepcopy(image)
        return [image01]

    def _get_mode_image(self, image):
        image_width, image_height = image.shape[1], image.shape[0]

        mode_area = copy.deepcopy(image[int(image_height * 65 /
                                            100):int(image_height * 83 / 100),
                                        0:image_width])

        mode_area_width, mode_area_height = mode_area.shape[
            1], mode_area.shape[0]

        offset_01 = 4
        mode_image01 = mode_area[0:mode_area_height,
                                 int(mode_area_width * offset_01 /
                                     100):int(mode_area_width * offset_01 /
                                              100) +
                                 int(mode_area_width * 1 / 7)]

        offset_02 = 19.5
        mode_image02 = mode_area[0:mode_area_height,
                                 int(mode_area_width * offset_02 /
                                     100):int(mode_area_width * offset_02 /
                                              100) +
                                 int(mode_area_width * 1 / 7)]

        offset_03 = 35
        mode_image03 = mode_area[0:mode_area_height,
                                 int(mode_area_width * offset_03 /
                                     100):int(mode_area_width * offset_03 /
                                              100) +
                                 int(mode_area_width * 1 / 7)]

        offset_04 = 50.5
        mode_image04 = mode_area[0:mode_area_height,
                                 int(mode_area_width * offset_04 /
                                     100):int(mode_area_width * offset_04 /
                                              100) +
                                 int(mode_area_width * 1 / 7)]

        offset_05 = 66
        mode_image05 = mode_area[0:mode_area_height,
                                 int(mode_area_width * offset_05 /
                                     100):int(mode_area_width * offset_05 /
                                              100) +
                                 int(mode_area_width * 1 / 7)]

        offset_06 = 81.5
        mode_image06 = mode_area[0:mode_area_height,
                                 int(mode_area_width * offset_06 /
                                     100):int(mode_area_width * offset_06 /
                                              100) +
                                 int(mode_area_width * 1 / 7)]

        return [
            mode_image01, mode_image02, mode_image03, mode_image04,
            mode_image05, mode_image06
        ]

    def _analysis_mode_image(self, mode_image_list):
        mode = self._capture_mode

        non_zero_count_list = []

        for index, mode_image in enumerate(mode_image_list):
            # HSV色空間で選択色の抽出
            hsv = [40, 225, 220]
            hsv_offset = 30
            hsv_lower = np.array([
                hsv[0] - hsv_offset,
                hsv[1] - hsv_offset,
                hsv[2] - hsv_offset,
            ])
            hsv_upper = np.array([
                hsv[0] + hsv_offset,
                hsv[1] + hsv_offset,
                hsv[2] + hsv_offset,
            ])
            mode_image = cv.cvtColor(mode_image, cv.COLOR_BGR2HSV)
            hsv_mask = cv.inRange(mode_image, hsv_lower, hsv_upper)

            # クロージング処理による粒ノイズ除去
            kernel = np.ones((3, 3), np.uint8)
            hsv_mask = cv.morphologyEx(hsv_mask, cv.MORPH_CLOSE, kernel)

            # 大きい領域の上位のみマスク画像として描画する
            mask = np.zeros(mode_image.shape, np.uint8)
            contours = cv.findContours(hsv_mask, cv.RETR_EXTERNAL,
                                       cv.CHAIN_APPROX_SIMPLE)[0]
            contours = sorted(contours,
                              key=lambda x: cv.contourArea(x),
                              reverse=True)
            for i, controur in enumerate(contours):
                if i < 1:
                    mask = cv.drawContours(mask, [controur],
                                           -1,
                                           color=(255, 255, 255),
                                           thickness=-1)

            mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
            _, mask = cv.threshold(mask, 0, 255, cv.THRESH_OTSU)

            # 抽出領域のピクセル数が過半数の場合、モード選択状態と判断
            mode_image_pixel_num = mode_image.shape[0] * mode_image.shape[1]
            non_zero_count = cv.countNonZero(mask)
            non_zero_count_list.append(non_zero_count)
            if non_zero_count > int(mode_image_pixel_num / 2):
                self._select_mode = (index + 1)

        if np.all(np.array(non_zero_count_list) == 0):
            mode = self._select_mode
        return mode
