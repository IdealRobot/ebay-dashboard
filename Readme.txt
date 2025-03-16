# eBay Store Manager - Dashboard Application (v1.0)

## Overview
This is the MVP for the eBay Store Manager dashboard application. The application is designed to help manage eBay store metrics, integrating with the eBay API to display key business insights in a user-friendly dashboard.

---

## Key Features
- Displays total orders from the past 90 days.
- Provides a detailed table with the following information for each order:
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
    └── version 1.0
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
Visit [http://localhost:5000](http://localhost:5000) in your web browser.

---

## Known Issues / Future Enhancements
✅ Current MVP displays total orders but lacks additional metrics.  
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

Copyright (c) 2025 Ideal Robot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Author
**John Szpyrka**
- Email: john.l.szpyrka@outlook.com
- GitHub: [IdealRobot](https://github.com/IdealRobot)

---

## Contact
For issues or feature requests, please submit an issue on the GitHub repository.

