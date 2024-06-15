import React, { useState } from 'react';
import { useRouter } from 'next/router';

function Index() {
  const [location, setLocation] = useState('');
  const [enemy, setEnemy] = useState('');
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:5001/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ Location: location, Enemy: enemy }),
    });
    const data = await response.json();
    // Encode predictions data into query parameters
    const queryParams = new URLSearchParams(data).toString();
    // Navigate to the predictions page with query parameters
    router.push(`/predictions?${queryParams}`);
  };

  return (
    <div className="login">
      <img src="/login-bg.jpg" alt="image" className="login__bg" />

      <form onSubmit={handleSubmit} className="login__form">
        <h1 className="login__title">PREDICT COMPOSITION</h1>

        <div className="login__inputs">
          <div className="login__box">
            <input
              type="text"
              placeholder="Select enemy"
              value={enemy}
              onChange={(e) => setEnemy(e.target.value)}
              required
              className="login__input"
            />
            <i className="ri-mail-fill"></i>
          </div>

          <div className="login__box">
            <input
              type="text"
              placeholder="Select Location"
              value={location}
              onChange={(e) => setLocation(e.target.value)}
              required
              className="login__input"
            />
            <i className="ri-lock-2-fill"></i>
          </div>
        </div>

        <button type="submit" className="login__button">
          Predict
        </button>
      </form>
    </div>
  );
}

export default Index;
