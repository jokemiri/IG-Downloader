import instaloader
import tkinter as tk
from tkinter import messagebox
from tqdm import tqdm

# Initialize Instaloader
L = instaloader.Instaloader()

# Define function to download Instagram post
def download_post():
    post_url = post_url_entry.get()
    try:
        post = instaloader.Post.from_shortcode(L.context, post_url.split("/")[-2])
        with tqdm(total=post.mediacount, desc="Downloading post...") as pbar:
            L.download_post(post, target="instagram_downloads", progress_callback=lambda d: pbar.update(1))
        messagebox.showinfo("Download Complete", "The post has been downloaded successfully.")
    except:
        messagebox.showerror("Download Error", "An error occurred while downloading the post. Please check the URL and try again.")

# Create GUI window
window = tk.Tk()
window.title("Instagram Post Downloader")

# Create post URL label and entry box
post_url_label = tk.Label(window, text="Instagram Post URL:")
post_url_label.pack()
post_url_entry = tk.Entry(window, width=50)
post_url_entry.pack()

# Create download button
download_button = tk.Button(window, text="Download", command=download_post)
download_button.pack()

# Run GUI window
window.mainloop()
