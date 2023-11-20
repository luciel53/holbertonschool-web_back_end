export default function getStudentsByLocation(getListStudents, city) {
  const cityStudents = getListStudents.filter((student) => student.location === city);
  return cityStudents;
}
