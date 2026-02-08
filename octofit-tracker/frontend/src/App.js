import './App.css';
import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function Navbar() {
  return (
    <nav className="navbar">
      <img src={process.env.PUBLIC_URL + '/octofitapp-small.svg'} alt="OctoFit Logo" className="navbar-logo" />
      <div className="navbar-links">
        <Link to="/activities" className="navbar-link">Activities</Link>
        <Link to="/leaderboard" className="navbar-link">Leaderboard</Link>
        <Link to="/teams" className="navbar-link">Teams</Link>
        <Link to="/users" className="navbar-link">Users</Link>
        <Link to="/workouts" className="navbar-link">Workouts</Link>
      </div>
    </nav>
  );
}

function App() {
  return (
    <div className="App">
      <Navbar />
      <h1>Octofit Tracker</h1>
      <main>
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={<h2>Welcome to Octofit Tracker!</h2>} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
