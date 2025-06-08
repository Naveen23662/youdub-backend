import React from 'react';
import { useLocation } from 'react-router-dom';

const DubResult = () => {
  const location = useLocation();
  const audioUrl = location.state?.audioUrl;

  return (
    <div className="p-6 max-w-xl mx-auto text-center">
      <h1 className="text-2xl font-bold mb-4">Dubbed Audio Result</h1>
      {audioUrl ? (
        <audio controls src={audioUrl} className="w-full" />
      ) : (
        <p>No audio result found.</p>
      )}
    </div>
  );
};

export default DubResult;

