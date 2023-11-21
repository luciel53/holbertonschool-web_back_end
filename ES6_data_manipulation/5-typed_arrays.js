export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const DV = new DataView(buffer, 0);
  if (buffer.byteLength !== length) {
    throw new Error('Position outside range');
  }
  DV.setInt8(position, value);
  return DV;
}
