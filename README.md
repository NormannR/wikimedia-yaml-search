# Wikimedia YAML Search

**Wikimedia YAML Search** is a cross-platform command-line tool that lets you search and download images from [Wikimedia Commons](https://commons.wikimedia.org/) using a structured YAML file of categories and search queries.

It automatically organizes downloaded images by category and search term into timestamped folders.

---

## 🚀 Features

- 🔍 Searches Wikimedia Commons via the official API
- 📁 Organizes results by category and query
- 📥 Downloads images and saves them locally
- 🕒 Creates timestamped output folders per run
- 🧾 Simple YAML format for defining search terms
- 🐍 CLI interface with support for packaging, `.exe` generation, and GitHub Releases

---

## 📦 Installation

### 🔧 From source

```bash
git clone https://github.com/your-username/wikimedia-yaml-search.git
cd wikimedia-yaml-search
pip install -e .
```

### 📥 From GitHub Releases

Precompiled binaries are available for Windows, Linux, and macOS:
➡️ See the [Releases page](https://github.com/NormannR/wikimedia-yaml-search/releases)

---

## 🧰 Usage

```bash
wikimedia-yaml-search --filename path/to/queries.yaml --limit 3
```

### Arguments:
- `--filename` *(required)*: Path to the YAML file containing categories and search terms
- `--limit` *(optional)*: Number of images to download per query (default: 2)

---

## 🧾 Example YAML

See `animals.yaml`:
```yaml
"Birds":
  - Bald Eagle
  - Kiwi
  - Puffin

"Mammals":
  - Elephant
  - Capybara
  - Red Fox
```

---

## 🗂 Output structure

A folder named `search_YYYY-MM-DD_HH-MM-SS` will be created with the following layout:

```
search_2025-04-21_14-55-33/
├── Birds/
│   ├── Bald Eagle/
│   ├── Kiwi/
│   └── ...
└── Mammals/
    ├── Elephant/
    └── ...
```

Absolutely — that's a thoughtful addition! Here's a friendly, no-jargon **"For Beginners"** section you can add to your `README.md`, just below the usage or release section.

---

## 🐣 For Beginners (No Command Line Experience in Windows)

Want to use the tool but not familiar with the terminal? No problem!

Here’s how to use the program on Windows without needing to install Python or use the command line much:

### 1. ✅ **Download the tool**

1. Go to the [Releases page](https://github.com/NormannR/wikimedia-yaml-search/releases)
2. Download the file called **`wikimedia-yaml-search.exe`**
3. Save it somewhere easy to find, like your Desktop or Downloads folder

---

### 2. 📝 **Create your search file**

1. Open **Notepad**
2. Write something like this:

    ```yaml
    "Birds":
      - Bald Eagle
      - Penguin

    "Mammals":
      - Elephant
      - Capybara
    ```

3. Save the file as `search.yaml` (make sure it ends in `.yaml`, not `.txt`)

---

### 3. 🚀 **Run the program**

1. Hold **Shift** and right-click in the folder where `wikimedia-yaml-search.exe` and `search.yaml` are
2. Click **"Open PowerShell window here"** or **"Open Terminal"**
3. Type:

    ```powershell
    .\wikimedia-yaml-search.exe --filename search.yaml --limit 3
    ```

    This tells the program:
    - Use your file `search.yaml`
    - Download up to 3 images per search

---

### 🧾 What happens next?

- A folder will be created called something like `search_2025-04-21_15-12-09`
- Inside, you'll find images organized by category and search term
- You can open them just like any regular images
- If the output images are not what you expected, don't hesitate to make your queries more precise in the `.yaml` file and run the program again

---

### 💡 Tip

You can make multiple `.yaml` files for different topics and reuse the `.exe` without installing anything else.

## 📄 License

This project is licensed under the [MIT License](LICENSE).