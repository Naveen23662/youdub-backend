export default function Landing() {
  return (
    <div className="min-h-screen bg-black text-white p-4">
      <h1 className="text-3xl font-bold mb-4">Dub any YouTube video</h1>
      <input
        type="text"
        placeholder="Enter YouTube URL"
        className="w-full p-2 mb-4 rounded text-black"
      />
      <select className="w-full p-2 mb-4 rounded text-black">
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
        <option value="en">English</option>
        <option value="fr">French</option>
        <option value="de">German</option>
        <option value="es">Spanish</option>
        <option value="it">Italian</option>
        <option value="ja">Japanese</option>
        <option value="ko">Korean</option>
        <option value="ru">Russian</option>
        <option value="ar">Arabic</option>
        <option value="zh">Chinese</option>
      </select>
      <button className="bg-green-600 p-2 rounded w-full">Dub Now</button>
    </div>
  );
}

