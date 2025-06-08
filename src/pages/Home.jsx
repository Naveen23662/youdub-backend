import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const [youtubeUrl, setYoutubeUrl] = useState('');
  const [lang, setLang] = useState('te');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async () => {
    setError('');

    if (!youtubeUrl) {
      setError('⚠️ Please enter a valid YouTube link.');
      return;
    }

    setLoading(true);

    try {
      const res = await fetch('https://your-backend-url.com/dub', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          youtube_url: youtubeUrl,
          lang: lang,
        }),
      });

      if (!res.ok) {
        throw new Error('Server Error');
      }

      const data = await res.json();

      const videoId = youtubeUrl.split('v=')[1]?.split('&')[0];
      const embedUrl = `https://www.youtube.com/embed/${videoId}`;

navigate('/success', {
  state: {
    videoUrl: embedUrl,
    audioUrl: data.output_url
  }
});
    } catch (err) {
      console.error(err);
      setError('❌ Something went wrong while processing. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-xl mx-auto p-6 space-y-4 text-center">
      <h1 className="text-2xl font-bold">🎬 YouDub – Dub Any YouTube Video</h1>

      <input
        type="text"
        value={youtubeUrl}
        onChange={(e) => setYoutubeUrl(e.target.value)}
        placeholder="Paste YouTube video URL"
        className="w-full border p-2 rounded"
      />

      <select
        value={lang}
        onChange={(e) => setLang(e.target.value)}
        className="w-full border p-2 rounded"
      >
        {/* Same 20 languages */}
        <option value="te">Telugu</option>
        <option value="hi">Hindi</option>
        <option value="ta">Tamil</option>
        <option value="kn">Kannada</option>
        <option value="ml">Malayalam</option>
        <option value="gu">Gujarati</option>
        <option value="mr">Marathi</option>
        <option value="bn">Bengali</option>
        <option value="ur">Urdu</option>
        <option value="pa">Punjabi</option>
        <option value="en">English</option>
        <option value="fr">French</option>
        <option value="de">German</option>
        <option value="es">Spanish</option>
        <option value="pt">Portuguese</option>
        <option value="it">Italian</option>
        <option value="ja">Japanese</option>
        <option value="ko">Korean</option>
        <option value="ru">Russian</option>
        <option value="zh">Chinese</option>
      </select>

      <button
        onClick={handleSubmit}
        className="bg-green-600 text-white px-4 py-2 rounded w-full hover:bg-green-700"
        disabled={loading}
      >
        {loading ? '⏳ Dubbing in Progress...' : '🎧 Dub Now'}
      </button>

      {error && <p className="text-red-600 mt-2">{error}</p>}
    </div>
  );
};

export default Home;

