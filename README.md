# Task Management Apps
Task Management App adalah aplikasi berbasis web yang dirancang untuk membantu pengguna mengelola produktivitas harian mereka secara efisien. Proyek ini berfokus pada pengalaman pengguna yang bersih (Clean UI) dan alur kerja yang intuitif dalam mengelola daftar tugas (To-Do List). Aplikasi ini memisahkan logika Frontend yang reaktif dengan Backend API yang aman dan skalabel.

# ✨ Fitur Utama
- Create, Read, Update, Delete (CRUD): Kontrol penuh atas tugas yang dibuat.
- Task Status Tracking: Menandai tugas yang sudah selesai atau masih berjalan.
- Filter: Memudahkan pencarian tugas berdasarkan kriteria tertentu.
- Responsive Design: Tampilan yang optimal baik di perangkat desktop maupun mobile.
- Interactive UI: Feedback visual saat menambah atau menghapus tugas.

# 🧩 Technology Stack Notice
**Backend Technology Stack**

- Flask (Python Web Framework) digunakan untuk:
  - Membangun RESTful API
  - Menangani routing endpoint (GET, POST, PUT, DELETE)
  - Mengelola request dan response dari frontend
  - Mengatur logika bisnis aplikasi task management
- JWT (JSON Web Token) Authentication digunakan untuk:
  - Mengamankan endpoint backend
  - Mengelola sesi login tanpa menyimpan session di server (stateless)
  - Mengirim identitas pengguna secara aman melalui HTTP header
- Database (PostgreSQL) digunakan untuk menyimpan:
  - Data task
  - Status task
  - Informasi user

**Frontend Technology Stack**

- Vue.js yang bertanggung jawab untuk:
  - Menampilkan data task secara dinamis
  - Menangani input pengguna
  - Berkomunikasi dengan backend melalui REST API
  - Mengelola state aplikasi
- Tailwind CSS digunakan untuk membangun UI yang:
  - Responsif
  - Konsisten
  - Modern
  - Mudah dikustomisasi

# 🔄 System Workflow
1. User berinteraksi dengan UI (Frontend – Vue.js)
2. Frontend mengirim request ke Backend (Flask)
3. Request diamankan menggunakan JWT
4. Backend memproses data dan mengakses database
5. Response dikembalikan ke frontend
6. UI diperbarui secara real-time

# 📋 Prasyarat Minimum
- Git – untuk clone repository
- Python 3.8+ – untuk menjalankan backend Flask
- pip – Python package manager
- Node.js v16+ – untuk frontend Vue.js
- npm – package manager frontend
- Flask – backend web framework
- Flask-JWT-Extended – autentikasi berbasis JWT
- Vue.js – frontend framework
- Tailwind CSS – styling frontend
- PostgreSQL – database manajemen

# 🚀 Instalasi & Penggunaan
Ikuti langkah-langkah berikut untuk menjalankan proyek ini di lokal Anda:

**1. Clone Repositori**
```python
git clone https://github.com/yongkytristan/Task_Management_Apps.git
```

**2. Setup Database PostgreSQL**
```python
CREATE DATABASE task_db;
```

**3. Masuk ke Direktori Proyek**
```python
cd Task_Management_Apps
```

**4. Setup Backend**

Masuk ke direktori backend
```python
cd backend
```
Buat dan aktifkan virtual environment
```python
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Mac/Linux
```
Instal requirements
```python
pip install -r requirements.txt
```
Buka file `config.py` pilih `SQLALCHEMY_DATABASE_URI` lalu ganti dan sesuaikan dengan postgreSQL anda
```python
# Format: postgresql://username:password@localhost/nama_database
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres123@localhost/task_db'
```
Buka file `check_db_connection.py` pilih `DATABASE_URI` lalu sesuaikan seperti `SQLALCHEMY_DATABASE_URI` di `config.py`
```python
# Format: postgresql://username:password@localhost/nama_database
DATABASE_URI = 'postgresql://postgres:postgres123@localhost/task_db'
```
Kembali ke direktori backend lalu jalankan app.py
```python
python app.py
```
Jika sudah muncul `http://127.0.0.1:5000` maka backend siap digunakan

**5. Setup Frontend**
Masuk ke direktori frontend
```python
cd frontend
```
Instal npm yang dibutuhkan
```python
npm install
```
Jalankan lokal server
```python
npm run dev
```
Jika sudah muncul `http://localhost:5173` maka tinggal di klik dan apps siap digunakan

# 🔐 Dummy Testing
Sistem menggunakan login statis untuk demo dengan:
- Username: admin
- Password: admin123

# 📂 Struktur Folder
```text
Task-Management-App/
├── backend/
│   ├── instance/
│   │   └── task.db                  
│   ├── app.py              
|   ├── check_db_connection.py  
│   ├── config.py            
│   ├── models.py            
│   ├── routes.py
│   ├── reset_db_schema.py          
│   └── requirements.txt    
│
├── frontend/               
│   ├── src/
│   │   ├── assets/
│   │   │   └── main.css         
│   │   ├── components/      
│   │   │   ├── Dashboard.vue    
│   │   │   └── Login.vue 
│   │   ├── App.vue          
│   │   └── main.js          
│   ├── index.html
│   ├── jsconfig.json 
│   ├── package.json
│   ├── package-lock.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   └── vite.config.js
│
└── README.md
```

# 📬 Kontak
Jika ada pertanyaan atau ingin diskusi:

📧 Email: tristanyongky@gmail.com

💼 GitHub: https://github.com/yongkytristan

▶️ Demo Video (YouTube): https://youtu.be/WfUaWBknqAQ
