// Connecting randomizer function from another file
const { getRandomNumber, getRandomColor } = require('./randomizer');

// Getting a canvas element
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Function for drawing a geometric figure
function drawShape(type, x, y, size, color) {
  switch (type) {
    case 'circle':
      ctx.beginPath();
      ctx.arc(x, y, size / 2, 0, 2 * Math.PI);
      ctx.fillStyle = color;
      ctx.fill();
      break;
    case 'square':
      ctx.fillRect(x - size / 2, y - size / 2, size, size);
      ctx.fillStyle = color;
      break;
    case 'triangle':
      ctx.beginPath();
      ctx.moveTo(x, y - size / 2);
      ctx.lineTo(x + size / 2, y + size / 2);
      ctx.lineTo(x - size / 2, y + size / 2);
      ctx.closePath();
      ctx.fillStyle = color;
      ctx.fill();
      break;
  }
}

// Function for generating random shapes
function generateShapes() {
  // Очистка canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Getting the number of shapes
  const numShapes = getRandomNumber(10, 20);

  // Shape generation
  for (let i = 0; i < numShapes; i++) {
    // Obtaining random shape parameters
    const type = getRandomShapeType();
    const x = getRandomNumber(0, canvas.width);
    const y = getRandomNumber(0, canvas.height);
    const size = getRandomNumber(20, 50);
    const color = getRandomColor();

    // Figure drawing
    drawShape(type, x, y, size, color);
  }
}

// Generating shapes on page load
generateShapes();

// Adding a button to generate new figures (optional)
const generateButton = document.createElement('button');
generateButton.textContent = 'Сгенерировать новые фигуры';
generateButton.addEventListener('click', generateShapes);
document.body.appendChild(generateButton);
