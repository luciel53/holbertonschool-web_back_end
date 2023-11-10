export default function appendToEachArrayValue(array, appendString) {
  let res = [];
  for (let value of array) {
    res.push(appendString + value);
  }
  return res;
}
