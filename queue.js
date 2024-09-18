// Function to load the visualization page inside an iframe
function loadVisualization() {
    // Remove existing iframes, if any, to avoid stacking up multiple iframes
    const container = document.getElementById('visualization-container');
    container.innerHTML = ''; // Clear the container

    var iframe = document.createElement('iframe');
    iframe.src = 'Basics/stack/stack.html'; // Correct path to your visualization page
    iframe.width = '100%';
    iframe.height = '500px'; // Adjust height as needed
    iframe.frameBorder = '0';
    iframe.allowFullscreen = true;
    
    container.appendChild(iframe); // Append the new iframe to the container
}

// Array of links to different pages for navigation
const links = [
    'Ds_intro/dsa.html',          // Path to the DSA introduction page
    'Basics/stack/stack.html',    // Path to the Stack visualization
    'DS/whatisDS.html',           // Path to the "What is Data Structures" page
    'Basics/stack/stack_notes.html', // Path to Stack notes
    'Basics/QueueArray.html',     // Path to Queue Array page
    'Basics/QueueLinkedlist.html' // Path to Queue Linked List page
];

let currentIndex = 0; // Keep track of the current link index
let navigationStack = []; // Stack to keep track of visited pages

// Function to load content into an iframe based on the provided URL
function loadContent(url) {
    document.getElementById('contentFrame').src = url;
    currentIndex = links.indexOf(url); // Set the current index when content is loaded
}

// Function to navigate to the previous content
function prevContent() {
    if (navigationStack.length > 0) {
        currentIndex = navigationStack.pop(); // Pop the last visited index from the stack
        document.getElementById('contentFrame').src = links[currentIndex];
    }
}

// Function to navigate to the next content
function nextContent() {
    if (currentIndex < links.length - 1) {
        navigationStack.push(currentIndex); // Push the current index onto the stack before navigating
        currentIndex++;
        document.getElementById('contentFrame').src = links[currentIndex];
    }
}

// Function to initialize the navigation buttons
function initializeNavigation() {
    document.getElementById('prevButton').addEventListener('click', prevContent);
    document.getElementById('nextButton').addEventListener('click', nextContent);
    loadContent(links[currentIndex]); // Load the first content by default
}

// Initialize the navigation when the window loads
window.onload = function() {
    initializeNavigation();
};
