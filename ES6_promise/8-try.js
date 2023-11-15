export default function divideFunction(numerator, denominator) {
  if (denominator !== 0) {
    const res = numerator / denominator;
    return res;
  } else {
    throw new Error('cannot divide by 0');
  }
}
