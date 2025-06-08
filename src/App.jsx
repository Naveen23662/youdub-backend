import { useState } from 'react';
import './App.css';

function App() {
  const [audioUrl, setAudioUrl] = useState(null);
  const [loading, setLoading] = useState(false);
  const [detectedLang, setDetectedLang] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const url = e.target.elements.url.value.trim();
    const lang = e.target.elements.lang.value;

    if (!url) return alert('Enter a valid YouTube URL');

    setAudioUrl(null);
    setLoading(true);

    try {
      const res = await fetch('https://youdub-backend.onrender.com/dub', {
        method: 'POST',
        body: JSON.stringify({ youtube_url: url, lang }),
        headers: { 'Content-Type': 'application/json' }
      });

      if (res.ok) {
        const blob = await res.blob();
        const previewUrl = window.URL.createObjectURL(blob);
        setAudioUrl(previewUrl);
      } else {
        alert('Something went wrong!');
      }
    } catch (err) {
      alert('Error connecting to server.');
    } finally {
      setLoading(false);
    }
  };

  const handleUrlBlur = async (e) => {
    const url = e.target.value.trim();
    if (!url) return;

    try {
      const res = await fetch('https://youdub-backend.onrender.com/detect_lang', {
        method: 'POST',
        body: JSON.stringify({ youtube_url: url }),
        headers: { 'Content-Type': 'application/json' }
      });

      if (res.ok) {
        const data = await res.json();
        setDetectedLang(data.lang || '');
      }
    } catch (err) {
      console.log('Language detection failed');
    }
  };

  return (
    <div style={{ background: '#000', minHeight: '100vh', color: '#fff', fontFamily: 'Arial, sans-serif' }}>
      <header style={{ display: 'flex', alignItems: 'center', padding: '20px' }}>
        <img src="/favicon.png" alt="YouDub Logo" style={{ height: '50px', marginRight: '15px' }} />
        <h1 style={{ fontSize: '1.8rem', color: '#ff3131' }}>YouDub</h1>
      </header>

      <section style={{ textAlign: 'center', padding: '80px 20px' }}>
        <h2 style={{ fontSize: '2.5rem', marginBottom: '20px' }}>
          Dub any YouTube video in your language
        </h2>
        <p style={{ maxWidth: '600px', margin: '0 auto 30px', fontSize: '1.2rem' }}>
          Just paste a link. We'll detect the language — or pick your own.
        </p>

        <form onSubmit={handleSubmit}>
          <input
            name="url"
            type="text"
            onBlur={handleUrlBlur}
            placeholder="Enter YouTube URL"
            style={{
              padding: '10px',
              width: '280px',
              borderRadius: '6px',
              border: '1px solid #555',
              fontSize: '1rem',
              marginRight: '10px'
            }}
          />

          <select
            name="lang"
            defaultValue=""
            style={{ padding: '10px', fontSize: '1rem', marginRight: '10px' }}
          >
            <option value="" disabled>
              {detectedLang ? `Auto: ${detectedLang}` : 'Choose language'}
            </option>

            {/* Indian Languages */}
            <option value="hi">Hindi</option>
            <option value="te">Telugu</option>
            <option value="ta">Tamil</option>
            <option value="ml">Malayalam</option>
            <option value="kn">Kannada</option>
            <option value="bn">Bengali</option>
            <option value="gu">Gujarati</option>
            <option value="mr">Marathi</option>
            <option value="pa">Punjabi</option>
            <option value="ur">Urdu</option>

            {/* International Languages */}
            <option value="en">English</option>
            <option value="es">Spanish</option>
            <option value="fr">French</option>
            <option value="de">German</option>
            <option value="it">Italian</option>
            <option value="pt">Portuguese</option>
            <option value="ru">Russian</option>
            <option value="ja">Japanese</option>
            <option value="ko">Korean</option>
            <option value="zh">Chinese</option>
          </select>

          <button
            type="submit"
            style={{
              padding: '10px 20px',
              backgroundColor: '#ff3131',
              border: 'none',
              borderRadius: '6px',
              color: '#fff',
              fontSize: '1rem',
              cursor: 'pointer'
            }}
            disabled={loading}
          >
            {loading ? 'Processing...' : 'Dub Now'}
          </button>
        </form>

        {loading && (
          <div style={{ marginTop: '30px', fontSize: '1.2rem', color: '#aaa' }}>
            Generating dubbed audio...
          </div>
        )}

        {audioUrl && (
          <div style={{ marginTop: '40px' }}>
            <h3>Preview Dubbed Audio:</h3>
            <audio controls src={audioUrl} style={{ marginTop: '10px' }} />
            <br />
            <a
              href={audioUrl}
              download="dubbed_audio.mp3"
              style={{
                display: 'inline-block',
                marginTop: '20px',
                padding: '10px 20px',
                backgroundColor: '#ff3131',
                color: '#fff',
                borderRadius: '6px',
                textDecoration: 'none'
              }}
            >
              Download MP3
            </a>
          </div>
        )}
      </section>

      <footer style={{ textAlign: 'center', padding: '20px', borderTop: '1px solid #333' }}>
        © 2025 YouDub — Break the language barrier.
      </footer>
    </div>
  );
}

export default App;

