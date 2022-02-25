MATLAB_to_Python
===
1分子動画の軌跡描画ソフトの言語移行(MATLAB &rarr; Python)

## Description
MATLABで書かれていた1分子動画の軌跡描画ソフトをPythonで書き直した.<br>
現段階では2分子までの複数プロットも可能である.<br>
ファイル構成は以下のようになっている.

+ demo_data
    + Original_mov1.mp4
    + Tracks1_Original
        + workstate_0001.dat
        + workstate_0014.dat
+ video_split.py
+ original_images
    + 作成された画像
+ frame_count.py
+ get_xyposition.py
+ figure_draw.py
+ figure_images
    + 作成された画像
+ trajectory_draw.py
+ trajectory_images
    + 作成された画像
+ video_write.py
+ edited_video.mp4(作成された動画)

## Requirement
* Python 3.9.6
* cv2
* sys
* os
* pandas
* numpy

## Usage
`main.py`で設定されている初期パスを変更せずに使用するには, まずホームディレクトリ上にcloneする. <br>
次に, ホームディレクトリ上で`python3 MATLAB_to_Python/main.py`のようにして`main.py`を実行する必要がある.<br>

また, `main.py`にて<br>
+ プロットする図形のタイプ(circle, square)
+ 図形の色(white, light_blue, pink, purple, blue, yellow, yellow_green, red, orange)
+ プロットする軌跡のタイプ(disappear, keep)
+ 軌跡の色(図形の色と同様)

を選択することができる.
