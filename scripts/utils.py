import requests
import yaml
import os

def generate_yaml_section(permalink: str, title: str, excerpt: str, author: str, caption: str, download_url: str):
	# Tworzymy strukturę YAML jako słownik
	data = {
		"permalink": permalink,
		"title": title,
		"excerpt": excerpt,
		"published": True,
		"author_profile": True,
		"author": author,
		"layout": "single",
		"header": {
			"caption": caption,
			"actions": [
				{
					"label": "Download",
					"url": download_url
				}
			]
		}
	}

	# Konwertujemy słownik na YAML i zwracamy jako tekst
	yaml_text = yaml.dump(data, sort_keys=False)
	return f"---\n{yaml_text}---"

def get_readme(repo_owner: str , repo_name: str, branch: str = "main"):
	url: str = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/README.md"
	response = requests.get(url)
	
	if response.status_code == 200:
		return response.text
	
	print(f"Fail to download {repo_owner/repo_name}/README.md.")
	return None

import requests

def get_release_link(repo_owner: str, repo_name: str, version: str = "latest"):
	url: str = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
	if version != "latest":
		url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/tags/{version}"
	
	response = requests.get(url)
	
	if response.status_code == 200:
		release_info = response.json()
		return release_info.get("html_url")

	print("Fail to get download link to {repo_owner}/{repo_name}/{version}")
	return None

def get_release_notes(repo_owner: str, repo_name: str, version: str = "latest"):
	url: str = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
	if version != "latest":
		url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/tags/{version}"
	
	response = requests.get(url)
	
	if response.status_code == 200:
		latest_release = response.json()
		release_notes = latest_release.get("body")
		return release_notes

	print("Fail to download info of {repo_owner}/{repo_name}/{version}")
	return None

def create_markdown(directory: str, author: str, repo_owner: str, repo_name: str, version: str = "latest"):
	# Pobierz README i notatki z wydania
	readme_content = get_readme(repo_owner, repo_name)
	release_notes = get_release_notes(repo_owner, repo_name)
	release_link = get_release_link(repo_owner, repo_name)
	
	if not readme_content or not release_notes:
		print("Nie udało się pobrać wszystkich wymaganych danych.")
		return

	# Wygeneruj sekcję YAML
	yaml_content = generate_yaml_section(
		permalink=f"/{directory}/{repo_name}",
		title=repo_name.replace("-", " ").title(),
		excerpt="",
		author=author,
		caption=version,
		download_url=release_link
	)

	# Połącz sekcje w jeden markdown
	markdown_content = f"""
	{yaml_content}
	{readme_content}
	{release_notes}
	"""

	# Zapisz do pliku
	output_path = os.path.join(directory, f"{repo_name}.md")
	with open(output_path, "w", encoding="utf-8") as file:
		file.write(markdown_content)

	print(f"Plik markdown został zapisany jako: {output_path}")

# Przykład użycia
create_markdown(
	repo_owner="rakugoteam",
	repo_name="AdvancedText",
	directory=".",  # Podaj katalog docelowy
	author="Jeremi Biernacki"
)
