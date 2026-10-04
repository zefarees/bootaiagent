import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        wd_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(wd_path, directory))
        valid_target_dir = os.path.commonpath([wd_path, target_dir])

        if valid_target_dir != wd_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        lines = []
        for dir in os.listdir(target_dir):
            item_path = os.path.join(target_dir, dir)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            lines.append(f"- {dir}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(lines)

    except Exception as e:
        return f"Error: {e}"
