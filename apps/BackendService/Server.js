const express = require('express');
const app = express();

// Let it read JSON data
app.use(express.json());

// A simple endpoint to receive your data
app.get('/', (req, res) => {
    console.log('M!');
    res.json({ message: 'Success Guru!' });
});

// Capture the semester data on this endpoint
app.post('/studentdata', (req, res) => {
    
    // Get the data 
    console.log(req)

    // Put the data into MySQL database
    // Will do this later 
    res.json({ message: 'Successfully received data!'})

})

// Start the server
app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});