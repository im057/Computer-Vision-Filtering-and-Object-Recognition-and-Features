import cv2
import numpy as np

from src.convolution import convolution, gaussian_kernel
from src.helpers import get_video_filenames


def main():
    """
    Program entry point.
    :return: None
    """
    training_dataset_directory = "dataset/Training/png/"
    testing_dataset_directory = "dataset/Test/"

    # Blur an image
    blur_image(training_dataset_directory, "001-lighthouse.png")

    # Train the intensity-based template matching model
    intensity_based_template_matching_training(training_dataset_directory)

    # Test the intensity-based template matching model
    intensity_based_template_matching_testing(testing_dataset_directory)


def blur_image(directory, image):
    gauss_kernel = gaussian_kernel(10, 10, 5)
    blur_kernel = np.ones((5, 5)) / 25

    img = cv2.imread(directory + image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    conv_img = convolution(gray, gauss_kernel)

    cv2.imshow("Original image", gray)
    cv2.imshow("Convoluted image", conv_img)
    cv2.waitKey(0)


def intensity_based_template_matching_training(directory):
    images = get_video_filenames(directory)
    print("\nTraining image file names:")
    print(images)


def intensity_based_template_matching_testing(directory):
    images = get_video_filenames(directory)
    print("\nTesting image file names:")
    print(images)


if __name__ == "__main__":
    main()