import shutil

def generate_dub(input_path, lang):
    output_path = "static/downloads/output.mp3"
    shutil.copy(input_path, output_path)
    return output_path

