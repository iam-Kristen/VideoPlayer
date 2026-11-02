import json
import os


def generate_json():
    image_folder = "Rex/icon"
    json_data = {
        "name": "Rex_Logo",
        "description": "Rex icon set",
        "icons": [],
    }

    for filename in sorted(os.listdir(image_folder)):
        if filename.lower().endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            raw_url = f"https://raw.githubusercontent.com/{os.environ['GITHUB_REPOSITORY']}/main/{image_path}"
            icon_name = os.path.splitext(filename)[0]
            icon_data = {"name": icon_name, "url": raw_url}
            json_data["icons"].append(icon_data)

    output_path = os.path.join(os.getcwd(), "Rex", "Logo.json")

    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

    github_state = os.environ.get("GITHUB_STATE")
    if github_state:
        with open(github_state, "a", encoding="utf-8") as state_file:
            state_file.write(f"ICONS_JSON_PATH={output_path}\n")


if __name__ == "__main__":
    generate_json()
