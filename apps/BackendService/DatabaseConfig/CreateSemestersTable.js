const { getConnection, cleanUpconnection } = require('./Connect');

const createSemestersTable = async () => {

    const connection = await getConnection();

    try {
        await connection.query(`
            CREATE TABLE IF NOT EXISTS semesters (
                semester_id INT PRIMARY KEY AUTO_INCREMENT,
                semester_name VARCHAR(50) NOT NULL
            )    
        `);
        
        console.log('Semesters table created');
    } catch (error) {
        console.error('Error creating semesters table', error)
    }
}

module.exports = { createSemestersTable }