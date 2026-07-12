"""
Simple LSB Steganography Tool
Hides / reveals text messages inside PNG images using least-significant-bit encoding.
"""

import os
from stegano import lsb


def hide_message(image_path: str, message: str, output_path: str) -> None:
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    if not image_path.lower().endswith(".png"):
        print("Warning: LSB steganography needs a lossless format. "
              "JPEG compression will destroy hidden data — use PNG.")

    if not output_path.lower().endswith(".png"):
        output_path += ".png"

    try:
        secret_image = lsb.hide(image_path, message)
        secret_image.save(output_path)
        print(f"Message hidden successfully -> {output_path}")
    except Exception as e:
        print(f"Failed to hide message: {e}")


def reveal_message(image_path: str) -> str | None:
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    try:
        return lsb.reveal(image_path)
    except Exception as e:
        print(f"Failed to reveal message: {e}")
        return None


def main():
    choice = input("Do you want to (1) hide a message or (2) reveal a message? ").strip()

    try:
        if choice == "1":
            image_path = input("Enter the path of the image (PNG recommended): ").strip()
            message = input("Enter the message to hide: ").strip()
            output_path = input("Enter the output image path: ").strip()
            hide_message(image_path, message, output_path)

        elif choice == "2":
            image_path = input("Enter the path of the image to reveal the message from: ").strip()
            message = reveal_message(image_path)
            if message:
                print(f"Hidden message: {message}")
            else:
                print("No hidden message found.")

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
