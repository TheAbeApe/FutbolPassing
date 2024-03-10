import React from 'react';
import ReactDOM from 'react-dom';


const App = () => (
  <>
    <header>
      <p>This will be the logo </p>
      <h1>CHELSEA FC ANALYTICS HUB</h1>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="index.html#">About</a></li>
          <li><a href="index.html">Contact</a></li>
          <li><a href="index.html">PlayerNetworks</a></li>
          <li><a href="index.html">MVPPasses</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <h1>Welcome to the Ultimate Chelsea FC Analytics Hub</h1>
      <p>Greetings, Blues fans and soccer analytics enthusiasts! You’ve just stepped into a world where passion for soccer meets the precision of data. 
        Our mission is to provide Chelsea FC supporters and data-savvy fans with in-depth analyses, interactive data visualizations, 
        and a unique platform to explore the beautiful game. Dive into a new way of experiencing soccer, 
        powered by React and our community’s love for Chelsea.</p>
    </main>
    <section id="about">
    <h2>Interactive Passing Data Project: A Closer Look</h2>
    <p>At the heart of our website lies the Interactive Passing Data Project, a pioneering initiative designed to transform how we view and analyze soccer matches.
       Utilizing React's dynamic capabilities, this project offers fans the opportunity to input and visualize passing data in real-time. 
       Imagine clicking on circles representing Chelsea's players on a virtual pitch, tracking passes, and uncovering the strategies that define our victories. 
      This platform isn't just about observing; it's about engaging directly with the game's fabric, one pass at a time.</p>
  </section>
  <section id="recent-game">
    <h2>Recent Match Insights at Your Fingertips</h2>
    <p>tay ahead of the game with detailed analyses and statistics from Chelsea's three most recent matches. 
      From comprehensive match reports to player performance ratings, dive into the numbers that matter.
    </p>
    <ul>
      <li><a href="#"> Match 1 Placeholder [Link to full analysis]</a></li>
      <li><a href="#">Match 2 Placeholder [Link to full analysis]</a></li>
      <li><a href="#">Match 3 Placeholder [Link to full analysis]</a></li>
      
    </ul>
    <p>Keep up with the latest trends and strategies as we dissect each game to bring you the insights you crave.</p> 
    <p>Insert Image Placeholder for Match Data Visualization]</p>
  </section>
  <section id="MVP-Passes">
    <h2>Spotlight on the Last Game’s MVP: Passing Mastery Unveiled</h2>
    <p>Every match has its standout performers, and here we shine a light on the MVP from Chelsea’s latest outing. 
      Explore the passing maps that showcase their vision, strategy, 
      and impact on the game's flow. Discover how key passes carved out opportunities and led to decisive moments on the pitch.</p>
    <p>Insert Image Placeholder for MVP Passes]</p>
    <p>Delve into the artistry behind the passes that make the difference.</p>

  </section>
  <section id="News">
    <h2>Catch Up on the Latest Chelsea FC News</h2>
    <p>Don't miss out on any updates from Stamford Bridge! From transfer rumors to exclusive interviews and behind-the-scenes content, 
      stay connected with all things Chelsea FC.</p>
      <ul>
        <li><a href="#"> News Article 1 Placeholder [Read More]</a></li>
        <li><a href="#">News Article 2 Placeholder [Read More]</a></li>
        <li><a href="#">News Article 3 Placeholder [Read More]</a></li>
      </ul>
      <p>Your go-to source for all the latest Chelsea buzz, straight from the heart of London.</p>
      <p>Insert Image Placeholder for News Section]</p>
  </section>
    <footer>
      <p>© 2021 Chelsea FC Analytics Hub. All rights reserved.</p>
    </footer>
  </>
);

ReactDOM.render(<App />, document.getElementById('root'));