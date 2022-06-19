"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and newColor.
You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels
(also with the same color), and so on. Replace the color of all the aforementioned pixels with newColor.
Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected
by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
"""


def flood_fill(image: list[list[int]], sr: int, sc: int, new_color: int) -> list[list[int]]:
    rows = len(image)
    cols = len(image[0])
    color = image[sr][sc]  # changes will occur on this pixel only

    def mark_current_pixel(row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols:
            return

        # only change the color if the pixel is of the source color, return if it's new color
        if image[row][col] == new_color or image[row][col] != color:
            return

        image[row][col] = new_color
        mark_current_pixel(row + 1, col)
        mark_current_pixel(row - 1, col)
        mark_current_pixel(row, col + 1)
        mark_current_pixel(row, col - 1)

    mark_current_pixel(sr, sc)
    return image


def flood_fill_2(image: list[list[int]], sr: int, sc: int, new_color: int):
    m = len(image[0])
    n = len(image)
    old_color = image[sr][sc]
    if old_color == new_color:
        return image

    image[sr][sc] = new_color
    if sr > 0 and old_color == image[sr - 1][sc]:
        flood_fill_2(image, sr - 1, sc, new_color)

    if sr < n - 1 and old_color == image[sr + 1][sc]:
        flood_fill_2(image, sr + 1, sc, new_color)

    if sc > 0 and old_color == image[sr][sc - 1]:
        flood_fill_2(image, sr, sc - 1, new_color)

    if sc < m - 1 and old_color == image[sr][sc + 1]:
        flood_fill_2(image, sr, sc + 1, new_color)
    return image

    
def main():
    a = flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
    print(a)

    b = flood_fill([[0, 0, 0], [0, 0, 0]], 0, 0, 2)
    print(b)


if __name__ == '__main__':
    main()
