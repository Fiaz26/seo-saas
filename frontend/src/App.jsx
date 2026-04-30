import { useState } from "react";
import axios from "axios";

const API = "https://fiaz26seo-saas-production.up.railway.app";

export default function App() {
  const [topic, setTopic] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

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

      <button onClick={generateBlog} style={{ padding: "10px" }}>
        {loading ? "Loading..." : "Generate Blog"}
      </button>

      <pre style={{ marginTop: "20px", whiteSpace: "pre-wrap" }}>
        {result}
      </pre>
    </div>
  );
}
