import { useState } from "react";
import { registerUser } from "../api";

export default function Register() {
  const [form, setForm] = useState({ name: "", email: "", password: "" });
  const [msg, setMsg] = useState("");

  const submit = async () => {
    const res = await registerUser(form);
    setMsg(res.message || res.error);
  };

  return (
    <div className="p-10 max-w-md mx-auto">
      <h2 className="text-3xl mb-5">Register</h2>

      <input
        className="border p-2 w-full mb-3"
        placeholder="Full Name"
        onChange={(e) => setForm({ ...form, name: e.target.value })}
      />

      <input
        className="border p-2 w-full mb-3"
        placeholder="Email"
        onChange={(e) => setForm({ ...form, email: e.target.value })}
      />

      <input
        type="password"
        className="border p-2 w-full mb-3"
        placeholder="Password"
        onChange={(e) => setForm({ ...form, password: e.target.value })}
      />

      <button onClick={submit} className="bg-green-600 text-white p-2 w-full">
        Register
      </button>

      <p className="mt-4 text-center">{msg}</p>
    </div>
  );
}
