import itertools, string, pyzipper, time
from multiprocessing import Pool, cpu_count




def try_password(finalpass_tuple):
    passwd = ''.join(finalpass_tuple)
    try:
        with pyzipper.AESZipFile(file_zip) as zf:
            zf.setpassword(passwd.encode())
            zf.extractall(path='extracted')
        return passwd
    except RuntimeError:
        return None  # wrong password
    except Exception as e:
        return None

def report_status(start_time):
    elapsed_time = time.perf_counter() - start_time
    print(f"[{elapsed_time:6.2f}s]")


file_zip = 'archive_withpass.zip'   # The zip file to be cracked
listpas = string.digits             # Characters to use in the password (digits only)
                                    # You can change this to string.ascii_lowercase, string.ascii_uppercase, string.ascii_letters, string.hexdigits, string.punctuation, or any custom string of characters
                                    # Example: listpas = string.ascii_lowercase + string.digits  # lowercase letters and digits


if __name__ == "__main__":
    start_time = time.perf_counter()
    last_report = start_time
    print(f"[*] Starting brute-force attack on: '{file_zip}'")
    with Pool(cpu_count()) as pool: # Create a pool of worker processes = cpu_count()
    
        # itertools.product(listpas, repeat=6) generates all possible combinations of passwords
        # pool.imap_unordered() will distribute these combinations to the worker processes
        # Allowing them to process tasks in parallel

        for result in pool.imap_unordered(try_password, itertools.product(listpas, repeat=6)):
            now = time.perf_counter()
            if now - last_report >= 5:      # report every 5 seconds
                report_status(start_time)
                last_report = now           # Update last_report time

            if result:
                elapsed_time = time.perf_counter() - start_time
                speed = int(result) / elapsed_time 
                print(f"[*] Found password: {result} in {elapsed_time:.2f}s")
                print(f"[*] Speed: {speed:.2f} tries/sec")

                pool.terminate()



