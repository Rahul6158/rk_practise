import streamlit as st

def generate_html_content(data):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Generated HTML</title>
        <style>
            *{
                margin:0;
                padding:0;
                box-sizing: border-box;
            }
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            .header {
                background-color: #4CAF50;
                color: white;
                padding: 20px;
                text-align: center;
                font-size: 24px;
            }
            ul {
                list-style: none;
                position: fixed;
                top: 0;
                left: 0;
                width: 200px;
                height: 100%;
                background-color: #333;
                padding: 20px;
                box-shadow: 2px 0px 5px black;
            }
            ul li {
                margin: 20px 0;
            }
            ul li a {
                color: white;
                text-decoration: none;
                font-size: 18px;
                padding: 5px;
                display: block;
            }
            ul li a:hover {
                background-color: #575757;
                color: #fff;
            }
            .content {
                margin-left: 220px;
                padding: 20px;
            }
            .section {
                display: none;
            }
            .section.active {
                display: block;
            }
            .nav-btn {
                margin-top: 20px;
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border: none;
                cursor: pointer;
                font-size: 18px;
            }
            .nav-btn:hover {
                background-color: #45a049;
            }
            @media (max-width: 768px) {
                ul {
                    width: 100%;
                    height: auto;
                    position: relative;
                }
                .content {
                    margin-left: 0;
                }
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Generated Content</h1>
        </div>
        <ul>
            {}
        </ul>
        <div class="content">
            {}
        </div>
        <script>
            const sections = document.querySelectorAll('.section');
            const navLinks = document.querySelectorAll('ul li a');
            let currentSectionIndex = 0;

            function showSection(index) {
                sections.forEach(section => section.classList.remove('active'));
                sections[index].classList.add('active');
                currentSectionIndex = index;
            }

            navLinks.forEach((link, index) => {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    showSection(index);
                });
            });

            document.getElementById('prevBtn').addEventListener('click', () => {
                if (currentSectionIndex > 0) {
                    showSection(currentSectionIndex - 1);
                }
            });

            document.getElementById('nextBtn').addEventListener('click', () => {
                if (currentSectionIndex < sections.length - 1) {
                    showSection(currentSectionIndex + 1);
                }
            });

            // Show the first section by default
            showSection(0);
        </script>
    </body>
    </html>
    """

    # Generate navigation links and sections
    headers_html = ""
    sections_html = ""
    for i, (header, content) in enumerate(data.items()):
        headers_html += f'<li><a href="#section{i}">{header}</a></li>\n'
        sections_html += f'''
        <section id="section{i}" class="section">
            <h2>{header}</h2>
            <p>{content}</p>
        </section>
        '''

    # Add navigation buttons at the bottom of the sections
    sections_html += '''
        <div style="margin-top: 20px;">
            <button id="prevBtn" class="nav-btn">Previous</button>
            <button id="nextBtn" class="nav-btn">Next</button>
        </div>
    '''

    # Return the structured HTML content
    return html_content.format(headers_html, sections_html)

# Streamlit App
st.title('HTML Content Generator')

# Input data (you can customize this as needed)
st.write("Provide data as dictionary of headers and content")
sample_data = {
    "Introduction to Stack": "Stack is a linear data structure that follows the LIFO principle...",
    "Operations on Stack": "The primary operations are push, pop, peek, and isEmpty...",
    "Applications of Stack": "Stack is used in expression evaluation, syntax parsing, and more...",
    "Implementation of Stack": "Stacks can be implemented using arrays or linked lists..."
}

# Text input for raw data (headers and content)
data_input = st.text_area("Enter your data (JSON format):", value=str(sample_data))

# Convert the input to a Python dictionary
try:
    input_data = eval(data_input)
except Exception as e:
    st.error(f"Invalid input format. Please enter data as a dictionary. Error: {e}")
    input_data = {}

# Generate HTML if data is valid
if input_data:
    st.subheader('Generated HTML Preview')
    
    # Generate the HTML content
    html_output = generate_html_content(input_data)
    
    # Display the HTML code
    st.code(html_output, language='html')
    
    # Option to download the generated HTML file
    st.download_button("Download HTML", data=html_output, file_name="generated_content.html", mime="text/html")
