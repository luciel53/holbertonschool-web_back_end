export default function getStudentIdsSum(getListStudents) {
  const sum = getListStudents.reduce((accumulator, student) => {
    return accumulator + student.id;
  }, 0);
  return sum;
}
