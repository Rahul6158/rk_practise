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
            padding: 10px;
            text-align: center;
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
    </style>
</head>
<body>
    <div class="header">
        <h1>Generated Content</h1>
    </div>
    <ul>
        <li><a href="#section0">Introduction to Stack</a></li>
        <li><a href="#section1">Operations on Stack</a></li>
        <li><a href="#section2">Applications of Stack</a></li>
    </ul>
    <div class="content">
        <section id="section0" class="section">
            <h2>Introduction to Stack</h2>
            <p>A stack is a linear data structure that follows LIFO (Last In First Out).</p>
        </section>
        <section id="section1" class="section">
            <h2>Operations on Stack</h2>
            <p>The main operations on a stack are push, pop, and peek.</p>
        </section>
        <section id="section2" class="section">
            <h2>Applications of Stack</h2>
            <p>Stacks are used in expression evaluation, backtracking algorithms, etc.</p>
        </section>
        <div style="margin-top: 20px;">
            <button id="prevBtn" class="nav-btn">Previous</button>
            <button id="nextBtn" class="nav-btn">Next</button>
        </div>
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
