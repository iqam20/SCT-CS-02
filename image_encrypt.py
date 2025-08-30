from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key=50):
    """Encrypts image by adding key value to pixel values."""
    img = Image.open(input_path)
    arr = np.array(img)
    encrypted_arr = (arr + key) % 256
    encrypted_img = Image.fromarray(np.uint8(encrypted_arr))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key=50):
    """Decrypts image by subtracting key value from pixel values."""
    img = Image.open(input_path)
    arr = np.array(img)
    decrypted_arr = (arr - key) % 256
    decrypted_img = Image.fromarray(np.uint8(decrypted_arr))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    print("=== Image Encryption Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").lower()
    input_file = input("Enter input image filename (e.g., sample_input.png): ")
    output_file = input("Enter output image filename (e.g., encrypted.png): ")
    key = int(input("Enter key value (integer): "))

    if choice.startswith("e"):
        encrypt_image(input_file, output_file, key)
    elif choice.startswith("d"):
        decrypt_image(input_file, output_file, key)
    else:
        print("Invalid choice! Please select Encrypt or Decrypt.")
