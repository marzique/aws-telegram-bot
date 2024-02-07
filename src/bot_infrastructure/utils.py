def json_to_markdown(json_data):
    markdown = f"# {json_data['title']}\n"
    markdown += f"![Tux, the Linux mascot]({json_data['url']})\n"
    for key, value in json_data["data"].items():
        markdown += f"{key}: {value}\n"
    return markdown
