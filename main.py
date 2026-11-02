import cv2
import numpy as np

cap = cv2.VideoCapture("input_video.mp4")

ret, first_frame = cap.read()
prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

h, w = prev_gray.shape
mask = np.zeros_like(prev_gray)
mask[int(h * 0.50):int(h * 0.85), int(w * 0.15):int(w * 0.85)] = 255

points = cv2.goodFeaturesToTrack(prev_gray, maxCorners=80, qualityLevel=0.15, minDistance=25, mask=mask)

trail_layer = np.zeros_like(first_frame)
frame_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_counter += 1
    current_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if points is not None and len(points) > 0:
        new_pts, status, err = cv2.calcOpticalFlowPyrLK(
            prev_gray, current_gray, points, None, 
            winSize=(25, 25), maxLevel=3
        )

        valid_new = new_pts[status == 1]
        valid_old = points[status == 1]

        tracked_points = []
        for new, old in zip(valid_new, valid_old):
            x1, y1 = new.ravel()
            x0, y0 = old.ravel()

            distance = np.hypot(x1 - x0, y1 - y0)

            if 1.0 < distance < 25.0:
                trail_layer = cv2.line(trail_layer, (int(x1), int(y1)), (int(x0), int(y0)), (0, 255, 0), 2)
                frame = cv2.circle(frame, (int(x1), int(y1)), 4, (0, 0, 255), -1)
                tracked_points.append(new)

        if len(tracked_points) > 0:
            points = np.array(tracked_points).reshape(-1, 1, 2)
        else:
            points = None

    trail_layer = (trail_layer * 0.90).astype(np.uint8)
    combined_view = cv2.add(frame, trail_layer)

    if frame_counter % 30 == 0 or points is None or len(points) < 10:
        points = cv2.goodFeaturesToTrack(current_gray, maxCorners=80, qualityLevel=0.15, minDistance=25, mask=mask)

    prev_gray = current_gray.copy()

    cv2.imshow("Accurate Vehicle Tracker", combined_view)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()