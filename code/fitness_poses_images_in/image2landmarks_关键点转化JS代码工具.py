# 读取此文件夹所有图片

import os
import cv2
import mediapipe as mp

landmark_out = []
# 读取当前文件夹所有图片jpg或png
def read_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if (filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".JPG")):
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
    return images

# 归一化一组列表
def normalize_list(list):
    if len(list) == 0:
        return list
    max_value = max(list)
    min_value = min(list)
    normalized_list = []
    for value in list:
        if max_value == min_value:
            normalized_list.append(0)
        else:
            normalized_list.append((value - min_value) / (max_value - min_value))
    return normalized_list

# 将图片列表中的每个图片提取mediapipe的关键点
def extract_keypoints_from_images(images):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(
            static_image_mode=True,
            model_complexity=1,
            smooth_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:
        for idx, image in enumerate(images):
            # 将图片进行pose识别
            results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            # 将landmarks信息
            # print(type(results.pose_landmarks.landmark))
            if results.pose_landmarks is not None:
                landmark_x = []
                landmark_y = []
                landmark_z = []
                landmark_visiblity = []
                landmark_combine = []
                # 仅选取nose, left_shoulder, right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist, left_thumb, right_thumb, left_hip, right_hip, left_knee, right_knee, left_ankle, right_anke的关键点
                select = [0, 11, 12, 13, 14, 15, 16, 17, 18, 23, 24, 25, 26, 27, 28]
                for i in select:
                    landmark_combine.append(results.pose_landmarks.landmark[i].x)
                    landmark_combine.append(results.pose_landmarks.landmark[i].y)
                    landmark_combine.append(results.pose_landmarks.landmark[i].z)
                    landmark_combine.append(results.pose_landmarks.landmark[i].visibility)

                '''for landmark in results.pose_landmarks.landmark:
                    # 归一化landmark.x, landmark.y, landmark.z
                    landmark_x = normalize_list(landmark_x)
                    landmark_y = normalize_list(landmark_y)
                    landmark_z = normalize_list(landmark_z)
                    landmark_visiblity = normalize_list(landmark_visiblity)
                    
                    landmark_combine.append(landmark.x)
                    landmark_combine.append(landmark.y)
                    landmark_combine.append(landmark.z)
                    landmark_combine.append(landmark.visibility)'''
                # 合并landmarks信息
                landmark_out.append(landmark_combine)
        # print(landmark_out)
        print(len(landmark_out))
        return landmark_out


images = read_images_from_folder("up")
print(len(images))
landmark_out = extract_keypoints_from_images(images)
# 写入txt文件
action_name = "JJ_Up"
with open("JJ_Up.txt", "w") as f:
    for i in landmark_out:
        f.write('knn.learn(' + str(i) + ', \"' + action_name + '\")')
        f.write('\n')
