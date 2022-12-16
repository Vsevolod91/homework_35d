import time

def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""
    start_time = time.time()
    try:
        with open(file, "rb") as f:
            result = f.read()
    except Exception as e:
        print(e)
    else:
        return result
    finally:
        read_time = time.time() - start_time
        print(f"Time required for {file} = {read_time}")

if __name__ == "__main__":
    read_file_timed("all_stocks_5yr.csv")
    read_file_timed("file_not_exist.mp4")