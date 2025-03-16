# eBay Store Manager - Dashboard Application (v1.1)

## Overview
This is Version 1.1 of the eBay Store Manager dashboard application. This update introduces enhanced order metrics tracking and improved deployment readiness using the Waitress WSGI server.

---

## Key Features
- **New:** Now displays total orders for the past **30**, **60**, and **90** days.
- **New:** Integrated **Waitress** WSGI server for improved performance and production readiness.
- Displays a detailed table with:
  - **Order ID**
  - **Total Amount**
  - **Order Creation Date**
  - **Delivery Cost** (if available)
- Uses a **dark, neon-inspired theme** for the visual design.

---

## Project Structure
```
.
├── app.py
├── templates
│   └── index.html
├── static
│   └── styles.css
├── .env
├── requirements.txt
└── previous_versions
    └── version 1.1
```

---

## Environment Variables (.env)
The following environment variable is required for the application to connect to the eBay API:
```
EBAY_PROD_TOKEN=your_ebay_production_token_here
```

---

## Installation
1. **Clone the repository:**  
```bash
$ git clone <repo_url>
$ cd <project_directory>
```

2. **Create a virtual environment and install dependencies:**  
```bash
$ python -m venv venv
$ source venv/bin/activate  # For Windows: venv\Scripts\activate
$ pip install -r requirements.txt
```

3. **Add the `.env` file:**  
Create a `.env` file in the project root and add the required `EBAY_PROD_TOKEN` as described above.

4. **Run the application:**  
```bash
$ python app.py
```

5. **Access the dashboard:**  
Visit [http://localhost:8000](http://localhost:8000) in your web browser.

---

## Known Issues / Future Enhancements
✅ Current version displays order metrics but lacks additional insights.  
✅ Needs improved error handling for failed API requests.  
✅ Future enhancement: Implement dynamic date range selectors.  
✅ Future enhancement: Introduce caching for improved performance.  
✅ Future enhancement: Add functionality to retrieve updated eBay tokens directly within the app.

---

## Design Elements
- The CSS styling creates a **futuristic, neon-inspired interface** that complements the data-driven theme.
- Font used: **Orbitron** for a sleek, modern look.

---

## License
This project is licensed under the MIT License.

```
MIT License
...
```

---

## Author
**John Szpyrka**
- Email: john.l.szpyrka@outlook.com
- GitHub: [IdealRobot](https://github.com/IdealRobot)

---

## Contact
For issues or feature requests, please submit an issue on the GitHub repository.

