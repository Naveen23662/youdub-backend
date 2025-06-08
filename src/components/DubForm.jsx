import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const DubForm = () => {
  const [audioFile, setAudioFile] = useState(null);
  const [youtubeLink, setYoutubeLink] = useState('');
  const navigate = useNavigate();

  const handleFileChange = (e) => {
    setAudioFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!audioFile || !youtubeLink) {
      alert('Please provide both YouTube link and audio file.');
      return;
    }

    const formData = new FormData();
    formData.append('audio', audioFile);
    formData.append('lang', 'te'); // example: Telugu

    try {
      const res = await fetch('https://your-backend-url.com/dub', {
        method: 'POST',
        body: formData,
      });

      const data = await res.json();

      // Convert regular YouTube URL to embed format
      const videoId = youtubeLink.split('v=')[1]?.split('&')[0];
      const embedUrl = `https://www.youtube.com/embed/${videoId}`;

      navigate('/player', {
        state: {
          videoUrl: embedUrl,
          audioUrl: data.output_url,
        },
      });
    } catch (err) {
      console.error('Error:', err);
      alert('Something went wrong.');
    }
  };

  return (
    <div className="p-6 max-w-md mx-auto space-y-4">
      <input
        type="text"
        placeholder="Paste YouTube video link"
        value={youtubeLink}
        onChange={(e) => setYoutubeLink(e.target.value)}
        className="w-full border p-2 rounded"
      />

      <input
        type="file"
        accept="audio/*"
        onChange={handleFileChange}
        className="block w-full"
      />

      <button
        onClick={handleSubmit}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 w-full"
      >
        Submit to Dub
      </button>
    </div>
  );
};

export default DubForm;

