// Write a function that outputs 'x' number of stars
// according to the number of the row we are in.

function showStars(rows) {
  for (row = 1; row <= rows; row++) {
    let output = "";
    for (i = 0; i < row; i++) output += "*";
    console.log(output);
  }
}

showStars(5);
