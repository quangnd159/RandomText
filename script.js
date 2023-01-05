const textElement = document.getElementById('text');
const selectElement = document.getElementById('set-select');

// Function to generate a random text from the JSON data
function generateText() {
  fetch('texts.json')
    .then(response => response.json())
    .then(data => {
      // Access the desired set of data using the selected option value
      const textSet = data[selectElement.value];
      // Generate a random text from the set
      const text = textSet[Math.floor(Math.random() * textSet.length)];
      // Update the text element with the generated text
      textElement.textContent = text;
    });
}

// Populate the select element with the available sets of data
fetch('texts.json')
  .then(response => response.json())
  .then(data => {
    for (const key in data) {
      const option = document.createElement('option');
      option.value = key;
      option.textContent = key;
      selectElement.appendChild(option);
    }
  });

// Generate a text when the user press Enter or tap on mobile
document.addEventListener('keydown', event => {
  if (event.key === 'Enter') {
    generateText();
  }
});
document.addEventListener('touchstart', generateText);