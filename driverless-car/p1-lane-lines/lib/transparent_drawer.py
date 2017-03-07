class Drawer:
    def __init__(self, shape):
        self.image_buffer = np.zeros(image.shape)

    def draw_lines(self, image, lines, color, thickness):
        for line in lines:
            x1, y1, x2, y2 = line
            cv2.line(
                image, (x1, y1), (x2, y2), color, thickness
            )

        return image

    def draw_transparent_lines(self, image, lines, color, thickness):
        self.image_buffer *= 0
        self.draw_lines(lines, color, thickness, self.image_buffer)

        cv2.addWeighted(image, 1.0, self.image_buffer, 1.0, 0, image)

        return image
