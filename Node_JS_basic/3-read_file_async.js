const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(Error('Cannot load the database'));
        return;
      } else {
        const byLine = data.split('\n').filter((line) => line.trim() !== '');
        let totalStudents = 0;
        const studentsByField = {};
        for (let i = 1; i < byLine.length; i += 1) {
          /* data line by line */
          const elements = byLine[i].split(',');
          /* select the field element and store it in a variable */
          const field = elements[3];
          const firstname = elements[0];
          if (field) {
            if (studentsByField[field] === undefined) {
              studentsByField[field] = {}; // Initialize an object to store firstnames for this field
            }
            if (studentsByField[field][firstname] === undefined) {
              studentsByField[field][firstname] = 1; // Add firstname to this field's list with count 1
            } else {
              studentsByField[field][firstname] += 1; // Increment count for firstname in this field
            }
          }
          totalStudents += 1;
        }

        console.log(`Number of students: ${totalStudents}`);
        for (const field in studentsByField) {
          if (Object.prototype.hasOwnProperty.call(studentsByField, field)) {
            const firstnameByField = Object.keys(studentsByField[field]);
            console.log(
              `Number of students in ${field}: ${Object.values(studentsByField[field]).reduce((a, b) => a + b, 0)}. List: ${firstnameByField.join(', ')}`,
            );
          }
        }
        resolve();
      }
    })
  });
}

module.exports = countStudents;
