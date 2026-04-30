const [username, setUsername] = useState("");
const [password, setPassword] = useState("");


import { useState } from "react";
import axios from "axios";

const API = "https://fiaz26seo-saas-production.up.railway.app";

export default function App() {
  const [topic, setTopic] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
return <Dashboard />;
  const generateBlog = async () => {
    if (!topic) {
      alert("Enter a topic");
      return;
    }

    try {
      setLoading(true);

      const res = await axios.get(`${API}/ai/blog`, {
        params: { topic: topic },
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
    <h1>SEO SaaS AI Engine</h1>

    {/* SIGNUP SECTION */}
    <h2>Signup</h2>
const handleSignup = async () => {
  try {
    await axios.post(`${API}/auth/signup`, {
      username,
      password,
    });

    alert("Signup successful");
  } catch (err) {
    console.error(err);
    alert("Signup failed");
  }
};
    <input
      type="text"
      placeholder="Username"
      value={username}
      onChange={(e) => setUsername(e.target.value)}
      style={{ padding: "8px", marginRight: "10px" }}
    />

    <input
      type="password"
      placeholder="Password"
      value={password}
      onChange={(e) => setPassword(e.target.value)}
      style={{ padding: "8px", marginRight: "10px" }}
    />

    <button onClick={handleSignup}>Signup</button>

    <hr style={{ margin: "20px 0" }} />

    {/* BLOG GENERATOR */}
    <h2>Generate Blog</h2>
    <input
      type="text"
      placeholder="Enter topic..."
      value={topic}
      onChange={(e) => setTopic(e.target.value)}
      style={{
        padding: "10px",
        width: "300px",
        marginRight: "10px",
      }}
    />

    <button onClick={generateBlog}>
      {loading ? "Loading..." : "Generate Blog"}
    </button>

    <pre style={{ marginTop: "20px", whiteSpace: "pre-wrap" }}>
      {result}
    </pre>
  </div>
);

 
