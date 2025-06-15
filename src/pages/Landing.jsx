import React, { useState } from 'react';

const languages = [
  "Telugu", "Hindi", "Tamil", "Kannada", "Malayalam",
  "Bengali", "Gujarati", "Punjabi", "Marathi", "Urdu",
  "English", "Spanish", "French", "German", "Japanese",
  "Chinese", "Korean", "Russian", "Arabic", "Portuguese"
];

export default function Landing() {
  const [url, setUrl] = useState('');
  const [lang, setLang] = useState('Telugu');

  const handleDub = async () => {
    const response = await fetch('https://youdub-backend.onrender.com/dub', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: url, lang })
    });

    const blob = await response.blob();
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'dubbed.mp3';
    link.click();
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-[#0b0c24] to-[#1f1a4c] text-white flex items-center justify-center px-4 relative overflow-hidden">
      {/* Optional star field */}
      <div className="absolute inset-0 pointer-events-none z-0 bg-[radial-gradient(circle_at_1px_1px,#ffffff1a_1px,transparent_1px)] [background-size:20px_20px]" />

      <div className="z-10 max-w-md w-full bg-[#1e1e3f] p-8 rounded-2xl shadow-2xl border border-white/10 backdrop-blur-sm">
        <h1 className="text-2xl sm:text-3xl font-bold text-center mb-6">
          YouDub — Dub YouTube Videos in Any Language
        </h1>

        <label className="text-sm mb-1 block">YouTube URL</label>
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="https://www.youtube.com/watch?v=..."
          className="w-full px-4 py-2 mb-4 rounded bg-[#2d2d5c] text-white border border-white/20 placeholder-white/50"
        />

        <label className="text-sm mb-1 block">Select Language</label>
        <select
          value={lang}
          onChange={(e) => setLang(e.target.value)}
          className="w-full px-4 py-2 mb-6 rounded bg-[#2d2d5c] text-white border border-white/20"
        >
          {languages.map((l) => (
            <option key={l} value={l}>{l}</option>
          ))}
        </select>

        <button
          onClick={handleDub}
          className="w-full bg-indigo-500 hover:bg-indigo-600 text-white font-semibold py-2 rounded-lg transition-all"
        >
          Dub
        </button>
      </div>
    </div>
  );
}

