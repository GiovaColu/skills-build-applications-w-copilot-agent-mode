import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

function Teams() {
  const [data, setData] = useState([]);
  useEffect(() => {
    console.log('Fetching from:', API_URL);
    fetch(API_URL)
      .then(res => res.json())
      .then(json => {
        const results = Array.isArray(json) ? json : json.results || [];
        setData(results);
        console.log('Fetched teams:', json);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, []);
  return (
    <div>
      <h2>Teams</h2>
      <ul>
        {data.map((item, idx) => (
          <li key={item.id || idx}>{JSON.stringify(item)}</li>
        ))}
      </ul>
    </div>
  );
}

export default Teams;
