import re
import tkinter as tk
import random

# Load poems from the text file
def load_poems(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        
        # Use a regular expression to split the text by numbers followed by a line break
        poems = re.split(r'\n\d+\n', text)[1:]  
        
        # Strip any leading or trailing whitespace from each poem
        poems = [poem.strip() for poem in poems]
        
    return poems

# Get a random poem
def get_random_poem(poems):
    return random.choice(poems)

def create_overlay(text):
    # Create a Tkinter window
    root = tk.Tk()
    
    # Set window size 
    banner_width = 300
    banner_height = 700  
    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()
    x_position = 0  # Flush against the left side
    y_position = (screen_height - banner_height) // 2  # Centered vertically

    root.geometry(f"{banner_width}x{banner_height}+{x_position}+{y_position}")
    root.configure(bg="black")

    # Remove window decorations for a clean appearance
    root.overrideredirect(True)
    
    # Make window semi-transparent
    root.attributes("-alpha", 0.7)
    
    # Allow other windows to overlap this window
    root.attributes("-topmost", False)

    # Create a frame to contain the text
    text_frame = tk.Frame(root, bg="black")
    text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Create a text widget to display the poem
    text_widget = tk.Text(
        text_frame,
        font=("Helvetica", 18), 
        fg="white",
        bg="black",
        wrap=tk.WORD,
        borderwidth=0,
        highlightthickness=0
    )
    text_widget.insert(tk.END, text)
    text_widget.config(state=tk.DISABLED)  # Make text read-only
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Close the window when pressing Escape
    root.bind("<Escape>", lambda e: root.destroy())

    # Start the main loop
    root.mainloop()

# Main function
def main():
    poems = load_poems('/Users/helenemartin/DailyBookOverlay/book.txt')  
    poem = get_random_poem(poems)
    create_overlay(poem)

if __name__ == "__main__":
    main()