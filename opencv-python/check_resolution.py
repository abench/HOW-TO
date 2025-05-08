import cv2

# Codec formats
fourcc_codes = {
    'MJPG': cv2.VideoWriter_fourcc(*'MJPG'),
    'YUYV': cv2.VideoWriter_fourcc(*'YUYV'),
    'H264': cv2.VideoWriter_fourcc(*'H264'),
}

# Typical resolutions
rresolutions = [
    (640, 480), (800, 600), (1024, 768), (1280, 720),
    (1280, 1024), (1600, 1200), (1920, 1080), (2560, 1440), (3840, 2160), (5120, 2880)
]

# FPS
fps_list = [15, 30, 60]

camera_index = 0

results = []

for fmt_name, fourcc in fourcc_codes.items():
    for width, height in resolutions:
        for fps in fps_list:
            cap = cv2.VideoCapture(camera_index)
            cap.set(cv2.CAP_PROP_FOURCC, fourcc)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
            cap.set(cv2.CAP_PROP_FPS, fps)

            actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            actual_fps = cap.get(cv2.CAP_PROP_FPS)

            if int(actual_width) == width and int(actual_height) == height:
                results.append((fmt_name, width, height, actual_fps))

            cap.release()

# Infromation output  
print("Supported formats:")
for fmt_name, width, height, fps in results:
    print(f"{fmt_name}: {width}x{height} @ {fps:.2f} FPS")