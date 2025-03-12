



# import cv2
# import numpy as np

# # Video properties
# width, height = 720, 1280
# fps = 30
# duration = 6  # seconds

# # Define text properties
# font = cv2.FONT_HERSHEY_SIMPLEX
# font_scale = 3
# font_thickness = 5
# text_color = (255, 255, 255)  # White

# # Create video writer
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# video_path = "munisam_duolarimda.mp4"
# video = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

# # First 3 seconds: "Munisam"
# for _ in range(fps * 3):
#     frame = np.zeros((height, width, 3), dtype=np.uint8)
#     text_size = cv2.getTextSize("Munisam", font, font_scale, font_thickness)[0]
#     text_x = (width - text_size[0]) // 2
#     text_y = (height + text_size[1]) // 2
#     cv2.putText(frame, "Munisam", (text_x, text_y), font, font_scale, text_color, font_thickness, cv2.LINE_AA)
#     video.write(frame)

# # Next 3 seconds: "Seni duolarimda soʻrayman"
# for _ in range(fps * 3):
#     frame = np.zeros((height, width, 3), dtype=np.uint8)
#     text_size = cv2.getTextSize("Seni duolarimda soʻrayman", font, font_scale - 1, font_thickness - 2)[0]
#     text_x = (width - text_size[0]) // 2
#     text_y = (height + text_size[1]) // 2
#     cv2.putText(frame, "Seni duolarimda soʻrayman", (text_x, text_y), font, font_scale - 1, text_color, font_thickness - 2, cv2.LINE_AA)
#     video.write(frame)

# # Release the video writer
# video.release()
# print(f"Video saved as {video_path}")


# import cv2
# print(cv2.__version__)  # Should print OpenCV version
