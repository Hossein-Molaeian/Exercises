function StopWatch() {
  let timeStart,
    timeEnd,
    flag, // checking if stopwatch is already running or not
    duration = 0;

  this.start = function () {
    if (flag) throw new Error("Stopwatch has already started");

    flag = true;
    timeStart = new Date();
  };

  this.stop = function () {
    if (!flag) throw new Error("Stopwatch is not started");

    flag = false;
    timeEnd = new Date();

    const seconds = (timeEnd.getTime() - timeStart.getTime()) / 1000; // getTime() method returns milliseconds
    duration += seconds;
  };

  this.reset = function () {
    timeStart = 0;
    timeEnd = 0;
    flag = false;
    duration = 0;
  };

  Object.defineProperty(this, "duration", {
    get: function () {
      return duration;
    },
  });
}
