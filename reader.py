# use pytesseract to read the text in the screenshot and apprend it to the specified file

# import pytesseract, time
# from PIL import Image
# # from seer import get_file_path

# reads_file_path = "./output/"
# latest_read = ""

# def read_text_from_image(image_path):
#     # read text from image
#     text = pytesseract.image_to_string(Image.open(image_path))
#     return text


# def append_text_to_file(text, file_path):
#     # append text to file
#     global latest_read
#     latest_read = text
#     file_path = reads_file_path + "out.txt"
#     text = "-------\n"+ time.strftime("%H-%M-%S") + "\n-------\n" + text
#     with open(file_path, "a") as file:
#         file.write(text)


# def read_text_from_image_and_append_to_file(image_path, file_path):
#     # read text from image
#     text = read_text_from_image(image_path)
#     # append text to file
#     if text != latest_read:
#         append_text_to_file(text, file_path)
#     else:
#         print("skip")


# # read_text_from_image_and_append_to_file(get_file_path(), reads_file_path)


# # use pytesseract to read the text in the screenshot and apprend it to the specified file

# import pytesseract, time
# from PIL import Image

# reads_file_path = "./output/"
# appended_texts = set()

# def read_text_from_image(image_path):
#     # read text from image
#     text = pytesseract.image_to_string(Image.open(image_path))
#     return text

# def append_text_to_file(text, file_path):
#     # append text to file
#     global appended_texts
#     if text not in appended_texts:
#         appended_texts.add(text)
#         file_path += "out.txt"
#         text = "-------\n"+ time.strftime("%H-%M-%S") + "\n-------\n" + text
#         with open(file_path, "a") as file:
#             file.write(text)
#     else:
#         print("skip")

# def read_text_from_image_and_append_to_file(image_path, file_path):
#     # read text from image
#     text = read_text_from_image(image_path)
#     # append text to file
#     append_text_to_file(text, file_path)

# SEEKER

# use pytesseract to read the text in the screenshot and append it to the specified file

import pytesseract, time
from PIL import Image

reads_file_path = "./output/"
# latest_read = ""
appended_texts = set()

def read_text_from_image(image_path):
    # read text from image
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def append_text_to_file(text, file_path):
    # append text to file
    global appended_texts
    if text not in appended_texts:
        # latest_read = text
        appended_texts.add(text)
        file_path = reads_file_path + "out.txt"
        text = "-------\n"+ time.strftime("%H-%M-%S") + "\n-------\n" + text
        with open(file_path, 'r+') as file:
            original_contents = file.read()
            file.seek(0)
            file.write(text + original_contents)
    else:
        print("SKIP")

def read_text_from_image_and_append_to_file(image_path, file_path):
    # read text from image
    text = read_text_from_image(image_path)
    # append text to file
    append_text_to_file(text, file_path)
