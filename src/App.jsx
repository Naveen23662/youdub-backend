import React from 'react';
import { Routes, Route } from 'react-router-dom';

import Home from './pages/Home';
import DubForm from './components/DubForm';
import DubResult from './pages/DubResult';
import DubPlayer from './components/DubPlayer';
import Success from './pages/Success';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/dub" element={<DubForm />} />
      <Route path="/result" element={<DubResult />} />
      <Route path="/player" element={<DubPlayer />} />
      <Route path="/success" element={<Success />} />
    </Routes>
  );
};

export default App;

