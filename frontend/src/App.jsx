import { useState } from "react";
import axios from "axios";

const API = "https://fiaz26seo-saas-production.up.railway.app";

export default function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [topic, setTopic] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSignup = async () => {
    try {
      const res = await axios.post(`${API}/auth/signup`, {
        username,
        password,
      });

      // IMPORTANT: store API key
      localStorage.setItem("apiKey", res.data.api_key);

      alert("Signup successful");
    } catch (err) {
      console.error(err);
      alert("Signup failed");
    }
  };

  const generateBlog = async () => {
    if (!topic) return alert("Enter a topic");

    try {
      setLoading(true);

      const apiKey = localStorage.getItem("apiKey");

      const res = await axios.get(`${API}/ai/blog`, {
        params: { topic },
        headers: {
          "x-api-key": apiKey,
        },
      });

      setResult(JSON.stringify(res.data, null, 2));
    } catch (err) {
      console.error(err);
      alert("API Error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>SEO SaaS WORKING</h1>

      <h2>Signup</h2>
      <input
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button onClick={handleSignup}>Signup</button>

      <hr />

      <h2>Generate Blog</h2>

      <input
        placeholder="Topic"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <button onClick={generateBlog}>
        {loading ? "Loading..." : "Generate Blog"}
      </button>

      <pre>{result}</pre>
    </div>
  );
}
