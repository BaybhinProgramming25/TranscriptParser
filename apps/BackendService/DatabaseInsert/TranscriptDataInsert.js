const { getConnection, cleanUpconnection } = require('../DatabaseConfig/Connect')

const insertTranscriptData = async (data) => {
    
    const connection = await getConnection();

    for(const semesterObject of data) {

        const semesterName = Object.keys(semesterObject)[0];
        const courses = semesterObject[semesterName];

        console.log(`Adding ${semesterName}...`);

        const [semesterResult] = await connection.query(
            'INSERT INTO semesters (semester_name) VALUES (?)',
            [semesterName]
        )

        const semesterId = semesterResult.insertId;

        for(const course of courses) {

            console.log(`Adding ${course.course_name}...`)

            const [courseResult] = await connection.query(
                `INSERT INTO courses(semester_id, course_name, course_number, description, attempted_points, earned_points, letter_grade, total_points) VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
                [
                    semesterId,
                    course.name,
                    course.number,
                    course.description,
                    course.attempted_points,
                    course.earned_points,
                    course.letter_grade,
                    course.total_points
                ]
            )

            console.log(courseResult)
        }
    }

    await cleanUpconnection(connection);
}

module.exports = { insertTranscriptData }