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
        options.add_argument("--headless")  # Run headless
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--log-level=3")  # 0 = INFO, 3 = FATAL

        # Set up Chrome service properly
        service = Service(
            executable_path="chromedriver.exe",
            log_path=Path.cwd() / "NUL"  # For Windows; use "/dev/null" on Mac/Linux
            )
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        try:
            driver.get(movie_url)
            time.sleep(3)  # Wait for JavaScript to load

            # Find the image inside the film-poster container
            poster_img = driver.find_element(By.CSS_SELECTOR, "div.film-poster img")

            # Prefer srcset for higher res if available
            poster_url = poster_img.get_attribute("srcset")
            if poster_url:
                return poster_url.strip().split()[-2]  # Get the highest-res image
            else:
                return poster_img.get_attribute("src")

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
movie_url = "https://letterboxd.com/film/the-social-network/"
dumm = MoviePoster(movie_url)