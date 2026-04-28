import { useState } from "react";
const requestUpgrade = async (username, plan) => {
  try {
    await axios.post("http://127.0.0.1:8000/billing/request-upgrade", {
      username: username,
      plan: plan
    });

    alert("Upgrade request sent");
  } catch (err) {
    alert("Error sending request");
  }
};


const fetchRequests = async () => {
  const res = await axios.get("http://127.0.0.1:8000/admin/billing-requests", {
    headers: { "x-admin-key": adminKey }
  });

  setRequests(res.data);
};

import axios from "axios";
import {
  LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid
} from "recharts";

export default function App() {
  const [adminKey, setAdminKey] = useState("");
  const [users, setUsers] = useState([]);
  const [chartData, setChartData] = useState([]);
const approveRequest = async (id) => {
  await axios.post("http://127.0.0.1:8000/admin/approve-request?request_id=" + id, {}, {
    headers: { "x-admin-key": adminKey }
  });

  fetchRequests();
};


<button onClick={() => {
  fetchUsers();
  fetchAnalytics();
  fetchRequests();
}}>
  Load Dashboard
</button>
  const API = "http://127.0.0.1:8000";

  // fetch users
  const fetchUsers = async () => {
    const res = await axios.get(`${API}/admin/users`, {
      headers: { "x-admin-key": adminKey }
    });
    setUsers(res.data);
  };

  // fetch analytics
  const fetchAnalytics = async () => {
    const res = await axios.get(`${API}/admin/analytics`, {
      headers: { "x-admin-key": adminKey }
    });

    const formatted = res.data.users.map(u => ({
      name: u.username,
      usage: u.usage
    }));

    setChartData(formatted);
  };

  const loadDashboard = () => {
    fetchUsers();
    fetchAnalytics();
  };

<h2>Billing Requests</h2>

{requests.map((r) => (
  <div key={r.id} style={{ marginBottom: "10px" }}>
    {r.username} → {r.plan} → {r.status}

    {r.status === "pending" && (
      <button onClick={() => approveRequest(r.id)}>
        Approve
      </button>
    )}
  </div>
))}

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>

      <h1>🚀 SaaS Admin Dashboard</h1>

      {/* ADMIN LOGIN */}
      <div>
        <input
          placeholder="Enter Admin Key"
          onChange={(e) => setAdminKey(e.target.value)}
        />
        <button onClick={loadDashboard}>Load Dashboard</button>
      </div>

      {/* USERS */}
      <h2>Users</h2>
     {users.map((u, i) => (
  <div key={i} style={{ marginBottom: "10px" }}>
    {u.username} — {u.plan}

    <button
      style={{ marginLeft: "10px" }}
      onClick={() => requestUpgrade(u.username, "pro")}
    >
      Upgrade to Pro
    </button>
  </div>
))}

      {/* CHART */}
      <h2>Usage Analytics</h2>
      <LineChart width={600} height={300} data={chartData}>
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <CartesianGrid stroke="#ccc" />
        <Line type="monotone" dataKey="usage" stroke="#8884d8" />
      </LineChart>

    </div>
  );
}
