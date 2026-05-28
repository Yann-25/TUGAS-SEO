
import os
import requests

# Base URL for unsplash images
# Mapping of filenames to URLs I used
images = {
    # Home
    "hero-bg.jpg": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?q=80&w=1920&auto=format&fit=crop",
    "home-kopi.jpg": "https://images.unsplash.com/photo-1498804103079-a6351b050096?q=80&w=400&auto=format&fit=crop", # Changed
    "home-croissant.jpg": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?q=80&w=400&auto=format&fit=crop",
    "home-tea.jpg": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?q=80&w=400&auto=format&fit=crop",

    # Menu - Coffee
    "menu-kopi-senja.jpg": "https://images.unsplash.com/photo-1498804103079-a6351b050096?q=80&w=400&auto=format&fit=crop", # Changed
    "menu-americano.jpg": "D:\KULIAH\Kuliah Semester 6\SEARCH ENGINE OPTIMIZATION\TUGAS AKHIR ----- UTS ----- UAS\TUGAS AKHIR\images\menu-americano.jpg",
    "menu-macchiato.jpg": "https://images.unsplash.com/photo-1541167760496-1628856ab772?q=80&w=400&auto=format&fit=crop",

    # Menu - Non Coffee
    "menu-matcha.jpg": "https://images.unsplash.com/photo-1515823064-d6e0c04616a7?q=80&w=400&auto=format&fit=crop",
    "menu-chocolate.jpg": "https://images.unsplash.com/photo-1511920170033-f8396924c348?q=80&w=400&auto=format&fit=crop",
    "menu-lychee.jpg": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?q=80&w=400&auto=format&fit=crop",

    # Menu - Snacks
    "menu-croissant.jpg": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?q=80&w=400&auto=format&fit=crop",
    "menu-pisang.jpg": "https://images.unsplash.com/photo-1604382355076-af4b0eb60143?q=80&w=400&auto=format&fit=crop", # Changed
    "menu-platter.jpg": "https://images.unsplash.com/photo-1541592106381-b31e9674c96b?q=80&w=400&auto=format&fit=crop", # Changed

    # Promo
    "promo-sunset.jpg": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?q=80&w=400&auto=format&fit=crop",
    "promo-wfh.jpg": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?q=80&w=400&auto=format&fit=crop", # Changed
    "promo-student.jpg": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?q=80&w=400&auto=format&fit=crop",

    # About
    "about-hero.jpg": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?q=80&w=600&auto=format&fit=crop"
}

output_dir = "images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename, url in images.items():
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(os.path.join(output_dir, filename), 'wb') as f:
                f.write(response.content)
            print(f"Saved {filename}")
        else:
            print(f"Failed to download {filename}: Status {response.status_code}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

print("Download complete.")
