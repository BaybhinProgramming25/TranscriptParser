import './Home.css';

const Home = () => {
  return (
    <div className="home-container">
      <div className="home-box">
        <section className="hero-section">
          <h1>Welcome to TQA</h1>
          <p className="hero-text">
            TQA stands for Transcript Q&A. This is an application designed for Stony Brook 
            computer science students to upload their transcripts and get answers to 
            any questions about their academic records.
          </p>
        </section>
        <section className="feature-section">
          <div className="feature-card">
            <div className="feature-image">
              <img src="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800&q=80" alt="Student studying with documents" />
            </div>
            <h2>Upload Your Transcript</h2>
            <p>
              Getting started is simple! Just upload your Stony Brook computer science transcript 
              directly into our chat interface. Our system will read and understand all the 
              information in your transcript, including your courses, grades, credits, and more.
            </p>
            <p>
              Think of it like showing your transcript to a really smart helper who can remember 
              everything about it instantly. Once uploaded, your transcript is parsed in-memory, 
              which means all your academic information is ready to be searched through and 
              analyzed in seconds.
            </p>
            <p>
              No need to constantly look through your PDF over and over again. TQA will be
              able to answer questions based on the PDFs you provided. For privacy reasons, 
              TQA does not store your transcript data on the hard disk. Therefore, for everytime
              you run the applicaton, you will need to provide the transcript. 
            </p>
          </div>
          <div className="feature-card">
            <div className="feature-image">
              <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&q=80" alt="AI chatbot conversation" />
            </div>
            <h2>Ask Anything</h2>
            <p>
              Once your transcript is uploaded, you can ask any question you'd like! Our advanced 
              AI language model (LLM) understands both your transcript data and your questions, 
              combining them to give you accurate, helpful answers.
            </p>
            <ul>
              <li>What's my cumulative GPA?</li>
              <li>How many credits do I have in total?</li>
              <li>What courses did I take in this semester?</li>
              <li>What grade did I get in this class?</li>
              <li>What is my cumulative GPA?</li>
            </ul>
          </div>
          <div className="feature-card">
            <div className="feature-image">
              <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&q=80" alt="Computer science workspace" />
            </div>
            <h2>Why Use TQA?</h2>
            <p>
              Navigating your academic transcript can be confusing and time-consuming. TQA makes 
              it easy by combining the power of AI with an intuitive chat interface. Instead of 
              manually searching through documents, just ask your question in plain English and 
              get instant answers.
            </p>
            <p>
              Built specifically for Stony Brook computer science students, TQA understands the 
              structure of your transcripts and the requirements of your program. Whether you're 
              planning your next semester, checking your progress toward graduation, or just curious 
              about your academic history, TQA is here to help.
            </p>
          </div>
        </section>
        <section className="cta-section">
          <h2>Ready to Explore Your Academic Journey?</h2>
          <p>Join your fellow Stony Brook CS students in making transcript management effortless.</p>
          <div className="cta-buttons">
            <a href="/signup" className="cta-button primary">Sign Up</a>
            <a href="/login" className="cta-button secondary">Log In</a>
          </div>
        </section>
      </div>
    </div>
  );
}
export default Home;