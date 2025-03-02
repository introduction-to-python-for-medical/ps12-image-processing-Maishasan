
from image_utils import load_image, edge_detection
from skimage.filters import median
from skimage.morphology import ball
from PIL import Image

lena = load_image('lena.jpg')
clean = median(lena, ball(3))
l_edge = edge_detection(clean)
binary = l_edge > 100
edge_image = Image.fromarray(np.uint8(binary * 255))
edge_image.save('Lenanew.png')
