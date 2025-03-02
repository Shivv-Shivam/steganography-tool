import cv2
import numpy as np
from stegano import lsb

def hide_message(image_path, message, output_path):
    # Hide the message in the image
    secret_image = lsb.hide(image_path, message)
    
    # Save the new image
    secret_image.save(output_path)
    print(f"Message hidden in {output_path}")

def reveal_message(image_path):
    # Reveal the hidden message from the image
    hidden_message = lsb.reveal(image_path)
    return hidden_message

if __name__ == "__main__":
    # Example usage
    choice = input("Do you want to (1) hide a message or (2) reveal a message? ")

    if choice == '1':
        image_path = input("Enter the path of the image: ")
        message = input("Enter the message to hide: ")
        output_path = input("Enter the output image path: ")
        hide_message(image_path, message, output_path)
    elif choice == '2':
        image_path = input("Enter the path of the image to reveal the message: ")
        message = reveal_message(image_path)
        if message:
            print(f"Hidden message: {message}")
        else:
            print("No hidden message found.")
    else:
        print("Invalid choice.")
