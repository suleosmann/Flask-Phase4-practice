import React from 'react';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';

function App() {
  return (
    <div>
      <h1>Simple User Authentication</h1>
      <LoginForm />
      <hr />
      <SignupForm />
    </div>
  );
}

export default App;
