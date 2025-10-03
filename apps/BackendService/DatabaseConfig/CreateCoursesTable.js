const { getConnection, cleanUpconnection } = require('./Connect') 

const createCoursesTable = async () => {

    const connection = await getConnection()

    try {
        await connection.query(`
            CREATE TABLE IF NOT EXISTS courses(
                course_id INT PRIMARY KEY AUTO_INCREMENT,
                semester_id INT NOT NULL,
                course_name VARCHAR(10) NOT NULL,
                course_number VARCHAR(10) NOT NULL,
                description VARCHAR(200),
                attempted_points DECIMAL(5, 3),
                earned_points DECIMAL(5, 3),
                letter_grade VARCHAR(5),
                total_points DECIMAL(7, 3),
                FOREIGN KEY (semester_id) REFERENCES semesters(semester_id)
            )
        `);
        console.log('Courses table created!');
    } catch (error) {
        console.error('Error creating courses table', error);
    } 
}


module.exports = { createCoursesTable }