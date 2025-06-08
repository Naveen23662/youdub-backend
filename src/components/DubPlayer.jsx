import React from 'react';
import { useLocation } from 'react-router-dom';

const DubPlayer = () => {
  const location = useLocation();
  const { videoUrl, audioUrl, transcript } = location.state || {};

  return (
    <div className="p-6 max-w-5xl mx-auto space-y-6">
      <h1 className="text-2xl font-bold text-center">🎧 Dubbed YouTube Playback</h1>

      {videoUrl && (
        <iframe
          src={videoUrl + '?autoplay=1&mute=1'}
          width="100%"
          height="400"
          frameBorder="0"
          allow="autoplay; encrypted-media"
          allowFullScreen
          title="YouTube Video"
        ></iframe>
      )}

      {audioUrl && (
        <audio controls autoPlay className="w-full">
          <source src={audioUrl} type="audio/mpeg" />
        </audio>
      )}

      {transcript && (
        <div className="bg-gray-100 p-4 rounded mt-6">
          <h2 className="text-lg font-semibold mb-2">📜 Transcript</h2>
          <ul className="space-y-2 text-left">
            {transcript.map((block, index) => (
              <li key={index}>
                <strong>{block.speaker}:</strong> {block.text}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default DubPlayer;

