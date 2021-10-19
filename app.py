import sys # for Command Line Arguments
from jeanCV import skinDetector


imageName = "ISIC_0000245.jpg"

detector = skinDetector(imageName)
detector.find_skin()