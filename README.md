# Brute-Force Zip Password Cracker (Educational)

This repository is created **for educational purposes only**.  
Its main goal is to practice and demonstrate Python concepts through a brute-force attack simulation on password-protected ZIP files.  
This project was built as a **self-study exercise** to strengthen knowledge in the field of **Information Security (An toàn thông tin)**.  
Its aim is to practice and understand fundamental attack methods Brute-force) in a controlled and legal environment.  

## Purpose
- Understand **file handling** with `pyzipper`
- Implement **random password generation**
- Learn **multiprocessing** to speed up brute-force attempts
- Apply **error handling** & **performance logging**
- **Practical training** on how Brute-force concepts relate to **Information Security**

## Disclaimer
This project is strictly for **learning and research purposes**.  
Do not use it for unauthorized access or any illegal activity.  


---

## Project Structure
- `create_zip.py` → Create a ZIP file with a random numeric password.
- `main.py` → Try to crack the password using brute-force with multiprocessing.
- `raw.txt` → Sample file used for compression.
  

---

## Installation & Usage

Clone repository
  ```bash
    git clone https://github.com/Khanshs/encrypted-archiver.git
    cd encrypted-archiver

  ```

Install dependencies:
   ```bash

    pip install pyzipper

   ```

Runing:
Generate a file named archive_withpass.zip protected with a password for testing:
   ```bash
      python create_zip.py
   ```
Run brute-force attack on the encrypted zip:

  ```bash
      python main.py
   ```
## Demo 
```bash
    $ python main.py
    [~] Starting brute-force attack on file: archive_withpass.zip
    [  5.01s]
    [ 10.04s]
    [ 15.07s]
    [*] Found password: 123456 in 18.42s
    [*] Speed: 7231.27 tries/sec

```
## Notes
- This project is **for educational purposes only**, to practice Information Security concepts.  
- Works best with **6-digit numeric passwords**.  
- Can also brute-force shorter passwords (≤ 4 characters) with mixed uppercase/lowercase letters.  
- For longer & complex passwords (symbols, mixed sets), runtime becomes impractically slow.  
- Extracted files are saved into the `extracted/` folder.
  
## Future Improvements
- Support variable password lengths beyond fixed `repeat=6`.
- Add custom wordlist support (dictionary attack).
- Optimize performance with smarter search strategies.
- Implement progress bar and estimated time remaining (ETA).
- Compare brute-force speed across different character sets.
- Build GUI version for easier interaction.
