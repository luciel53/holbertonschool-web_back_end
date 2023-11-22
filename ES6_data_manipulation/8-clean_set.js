export default function cleanSet(set, startString) {
  let text = '';
  set.forEach((value) => {
    if (startString === '' || !startString || typeof value !== 'string') {
      text = '';
    } else if (value.startsWith(startString)) {
      const deletePartString = value.substring(startString.length);
      text += `${deletePartString}-`;
    }
  });
  return text.slice(0, -1);
}
