# NFC-e to NF-e Converter

A lightweight web application designed to convert Brazilian **NFC-e (Electronic Consumer Invoice)** XML files into **NF-e (Electronic Invoice)** XML format. Built with Python and Flask, this tool offers a straightforward interface for data transformation and educational demonstrations.

## ⚠️ Disclaimer

This software is provided for **educational and demonstration purposes only**. The converted XML files should not be used for official tax submissions without proper validation and compliance checks according to Brazilian federal revenue (Receita Federal) standards. Use at your own risk.

## Prerequisites

- **Python 3.7** or higher
- **pip** (Python package installer)

## Installation & Setup

Follow these steps to set up the project locally:

1. **Clone the Repository**
   bash
   git clone https://github.com/dougdotcon/converte-nfce-for-nfe.git
   cd converte-nfce-for-nfe
   

2. **Install Dependencies**
   Install the required Python libraries using the `requirements.txt` file:
   bash
   pip install -r requirements.txt
   

## Usage

1. **Run the Application**
   Start the Flask web server by executing the main script:
   bash
   python app.py
   
   The terminal will display a local URL (usually `http://127.0.0.1:5000`).

2. **Open in Browser**
   Navigate to the provided URL in your web browser.

3. **Convert Files**
   - Click the **"Procurar" (Browse)** button.
   - Select your source `.xml` file containing the NFC-e data.
   - Click **Upload/Convert**.

4. **Get Result**
   The application will process the file and download the converted file named **`nfe_convertida.xml`** to your local machine.

## Project Structure

- `app.py`: The main Flask application logic and routing.
- `templates/`: Contains the HTML files for the user interface.
- `requirements.txt`: List of Python dependencies (Flask, lxml, requests).

## Contributing

Contributions are welcome! Please follow this process:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/improvement`).
5. Open a Pull Request.

## Contact

**Author:** Douglas H. Machado  
**Email:** [dougdotcon@gmail.com](mailto:dougdotcon@gmail.com)  
**LinkedIn:** [dougdoton](https://www.linkedin.com/in/dougdoton/)  
**GitHub:** [dougdotcon](https://github.com/dougdotcon)
