import { useState } from "react";

export default function DubForm() {
  const [url, setUrl] = useState("");
  const [language, setLanguage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!url || !language) {
      alert("Please enter both URL and language.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/dub", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ url, language })
      });

      const data = await response.json();
      console.log("✅ Dubbed result:", data);

      // Optional: handle response, e.g., navigate to player
    } catch (error) {
      console.error("❌ Error sending data to backend:", error);
    }
  };

  const languages = [
    "Telugu", "Hindi", "Tamil", "Kannada", "Malayalam",
    "Marathi", "Bengali", "Gujarati", "Punjabi", "Urdu",
    "English", "Spanish", "French", "German", "Japanese",
    "Korean", "Chinese", "Russian", "Arabic", "Portuguese"
  ];

  return (
    <form
      onSubmit={handleSubmit}
      className="mt-12 w-full max-w-xl space-y-6 text-center"
    >
      <input
        type="text"
        placeholder="Paste YouTube URL here"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="w-full p-4 rounded-lg text-black text-lg"
      />

      <select
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
        className="w-full p-4 rounded-lg text-black text-lg"
      >
        <option value="">🌐 Select Language</option>
        {languages.map((lang, index) => (
          <option key={index} value={lang}>{lang}</option>
        ))}
      </select>

      <button
        type="submit"
        className="bg-green-500 hover:bg-green-600 text-white font-semibold py-3 px-6 rounded-lg transition duration-200"
      >
        🎙️ Dub Now
      </button>
    </form>
  );
}

