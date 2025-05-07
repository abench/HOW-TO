import cv2

# List of camera resolutions
resolutions = [
    (640, 480), (800, 600), (1024, 768), (1280, 720),
    (1280, 1024), (1600, 1200), (1920, 1080), (2560, 1440), (3840, 2160), (5120, 2880)
]

cap = cv2.VideoCapture(0)

supported_resolutions = []

for width, height in resolutions:
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    if int(actual_width) == width and int(actual_height) == height:
        supported_resolutions.append((width, height))

cap.release()

print("Supported camera resolutions:")
for res in supported_resolutions:
    print(f"{res[0]}x{res[1]}")