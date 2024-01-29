// Write a function that counts truthy values in an array.

function countTruthy(array) {
  let points = 0;
  for (value of array) if (value) points++;
  return points;
}

console.log(countTruthy([0, "", 1, 2, 3, NaN]));
