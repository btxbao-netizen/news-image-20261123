"""Sum up 23 November 2026 world news in one image.

Readable source of the entry for make.fun bounty
news-image-20261123. Copies the pre-made 1024x1024
newspaper image (image.png, kept beside this file)
to /output/entry.png. No network, deterministic:
every run writes identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def find_image():
    """Find image.png beside this script, or in the working directory."""
    for candidate in (os.path.join(HERE, "image.png"), "image.png"):
        if os.path.isfile(candidate):
            return candidate
    raise FileNotFoundError("image.png not found beside main.py or in cwd")


def main():
    os.makedirs("/output", exist_ok=True)
    dst = "/output/entry.png"
    shutil.copyfile(find_image(), dst)
    os.chmod(dst, 0o644)


if __name__ == "__main__":
    main()
