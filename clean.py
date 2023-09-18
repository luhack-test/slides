import os
import re
import uuid

def extract_first_heading(markdown_content):
    # Use regular expressions to find the first heading in the Markdown content
    match = re.search(r'^# (.+)$', markdown_content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    else:
        return None

def update_front_matter(markdown_content, new_title):
    # Check if front matter is already present
    if not markdown_content.startswith('---'):
        # Front matter is missing, so add it
        updated_content = f'---\ntitle: "{new_title}"\n---\n{markdown_content}'
    else:
        # Front matter is already present, so update the title within it
        updated_content = re.sub(
            r'^title: .+$',
            f'title: "{new_title}"',
            markdown_content,
            flags=re.MULTILINE
        )

    return updated_content

def update_img_location(markdown_content):
    updated_content = re.sub(r'!\[\]\(img/', '![](../img/', markdown_content)
    return updated_content

def clean_filename(filename):
    # Remove non-alphanumeric characters from the filename
    return re.sub(r'[^a-zA-Z0-9]', '', filename).lower().replace(" ", "_")

def snake_case(old):
    return clean_filename(old)+".md"

def rename_markdown_file(markdown_file, new_title):
    dir = os.path.dirname(markdown_file)
    new_file = snake_case(new_title)

    # Rename the file
    os.rename(markdown_file, os.path.join(dir,new_file))

def generate_snake_case_name_with_uuid():
    # Generate a new UUID
    unique_id = str(uuid.uuid4())
    
    # Remove hyphens and convert to snake_case
    snake_case_name = "idk_" + unique_id.replace("-", "_")
    
    return snake_case_name

def process_markdown_file(markdown_file):
    # Read the Markdown file
    with open(markdown_file, 'r') as file:
        content = file.read()

    # get the new name
    new_title = extract_first_heading(content)
    if new_title == None:
        new_title = generate_snake_case_name_with_uuid()

    # Update the front matter (and add it if missing)
    updated_content = update_front_matter(content, new_title)

    # fix the image names
    updated_content = update_img_location(updated_content)

    # Write the updated content back to the Markdown file
    with open(markdown_file, "w") as file:
        file.write(updated_content)

    # Rename the file to match the new title in snake case
    rename_markdown_file(markdown_file, new_title)

def ensure_index_md(directory):
    directory_name = os.path.basename(directory)
    # Ensure that a directory has an _index.md file with matching front matter title
    index_md_file = os.path.join(directory, '_index.md')
    if not os.path.exists(index_md_file):
        # Create _index.md file with front matter title matching the directory name
        with open(index_md_file, 'w') as file:
            file.write(update_front_matter("", clean_filename(directory_name)))
    else:
        with open(index_md_file, "r") as old_file:
            with open(index_md_file, "w") as new_file:
                new_file.write(update_front_matter(old_file.read(), clean_filename(directory_name)))

def process_folder_recursively(root_folder):
    for root, dirs, files in os.walk(root_folder):
        # Exclude directories and files that start with an underscore
        dirs[:] = [d for d in dirs if not d.startswith('_')]
        files[:] = [f for f in files if not f.startswith('_')]

        # Process each Markdown file
        for file in files:
            if file.endswith("_index.md"):
                ensure_index_md(root)
            elif file.endswith('.md'):
                markdown_file = os.path.join(root, file)
                process_markdown_file(markdown_file)

        # Ensure each directory has an _index.md file
        for dir in dirs:
            if dir != "img":
                directory_path = os.path.join(root, dir)
                ensure_index_md(directory_path)

if __name__ == "__main__":
    # Replace 'your_root_folder' with the path to your root folder
    root_folder = 'content'

    # Process all Markdown files recursively and ensure _index.md files
    process_folder_recursively(root_folder)

