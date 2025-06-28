import React, { useState } from 'react';

function App() {
  const [youtubeUrl, setYoutubeUrl] = useState('');
  const [language, setLanguage] = useState('hi');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse('');

    try {
      const res = await fetch('https://youdub-backend.onrender.com/dub', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          youtube_url: youtubeUrl,
          language: language,
        }),
      });

      const data = await res.json();
      setResponse(data.message || 'Success!');
    } catch (error) {
      setResponse('Error: ' + error.message);
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>YouDub 🌍</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter YouTube URL"
          value={youtubeUrl}
          onChange={(e) => setYoutubeUrl(e.target.value)}
          required
          style={{ width: '300px', padding: '8px' }}
        />

        <select
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
          style={{ marginLeft: '10px', padding: '8px' }}
        >
          <optgroup label="Indian Languages">
            <option value="hi">Hindi</option>
            <option value="te">Telugu</option>
            <option value="ta">Tamil</option>
            <option value="bn">Bengali</option>
            <option value="ml">Malayalam</option>
            <option value="gu">Gujarati</option>
            <option value="mr">Marathi</option>
            <option value="kn">Kannada</option>
            <option value="pa">Punjabi</option>
            <option value="ur">Urdu</option>
          </optgroup>

          <optgroup label="International Languages">
            <option value="en">English</option>
            <option value="es">Spanish</option>
            <option value="fr">French</option>
            <option value="de">German</option>
            <option value="it">Italian</option>
            <option value="ru">Russian</option>
            <option value="ja">Japanese</option>
            <option value="ko">Korean</option>
            <option value="pt">Portuguese</option>
            <option value="zh">Chinese</option>
          </optgroup>
        </select>

        <button type="submit" style={{ marginLeft: '10px', padding: '8px' }}>
          {loading ? 'Dubbing...' : 'Dub'}
        </button>
      </form>

      {response && (
        <div style={{ marginTop: '1rem', fontWeight: 'bold' }}>
          {response}
        </div>
      )}
    </div>
  );
}

export default App;

