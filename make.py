from PIL import Image

gif_path = "D:/Me/ai project/body.png"
resized_gif_path = "D:/Me/ai project/bod.gif"

with Image.open(gif_path) as img:
    img = img.resize((35, 35))
    img.save(resized_gif_path)

print(f"image saved in : {resized_gif_path}")