import cv2
import numpy as np

# 全局变量
drawing = False
ix, iy = -1, -1
fx, fy = -1, -1

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, fx, fy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            fx, fy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        fx, fy = x, y

def create_circular_mask(h, w, center=None, radius=None):
    if center is None: # 使用图像中心作为默认中心
        center = (int(w/2), int(h/2))
    if radius is None: # 使用图像对角线的一半作为默认半径
        radius = min(center[0], center[1], w-center[0], h-center[1])

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius
    return mask

def main():
    global ix, iy, fx, fy

    # 读取图像
    image_path = r"E:\Picture\girl.png"  # 替换为你的壁纸文件路径
    image = cv2.imread(image_path)
    clone = image.copy()

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectangle)

    while True:
        temp_image = clone.copy()
        if ix != -1 and fx != -1:
            cv2.rectangle(temp_image, (ix, iy), (fx, fy), (0, 255, 0), 2)
        cv2.imshow('image', temp_image)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):  # 按下 'c' 键确认选择
            break
        elif key == ord('r'):  # 按下 'r' 键重置选择
            clone = image.copy()
            ix, iy, fx, fy = -1, -1, -1, -1

    # 计算选择的矩形区域的中心和半径
    x1, y1 = min(ix, fx), min(iy, fy)
    x2, y2 = max(ix, fx), max(iy, fy)
    center = (int((x1 + x2) / 2), int((y1 + y2) / 2))
    radius = int(min(x2 - x1, y2 - y1) / 2)

    # 创建圆形掩码
    mask = create_circular_mask(image.shape[0], image.shape[1], center, radius)
    masked_image = np.zeros_like(image)
    masked_image[mask] = image[mask]

    # 保存结果
    output_path = 'profile.png'  # 替换为你想要保存的头像路径
    cv2.imwrite(output_path, masked_image)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
