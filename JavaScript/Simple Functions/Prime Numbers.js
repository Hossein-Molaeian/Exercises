// Write 2 functions that calculate primes upto a given number.

function isPrime(number) {
  for (j = 2; j < number; j++) {
    // not 1 and not the number itself (<), because every number is divisible by 1 and itself.
    if (number % j === 0) {
      return false;
    }
  }
  return true;
}

function showPrimes(limit) {
  for (i = 2; i <= limit; i++) if (isPrime(i)) console.log(i);
}

showPrimes(10);
