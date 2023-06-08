# 仰卧起坐各模块和文件介绍：
`version: 20220808`

​		**poseembedding.py**是人体关键点归一化编码模块

​		**poseclassifier.py**是人体姿态分类模块，使用的算法是k-NN

​		**resultsmooth.py**是分类结果平滑模块，使用的是指数移动平均

​		**counter.py**是运动计数模块

​		**visualizer.py**是分类结果可视化模块

​		**extracttrainingsetkeypoint.py**是提取和处理训练集关键点模块，并将特征向量存储在csv文件中

​		**trainingsetprocess.py**是输入训练样本生成训练集以及训练集的检验校正的模块，里面说明了训练样本文件夹的要求

​		**videoprocess.py**是检测视频并计数动作的的模块（注意class_name参数的含义）

​		**videocapture.py**是调用摄像头实时检测并计数动作的模块（注意class_name参数的含义）

​		**main.py**是整个项目运行的入口程序

​		Roboto-Regular是**visualizer.py**中需要用到的字体文件

​		**sample.mp4**是样本视频，当然你也可以换成你自己做深蹲的测试视频，在**videoprocess.py**中把video_path换成您的视频路径即可，需要注意的是本项目使用cv2处理视频帧，cv2要求路径不能有中文。

​		**fitness_poses_csvs_out**文件夹里面的**down.csv**和**up.csv**就是使用作者自己拍摄的训练样本提取出来的仰卧起坐训练集文件，有了该文件后就可以直接运行本项目。

## 注意
* 修改动作需要对应修改**videocapture.py**和**videoprocess.py**中对应的动作名。
* 训练集数据为**fitness_poses_images_in**文件夹，分为up（坐起来）和down（躺下）两个动作指标。
* 仰卧起坐的数据文件储存在**fitness_poses_csvs_out**文件夹中的csv文件中。
* 运行前:
  * `pip install mediapipe`
  * `pip install opencv-python`(如果有问题还原成较低版本即可)