#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import argparse

import cv2 as cv

from WindowUtilFor360WebCam import WindowUtilFor360WebCam


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", help='cap width', type=int, default=960)

    parser.add_argument("--webcam_model", type=str, default='400-CAM084')
    parser.add_argument('--unuse_autochange', action='store_true')

    args = parser.parse_args()

    return args


def main():
    # 引数解析 #################################################################
    args = get_args()

    cap_device = args.device
    cap_width = args.width
    cap_height = int(cap_width / 16 * 9)

    webcam_model = args.webcam_model
    use_autochange = not (args.unuse_autochange)

    # カメラ準備 ###############################################################
    cap = cv.VideoCapture(cap_device)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    print("CAP_PROP_FRAME_WIDTH : " + str(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
    print("CAP_PROP_FRAME_HEIGHT : " + str(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
    print("CAP_PROP_FPS : " + str(cap.get(cv.CAP_PROP_FPS)))

    window_util = WindowUtilFor360WebCam(webcam_model, use_autochange)

    #  ########################################################################
    curr_image_count = 0
    prev_image_count = 0

    while True:
        # カメラキャプチャ #####################################################
        ret, image = cap.read()
        if not ret:
            break

        # モードに従った画像の取得 ##############################################
        image_list = window_util(image)

        # 画面反映 #############################################################
        for index, temp_image in enumerate(image_list):
            cv.imshow(webcam_model + ':' + str(index), temp_image)
            curr_image_count = index + 1

        if curr_image_count < prev_image_count:
            for index in range(curr_image_count, prev_image_count):
                cv.destroyWindow(webcam_model + ':' + str(index))

        prev_image_count = curr_image_count

        # キー処理(ESC：終了) #################################################
        key = cv.waitKey(1)
        if 48 <= key <= 57:  # 0～9
            mode_id = (key - 48)
            window_util.set_mode(mode_id)
        elif key == 27:  # ESC
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
