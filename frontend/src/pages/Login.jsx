import { useState } from "react";
import { loginUser } from "../api";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const nav = useNavigate();
  const [form, setForm] = useState({ email: "", password: "" });
  const [msg, setMsg] = useState("");

  const submit = async () => {
    const res = await loginUser(form);

    if (res.user_id) {
      localStorage.setItem("user", JSON.stringify(res));
      nav("/dashboard");
    } else {
      setMsg(res.error);
    }
  };

  return (
    <div className="p-10 max-w-md mx-auto">
      <h2 className="text-3xl mb-5">Login</h2>

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

      <button onClick={submit} className="bg-blue-600 text-white p-2 w-full">
        Login
      </button>

      <p className="mt-4 text-center">{msg}</p>
    </div>
  );
}
