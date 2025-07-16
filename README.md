<div align = "center">

# NYT Letter Boxed Puzzle Solver
[![Web Deployment](https://img.shields.io/badge/❄%20Web%20Deployment-NY_Letter_Boxed_Solver-4baaaa.svg)](https://ny-letter-boxed-solver.onrender.com/)

</div>

<div align = "justify">

A full-stack, ready-to-deploy template for solving the New York Times Letter Boxed puzzle. Built with **FastAPI** (backend) and plain
**HTML**, **CSS**, and **JavaScript** (frontend). The app fetches daily puzzle data from a connected GitHub repository and computes 1-, 2-, or 3-word
solutions on demand.

## 🚀 Features

* **Two-Column Responsive Layout**

  * Left panel: Interactive 3-letter-per-side puzzle grid + solution controls + social links.
  * Right panel: Dynamic solution display.
* **Dynamic Puzzle Fetching**

  * `/api/puzzle` endpoint pulls the latest puzzle JSON from GitHub.
* **On-Demand Solver**

  * `/api/solve?words={1|2|3}` returns valid word chains covering all 12 letters.
* **Loading & Error States** during solution generation.
* **NYT-Inspired Styling** with a clean serif font and minimal palette.
* **Render Deployment**

  * Configured for Render.com Free Hobby plan.
* **Developer-Friendly**

  * `if __name__ == "__main__"` block for local testing.

---

## 📁 Project Structure

```bash
letter-boxed-solver/
├── assets/icons/       # Optional icon assets (site-favicon.png)
├── src/                # Python solver and scraper for letter-boxed puzzle
├── main.py             # FastAPI application
├── requirements.txt    # Python dependencies
├── static/             # Frontend assets
│   ├── style.css       # CSS styles
│   └── script.js       # JavaScript logic
├── index.html          # Main HTML template
└── README.md           # Project documentation
```

## 🛠️ Installation & Local Development

1. **Clone the repository**:

   ```bash
     $ git clone https://github.com/code-archived/letter-boxed-solver.git
     $ cd letter-boxed-solver
   ```

2. **Install dependencies**:
   ```bash
      pip install -r requirements.txt
    ```

3. **Run locally**:

   ```bash
     uvicorn main:app

Open in [http://localhost:8000](http://localhost:8000) browser.

## ☁️ Deploying on Render (Free Hobby)

1. Push your code to GitHub.
2. Log in to [Render.com](https://render.com/) and click **New → Web Service**.
3. Connect your GitHub repo `letter-boxed-solver`.
4. Configure:
   - **Environment**: Python 3
   - **Plan**: Free (Hobby)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. (Optional) Add environment variables:
   - `GITHUB_PUZZLE_URL`: URL to your raw puzzle JSON in GitHub
   - `GITHUB_TOKEN`: if fetching from a private repo
6. **Create Web Service** and wait for deployment to finish.

## ⚙️ Configuration

- **Puzzle Source**: Update `get_puzzle()` in `main.py` to point to your GitHub raw URL.
- **Solver Logic**: Replace the placeholder in `/api/solve` with your custom algorithm.

</div>
