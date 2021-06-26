# WindowUtilFor360WebCam
https://user-images.githubusercontent.com/37477845/123508197-de752100-d6a8-11eb-97be-9cb73b982eed.mp4


サンワダイレクトの[360度Webカメラ(400-CAM084)](https://direct.sanwa.co.jp/ItemPage/400-CAM084)のウィンドウをOpenCVで分割するプログラムです。<br>
実機での確認は取れていませんが、j5createの[360° パノラマミーティングカメラ(JVCU360)](https://jp.j5create.com/products/model_jvcu360)でも使用できると思います(メニュー自動選択を利用する際は検出色の調整が必要かもしれません)

# Requirement 
* opencv-python 4.5.2.54 or later

# Usage
以下コマンドでサンプルを起動できます。<br>
デフォルトではカメラ側のモード切替メニューを画像処理で判別して、自動で表示が切り替わるようになっています。<br>
また、キーボードの数字を押下することでモードを切り替えることが出来ます。<br>
　0：そのまま表示<br>
　1：上下2分割360度<br>
　2：パノラマ360度<br>
　3：360度+1方向<br>
　4：360度+2方向<br>
　5：広角90度<br>
　6：広角120度<br>
```bash
python sample.py
```
実行時には、以下のオプションが指定可能です。
   
* --device<br>
カメラデバイス番号の指定<br>
デフォルト：0
* --width<br>
カメラキャプチャ時の横幅 ※縦幅はwidth*(9/16)で計算されます<br>
デフォルト：960
* --device<br>
カメラデバイス番号の指定<br>
デフォルト：0
* --webcam_model<br>
カメラデバイス種類の指定 ※現状、400-CAM084のみ<br>
デフォルト：400-CAM084
* --unuse_autochange<br>
画像解析によるメニュー自動選択の不使用<br>
デフォルト：指定なし

# Device

|01：400-CAM084|02：-|
:---:|:---:
|<img src="https://user-images.githubusercontent.com/37477845/123508560-21d08f00-d6ab-11eb-8fd2-1bf07358e698.jpg" loading="lazy" width="400px">|<img src="https://user-images.githubusercontent.com/37477845/122628310-5e6f1a00-d0f0-11eb-946c-55d1dc6920ef.png" loading="lazy" width="400px">|

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
WindowUtilFor360WebCam is under [Apache-2.0 License](LICENSE).
