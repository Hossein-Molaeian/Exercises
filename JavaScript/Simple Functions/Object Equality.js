// Write a function that checks if 2 objects have equal property values. (areEqual)
// Write another function which checks if 2 objects have the same reference. (areSame)

function Address(street, city, zipCode) {
  this.street = street;
  this.city = city;
  this.zipCode = zipCode;
}

function areEqual(address1, address2) {
  for (let key1 in address1)
    for (let key2 in address2)
      if (key1 === key2 && address1[key1] !== address2[key2]) return false;
  return true;
}

function areSame(address1, address2) {
  return address1 === address2; // Checks references aswell.
}

let address1 = new Address("a", "b", "c");
let address2 = new Address("a", "b", "c");
let address3 = address1;

console.log(areEqual(address1, address2));
console.log(areSame(address1, address2));
console.log(areSame(address1, address3));
