def booklet_layout(content_pages):
    empty = 4 - content_pages % 4
    booklet = content_pages + empty

    return booklet, empty