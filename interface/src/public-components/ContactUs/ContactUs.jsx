import { useState } from 'react';
import axios from 'axios';

import './ContactUs.css';

const ContactUs = () => {

  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [subject, setSubject] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    
    e.preventDefault();

    const data = {
      name: name,
      email: email,
      subject: subject,
      message: message
    }

    try {
      await axios.post('http://localhost:3000/api/contact', data);
      alert('Thank you for contacting us! We will get back to you soon.');
    }
    catch (error) {
      console.log('Error sending information')
      alert('Unable to send message. Please try again later');
    }
  };

  return (
    <div className="contact-container">
      <div className="contact-box">
        <h1>Contact Us</h1>
        <p className="subtitle">Have a question? We'd love to hear from you!</p>
        
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label htmlFor="name">Your Name</label>
            <input
              type="text"
              id="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Enter your name"
              required
            />
          </div>

          <div className="input-group">
            <label htmlFor="email">Email Address</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter your email"
              required
            />
          </div>

          <div className="input-group">
            <label htmlFor="subject">Subject</label>
            <input
              type="text"
              id="subject"
              value={subject}
              onChange={(e) => setSubject(e.target.value)}
              placeholder="What's this about?"
              required
            />
          </div>

          <div className="input-group">
            <label htmlFor="message">Message</label>
            <textarea
              id="message"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              placeholder="Tell us more..."
              rows="6"
              required
            />
          </div>

          <button type="submit" className="contact-button">Send Message</button>
        </form>

        <div className="contact-info">
          <p>Or reach us directly:</p>
          <p className="phone">📞 +1 (800) TQA</p>
          <p className="email-info">✉️ support@tqa.com</p>
        </div>
      </div>
    </div>
  );
}

export default ContactUs;