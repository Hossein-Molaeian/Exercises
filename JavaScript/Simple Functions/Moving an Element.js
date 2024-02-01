// Write a function that moves an element by its index to an offset location
// Function should return a new array and should not edit the original array

function move(array, index, offset) {
  const list = [...array];
  const placement = index + offset;

  if (placement < 0 || placement > 3) {
    console.error("Invalid offset.");
    return;
  }
  list.splice(index, 1); // removes the element
  list.splice(placement, 0, array[index]); // adds the element to the correct location
  return list;
}

const numbers = [1, 2, 3, 4];
const output = move(numbers, 2, -2); // move element at index 2, 2 index to the left
console.log(output);
