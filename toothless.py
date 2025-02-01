import os, pathlib

def get_wallpaper_path() -> str | None:
    images = os.listdir("Wallpaper")
    if(len(images) == 0):
        return None
    return "Wallpaper\\" + images[0]

def main():
    base_path = pathlib.Path().resolve().__str__() + "\\"
    wallpaper_path = base_path + get_wallpaper_path()
    print(wallpaper_path)

if __name__ == "__main__":
    main()