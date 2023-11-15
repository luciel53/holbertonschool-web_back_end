export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0');
  }
  else {
    let res = numerator / denominator;
    return res;
  }

  try {
    divideFunction(numerator, denominator);
  } catch (e) {
    console.error(e);
  }
}
