# import cv2
# from ultralytics import YOLO
# import os
# import random
# import matplotlib.pyplot as plt
#
# # Load the YOLO model
# model = YOLO('trained_models/train3/best.pt')  # or yolov5s.pt if using YOLOv5
#
# # Define class ID for 'car' in COCO dataset
# CAR_CLASS_ID = 2  # COCO: 2 = 'car'
#
# # Define a simple line to count cars that cross it
# LINE_POSITION = 300  # Adjust based on video resolution
#
# def is_crossing_line(y, prev_y, line_y):
#     return (prev_y < line_y <= y) or (y < line_y <= prev_y)
#
# def process_video(video_path):
#     cap = cv2.VideoCapture(video_path)
#     car_count = 0
#     tracked_objects = {}
#     next_id = 0
#
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#
#         results = model(frame)[0]
#         current_frame_objects = {}
#
#         for box in results.boxes:
#             cls = int(box.cls)
#             if cls != CAR_CLASS_ID:
#                 continue
#
#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             cx = int((x1 + x2) / 2)
#             cy = int((y1 + y2) / 2)
#
#             # Simple object tracking by position (Euclidean distance)
#             matched_id = None
#             for obj_id, (px, py) in tracked_objects.items():
#                 if np.linalg.norm([cx - px, cy - py]) < 50:
#                     matched_id = obj_id
#                     break
#
#             if matched_id is None:
#                 matched_id = next_id
#                 next_id += 1
#
#             # Check if this object has crossed the line
#             if matched_id in tracked_objects:
#                 _, prev_y = tracked_objects[matched_id]
#                 if is_crossing_line(cy, prev_y, LINE_POSITION):
#                     car_count += 1
#                     print(f"Car #{matched_id} crossed the line. Total: {car_count}")
#
#             current_frame_objects[matched_id] = (cx, cy)
#
#             # Optional: draw bounding boxes
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.putText(frame, f"ID: {matched_id}", (x1, y1 - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
#
#         tracked_objects = current_frame_objects
#
#         # Draw the counting line
#         cv2.line(frame, (0, LINE_POSITION), (frame.shape[1], LINE_POSITION), (0, 0, 255), 2)
#
#         # Optional: show the video
#         # cv2.imshow('Car Counter', frame)
#         # if cv2.waitKey(1) & 0xFF == ord('q'):
#         #     break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
#     print(f"Total cars counted: {car_count}")
#
#
# # Run the script
# if __name__ == "__main__":
#     import sys
#     # if len(sys.argv) < 2:
#     #     print("Usage: python car_counter.py path_to_video.mp4")
#     # else:
#     #     process_video(sys.argv[1])
#     process_video("C:\\Users\\kamil\\Desktop\\carssssss.mp4")

import cv2
import numpy as np
from ultralytics import YOLO
#Obce
#model = YOLO("yolov8n.pt")

#CAR_CLASS_ID = 2
#LINE_POSITION_X = 300

#nasze
model = YOLO('trained_models/train3/best.pt')

CAR_CLASS_ID = 0
LINE_POSITION_X = 450

def is_crossing_line(curr_x, prev_x, line_x):
    return (prev_x < line_x <= curr_x) or (curr_x < line_x <= prev_x)

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    car_count = 0
    tracked_objects = {}
    next_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)[0]
        current_frame_objects = {}

        for box in results.boxes:
            cls = int(box.cls)
            if cls != CAR_CLASS_ID:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            matched_id = None
            for obj_id, (prev_x, prev_y) in tracked_objects.items():
                if np.linalg.norm([cx - prev_x, cy - prev_y]) < 50:
                    matched_id = obj_id
                    break

            if matched_id is None:
                matched_id = next_id
                next_id += 1

            if matched_id in tracked_objects:
                prev_x, _ = tracked_objects[matched_id]
                if is_crossing_line(cx, prev_x, LINE_POSITION_X):
                    car_count += 1
                    print(f"Car #{matched_id} crossed the line. Total: {car_count}")

            current_frame_objects[matched_id] = (cx, cy)

            # Draw bounding box and ID
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"ID: {matched_id}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

        tracked_objects = current_frame_objects


        cv2.line(frame, (LINE_POSITION_X, 0), (LINE_POSITION_X, frame.shape[0]), (0, 0, 255), 2)


        cv2.putText(frame, f"Cars Counted: {car_count}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)


        cv2.imshow('Car Counter', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Total cars counted: {car_count}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python app.py path_to_video.mp4")
    else:
        process_video(sys.argv[1])

