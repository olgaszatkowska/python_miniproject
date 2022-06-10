from PIL import Image

from src.utils import (
    parse_book_as_list,
    create_book_info,
    get_words_per_paragraph,
    generate_plot,
    download_picture,
    crop_image,
    rotate_image,
    compose_images,
    create_word_document,
    create_chapter_data,
    remove_files,
)


BOOK_URL = "https://www.gutenberg.org/cache/epub/68253/pg68253.txt"
BOOK_IMAGE_URL = "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1370363542i/12133302._UY630_SR1200,630_.jpg"
BOOK_LOGO_URL = "https://upload.wikimedia.org/wikipedia/commons/f/f4/Amazing_Stories_interior_title.png"
GRAPH_PATH = "graph.png"
WORD_DOC_PATH = "book_summary.docx"
AUTHOR = "Olga Szatkowska"


def main():
    content = parse_book_as_list(BOOK_URL)
    book_info = create_book_info(content)

    df = get_words_per_paragraph(book_info.first_chapter)
    generate_plot(df, GRAPH_PATH)

    picture_path = download_picture(BOOK_IMAGE_URL)
    image = Image.open(picture_path)
    width, height = image.size
    cropped_picture_path = crop_image(
        picture_path, (width / 3, 0, width * 2 / 3, height)
    )

    logo_path = download_picture(BOOK_LOGO_URL)
    rotated_logo_path = rotate_image(logo_path, 5)

    compose_images(rotated_logo_path, cropped_picture_path)
    create_word_document(
        WORD_DOC_PATH,
        AUTHOR,
        book_info.title,
        cropped_picture_path,
        book_info,
        GRAPH_PATH,
        create_chapter_data(df),
    )

    remove_files(cropped_picture_path, rotated_logo_path, logo_path, picture_path)


if __name__ == "__main__":
    main()
