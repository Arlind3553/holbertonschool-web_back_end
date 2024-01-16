export default function appendToEachArrayValue(array, appendString) {
  const myValue = [];
  for (let idx of array) {
     myValue.push(appendString + idx)
  }

  return myValue;
}
