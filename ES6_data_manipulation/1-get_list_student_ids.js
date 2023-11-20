export default function getListStudentIds(studentIdArray) {
  if (Array.isArray(studentIdArray) === false) {
    return [];
  }
  const studentId = studentIdArray.map((student) => student.id);
  });
  return studentId;
}
