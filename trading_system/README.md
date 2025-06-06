# 📊 TRADING_SYSTEM

A robust real-time trading backend system built with **Django** and **WebSockets**. This project enables users to **manage trade records via a REST API** and **monitor live stock price spikes** using a WebSocket client. 

---

## 🔧 Features

### REST API (Django + DRF)

- **Add Trade**: Create trade entries (ticker, price, quantity, side, timestamp)
- **Fetch Trades**: Retrieve trades with optional filters (by ticker or date range)

### ⚡ Real-Time WebSocket Monitoring

- Connects to a simulated WebSocket stock feed
- Tracks price changes within a 1-minute sliding window
- Triggers alerts if a stock spikes >2% within a minute

---

## 📁 Project Structure

```
TRADING_SYSTEM/
├── trading_system/               # Django project
│   ├── trades/                # Django app for trade operations
│   ├── manage.py
│   └── ...
├── websocket_simulator/       # WebSocket simulation (mock server + client)
│   ├── server.py              # Mock server to simulate stock data
│   └── client.py              # Client that listens and triggers alerts
└── requirements.txt
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ajeyajaz/TRADING_SYSTEM.git
cd TRADING_SYSTEM
```

---

## 🖥️ Part 1: Django REST API for Trades

### 📦 Setup

1. Copy the environment example file and update your database credentials:

```bash
cp .env.example .env
```

2. Edit `.env` with your PostgreSQL settings:

```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```


```bash
cd trading_api
pip install -r requirements.txt
```

### ⚙️ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### ▶️ Start Server

```bash
python manage.py runserver
```

---

## 🔗 API Endpoints

### ➕ Add Trade

```
POST /api/trades/
```

**Request Body (JSON):**
```json
{
  "ticker": "AAPL",
  "price": 170.25,
  "quantity": 10,
  "side": "buy",
  "timestamp": "2025-06-06T20:00:00Z"
}
```

### 📥 Fetch Trades

```
GET /api/trades/
```

**Query Parameters (optional):**

- `ticker=AAPL`
- `start_date=2025-06-01`
- `end_date=2025-06-06`

**Example:**

```
GET /api/trades/?ticker=AAPL&start_date=2025-06-01&end_date=2025-06-06
```

---

## ⚡ Part 2: Real-Time WebSocket Price Alerts

### 🧪 Install Dependencies

```bash
cd websocket_simulator
pip install -r ../requirements.txt
```

### 🔌 Start WebSocket Server

```bash
python server.py
```

### 🎯 Start WebSocket Client

```bash
python client.py
```

### 🔔 Example Alert Output

```bash
📈 Price Spike Alert: TICKER1 increased by 2.4% in 1 minute!
```

---

## 📈 Technologies Used

- **Python 3.11**
- **Django 4+**
- **Django REST Framework**
- **WebSockets (websockets library)**
- **asyncio**
- **PostgreSQL**

---




