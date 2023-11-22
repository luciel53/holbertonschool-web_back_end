export default function cleanSet(set, startString) {
  let text = '';
  set.forEach((value) => {
    if (startString === '' || !startString || typeof startString !== 'string') {
      text = '';
    } else if (typeof value === 'string' && value.includes(startString)) {
      const deletePartString = value.substring(startString.length);
      text += `${deletePartString}-`;
    }
  });
  return text.slice(0, -1);
}
