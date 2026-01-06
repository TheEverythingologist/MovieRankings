from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pathlib import Path
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import os
import re
import warnings


class MoviePoster:
    def __init__(self, letterboxd_url: str):
        self.movie_name = letterboxd_url.split("/")[-2]
        self.save_path = f"data/movie-posters/{self.movie_name}"
        self.save_letterboxd_poster(letterboxd_url)

    def slugify(self, text):
        return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

    def get_letterboxd_poster_url_with_selenium(self, movie_url):
        warnings.filterwarnings("ignore")

        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--log-level=3")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        try:
            driver.get(movie_url)
            time.sleep(2)

            poster = driver.find_element(By.CSS_SELECTOR, "div.film-poster img")

            # Force lazy-load
            driver.execute_script("arguments[0].scrollIntoView(true);", poster)
            time.sleep(1)

            # Try data-srcset first (highest quality)
            data_srcset = poster.get_attribute("data-srcset")
            if data_srcset:
                return data_srcset.split(",")[-1].split()[0]

            # Fallback to data-src
            data_src = poster.get_attribute("data-src")
            if data_src:
                return data_src

            # Last resort (will usually be empty-poster)
            return poster.get_attribute("src")

        finally:
            driver.quit()

    def download_image(self, image_url, filename):
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Image saved as: {filename}")

    def save_letterboxd_poster(self, movie_url, save_dir="."):
        poster_url = self.get_letterboxd_poster_url_with_selenium(movie_url)
        filename_slug = self.slugify(poster_url.split("/")[-1].split(".")[0])
        filename = os.path.join(save_dir, f"{self.save_path}.jpg")
        self.download_image(poster_url, filename)

# Example usage
if __name__ == "__main__":
    movie_url = "https://letterboxd.com/film/the-social-network/"
    dumm = MoviePoster(movie_url)