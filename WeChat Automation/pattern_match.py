import cv2
import numpy as np
from matplotlib import pyplot as plt


target_img = cv2.imread("view.png")
target_img = cv2.cvtColor(target_img, cv2.COLOR_BGR2RGB)

template_img = cv2.imread("send_btn.png")
template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2RGB)

h, w, depth = template_img.shape


res = cv2.matchTemplate(target_img, template_img, method=cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(target_img, top_left, bottom_right, 255, 2)
plt.subplot(121),plt.imshow(res,cmap = "gray")
plt.title("Matching Result"), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(target_img,cmap = "gray")
plt.title("Detected Point"), plt.xticks([]), plt.yticks([])
plt.suptitle("cv2.TM_CCOEFF_NORMED")
plt.show()
