from PIL import Image

image = Image.open("input_images/sample.jpg")

while True:
    print("\nIMAGE PROCESSOR")
    print("1. Resize Image")
    print("2. Rotate Image")
    print("3. Convert to PNG")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))

        resized = image.resize((width, height))
        resized.save("output_images/resized_image.jpg")

        print("Image resized successfully!")

    elif choice == "2":
        angle = int(input("Enter rotation angle: "))

        rotated = image.rotate(angle)
        rotated.save("output_images/rotated_image.jpg")

        print("Image rotated successfully!")

    elif choice == "3":
        image.save("output_images/converted_image.png")

        print("Image converted to PNG!")

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")