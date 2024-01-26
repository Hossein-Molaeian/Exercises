// Write a function which takes a driver's speed and evaluates its demerit points.
// Speed limit is 70km/h and each 5km/h above the speed limit is 1 demerit point.
// More than or equal to 12 points results in license suspension.

function checkingSpeed(speed) {
  const speedLimit = 70;
  const kmPerPoint = 5;

  if (speed < speedLimit + kmPerPoint) return "Ok";
  let points = Math.floor((speed - speedLimit) / kmPerPoint);
  if (points >= 12) return "License suspended.";
  return points;
}

console.log(checkingSpeed(85));
