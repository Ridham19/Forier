import tkinter as tk
from PIL import Image, ImageTk

# Function to close the window


def main():
    def close_window():
        root.destroy()

    # Create the main window

    root = tk.Tk()
    root.title("Original function and its Fourier series approximation")
    root.geometry("800x800+300+120")
    root.attributes('-fullscreen', False)

    # Load the background image
    image = Image.open("output.jpeg")
    bg_image = ImageTk.PhotoImage(image)

    # Create a label to hold the background image
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # Add a label on top of the background
    label = tk.Label(root, text="Your Output", bg="white", font=("Helvetica", 28))
    label.pack(pady=20)

    # close button
    close_button = tk.Button(root, text="Close❌", command=close_window, font=("Helvetica", 14))
    close_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()

