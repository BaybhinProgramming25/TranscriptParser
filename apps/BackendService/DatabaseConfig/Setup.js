const { createDatabase } = require('./Connect')
const { createSemestersTable } = require('./CreateSemestersTable')
const { createCoursesTable } = require('./CreateCoursesTable')

const setupTables = async () => {

    // Run the table functions
    console.log('Starting Database Setup...')

    await createDatabase();

    await createSemestersTable();
    await createCoursesTable();

    console.log('All tables created')

}

module.exports = { setupTables }