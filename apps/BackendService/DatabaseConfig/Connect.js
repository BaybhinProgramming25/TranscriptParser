const mysql = require('mysql2/promise')

const createDatabase = async () => {
    
    const connection = await mysql.createConnection({
        host: process.env.HOST,
        user: 'root',
        password: process.env.PASSWORD
    })

    try {
        await connection.query(`CREATE DATABASE IF NOT EXISTS studentdata`)
        console.log('Database Created')
    } catch (error) {
        console.error('Error creating database:', error)
    } 
}

// Get the connection
const getConnection = async () => {
    const connection = await mysql.createConnection({
        host: process.env.HOST,
        user: 'root',
        password: process.env.PASSWORD, // Password will be supplied via .env 
        database: 'studentdata'
    })

    return connection
}

// Clean up
const cleanUpconnection = async (connection) => {
    try {
        await connection.end()
        console.log('Connection closed!')
    } catch (error) {
        console.error('Error closing connection: ', error)
    }
}

module.exports = { createDatabase, getConnection, cleanUpconnection}