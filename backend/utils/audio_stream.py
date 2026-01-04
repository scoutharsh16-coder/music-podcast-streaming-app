import os
from flask import request, Response

def stream_audio(file_path):
    range_header = request.headers.get("Range", None)
    file_size = os.path.getsize(file_path)

    if range_header:
        byte1, byte2 = 0, None
        match = range_header.replace("bytes=", "").split("-")

        byte1 = int(match[0])
        if match[1]:
            byte2 = int(match[1])

        chunk_size = 1024 * 1024
        byte2 = min(byte1 + chunk_size, file_size - 1)

        length = byte2 - byte1 + 1

        with open(file_path, "rb") as f:
            f.seek(byte1)
            data = f.read(length)

        response = Response(
            data,
            206,
            mimetype="audio/mpeg",
            content_type="audio/mpeg",
            direct_passthrough=True
        )

        response.headers.add(
            "Content-Range",
            f"bytes {byte1}-{byte2}/{file_size}"
        )
        response.headers.add("Accept-Ranges", "bytes")
        response.headers.add("Content-Length", str(length))
        return response

    # fallback (full file)
    with open(file_path, "rb") as f:
        data = f.read()

    return Response(data, mimetype="audio/mpeg")
