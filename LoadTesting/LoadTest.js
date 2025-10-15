import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    vus: 1,
    duration: '3s'
};

// Load PDF file - make sure your PDF file is in the same directory
const pdfFile = open('../PDFs/Test1.pdf', 'b');

export default function() {
    
    const url = 'http://127.0.0.1:8000/parse';
    
    const data = {
        file: http.file(pdfFile, 'document.pdf', 'application/pdf')
    };
    
    const res = http.post(url, data);
    
    console.log(`Status: ${res.status}`);
    
    sleep(1);
}