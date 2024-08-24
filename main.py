import cv2


def split_video_to_images(video_path, output_folder, desired_fps=1):
    video_capture = cv2.VideoCapture(video_path)
    video_capture.set(cv2.CAP_PROP_FPS, desired_fps)

    frame_number = 0
    while video_capture.isOpened():
        frame_is_read, frame = video_capture.read()
        if not frame_is_read:
            break

        image_filename = f'frame_{frame_number}.jpg'
        cv2.imwrite(image_filename, frame)
        frame_number += 1

    video_capture.release()


# Usage
input_video_path = 'video.mp4'
output_folder_path = 'output_images'
split_video_to_images(input_video_path, output_folder_path, desired_fps=1)
