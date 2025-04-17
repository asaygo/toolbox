import sys
import os
import zlib
import io

def extract_zlib_stream(zlib_data):
    """
    Extracts the decompressed content from a zlib compressed byte stream.

    Args:
        zlib_data (bytes): The zlib compressed byte stream.

    Returns:
        bytes: The decompressed content as a byte stream.
               Returns None if decompression fails.
    """
    try:
        print("[+] Extract data")
        decompressor = zlib.decompressobj()
        decompressed_data = decompressor.decompress(zlib_data)
        decompressed_data += decompressor.flush()
        return decompressed_data
    except zlib.error as e:
        print(f"Error during zlib decompression: {e}")
        return None

def extract_zlib_stream_from_file(file_path):
    """
    Reads a file, assumes its content is a zlib compressed stream,
    and extracts the decompressed content.

    Args:
        file_path (str): The path to the file containing the zlib compressed data.

    Returns:
        bytes: The decompressed content as a byte stream.
               Returns None if the file cannot be read or decompression fails.
    """
    print(f"[+] Open {file_path}")
    try:
        with open(file_path, 'rb') as f:
            zlib_data = f.read()
        return extract_zlib_stream(zlib_data)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return None

if __name__ == "__main__":
    """
    Checks if the command-line parameter is a file,
    also checking if it's a file.
    """
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        if os.path.isfile(fname):
            b_data = extract_zlib_stream_from_file(fname)
            print(f"[+] Write decompressed data to {fname}.bin")            
            with open(fname + ".bin", "wb") as f:
                f.write(b_data)
        else:
             print(f"{fname} is not a file")
    else:
        print(f"Usage: {sys.argv[0]} <file>")
 