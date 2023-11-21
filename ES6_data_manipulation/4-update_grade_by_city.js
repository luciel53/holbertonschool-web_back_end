export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  if (newGrades) {
    const studentsByCity = getListStudents.filter((student) => student.location === city);
    const studentsGradeByCity = studentsByCity.map((student) => {
      const matchGrade = newGrades.find((grade) => grade.studentId === student.id);
      return {
        ...student,
        grade: matchGrade ? matchGrade.grade : 'N/A',
      };
    });
    return studentsGradeByCity;
  }
  return 'N/A';
}
