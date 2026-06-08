full_file_name = input("File name: ").strip()
# split the file name from the last dot (rsplit)and get the extension to print after
extension = full_file_name.rsplit(".", maxsplit=1)[-1].lower()


match extension:
    # cases where it's an image
    case "gif" | "jpg" | "jpeg" | "png":
        # make sure that jpg and jpeg are written the same (i.e. image/jpeg)
        print(f"image/{extension.replace("jpg", "jpeg")}")
    case "pdf" | "zip":
        print(f"application/{extension}")
    case "txt":
        print("text/plain")
    case _:
        # cases with other suffix or none
        print("application/octet-stream")
