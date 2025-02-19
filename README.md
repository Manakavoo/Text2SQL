# **Text2SQL Generator**  
![License](https://img.shields.io/badge/license-MIT-blue.svg) 

## **Overview**  
The **Text2SQL Generator** is a Streamlit-based web application that converts natural language queries into SQL statements using an AI model. It allows users to execute queries on a connected database and retrieve results efficiently.  

## **Features**  
- Convert natural language queries into SQL  
- Execute generated SQL queries on SQLite, PostgreSQL, or MySQL  
- View and test database schemas dynamically  
- Secure database connections with `.env` file  
- Built with **Streamlit**, **Google Gemini AI**, and **PostgreSQL/MySQL/SQLite**  

## **Installation**  

### **Step 1: Clone the Repository**  
```sh
git clone https://github.com/yourusername/text2sql.git  
cd text2sql
```

### **Step 2: Create a Virtual Environment**  
```sh
python -m venv venv  
source venv/bin/activate  # For macOS/Linux  
venv\Scripts\activate  # For Windows
```

### **Step 3: Install Dependencies**  
```sh
pip install -r requirements.txt  
```

### **Step 4: Set Up Environment Variables**  
Create a **.env** file in the project root and add:  
```env
GOOGLE_PRO_API_KEY=your_api_key
```

### **Step 5: Run the Application**  
```sh
streamlit run main.py  
```

---

## **API Endpoints**  

| Method | Endpoint       | Description |
|--------|--------------|-------------|
| `POST` | `/generate_sql` | Converts text input into an SQL query |
| `POST` | `/execute_query` | Runs the generated SQL query on the database |
| `GET`  | `/get_schema`   | Retrieves the database schema |

---

## **Usage**  
1. **Enter a natural language question** (e.g., *Show all students*).  
2. Click **"Generate SQL"** to create an SQL query.  
3. Click **"Execute"** to run the query on the database.  
4. View the results in a table format.  

---

## **Tech Stack**  
- **Frontend**: Streamlit, HTML, Bootstrap  
- **Backend**: Python (FastAPI)
- **Database supports**: PostgreSQL/MySQL/SQLite  
- **AI Model**: Google Gemini AI  

---

## **Contributing**  
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Added new feature"`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Open a Pull Request  

---

## **License**  
This project is licensed under the **MIT License**.  

---

## **Contact**  
- **Author**: Manakavoo Siva Balaji
- **Email**: sivabalajimanakavoo@gmail.com 
- **GitHub**: [Manakavoo](https://github.com/Manakavoo)  

---
