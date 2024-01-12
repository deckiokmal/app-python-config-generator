# Network Automation Tools

Alat ini dirancang untuk mengonfigurasi router secara remote menggunakan SSH dan templat konfigurasi.

## Penggunaan

1. Buat dan aktifkan lingkungan virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2. Pasang dependensi yang diperlukan:

    ```bash
    pip install -r requirements.txt
    ```

3. Buat file konfigurasi (`config.yml`), file templat (`config.j2`) di dalam direktori `templates` dan file informasi perangkat (`devices.json`)

4. Jalankan skrip utama untuk mengonfigurasi router:

    ```bash
    python main.py
    ```

## Struktur Directory

- `main/`
  - `main.py`: Skrip utama untuk mengonfigurasi router berdasarkan konfigurasi dan templat yang diberikan.
  - `config_generator.py`: Modul untuk menghasilkan konfigurasi dari templat menggunakan Jinja2.
  - `controller.py`: Modul yang berisi kelas dan fungsi untuk konfigurasi router.
  - `devices.json`: Berkas JSON yang berisi informasi tentang router (alamat IP, username, password, port).
- `templates/`
  - `config.yml`: Berkas konfigurasi YAML yang berisi pengaturan untuk konfigurasi router.
  - `config.j2`: Berkas templat Jinja2 untuk menghasilkan perintah konfigurasi router.
- `venv/` (lingkungan virtual - ini akan dibuat saat aktivasi)
- `requirements.txt`: Berkas yang berisi daftar dependensi dan versi yang diperlukan.

## Dependensi

- paramiko
- jinja2
- PyYAML

