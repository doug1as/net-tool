# 🧰 Net-Tool

**Net-Tool** is a Django-based web application that serves as a network automation dashboard, with a focus on managing VLAN assignments and interface modes (access/trunk) on Cisco Nexus switches.

Inspired by some daily needs, this project provides a clean interface, user-based access controls, and support for granular VLAN changes.

---

## 🚀 Features

- 🔐 **User Authentication** (login/signup/logout)
- 🎛 **VLAN Change Request System**
- 🎚 **Interface Mode Management** (Access / Trunk)
- 🧠 **Role-based Access Control (RBAC)** with Django Groups & Permissions
- 📓 **Audit Logging** for every configuration change
- 🔍 **Searchable Switch & Port Inventory**
- ☁️ Designed for future API integrations (e.g., NX-API, Ansible)

---

## 🧱 Tech Stack

- **Backend**: Python 3.13, Django 5.2.5
- **Frontend**: HTML, CSS (custom styles)
- **Database**: SQLite (dev) — can migrate to PostgreSQL/MySQL
- **Authentication**: Django auth system with Groups & Permissions
- **Version Control**: Git + GitHub

---

## 📦 Setup

### Requirements

- Python 3.13+
- pip
- Virtualenv (recommended)

### Installation

```bash
# Clone the repo
git clone git@github.com:doug1as/net-tool.git
cd net-tool

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run initial migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Start development server
python manage.py runserver

### 📫 Contact
Maintainer: @doug1as
Email: doug1as@outlook.com