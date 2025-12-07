import { Link } from "react-router-dom";

export default function Login() {
  return (
    <div className="max-w-md mx-auto p-8 bg-white shadow rounded-xl">
      <h2 className="text-3xl font-bold mb-4">Login</h2>

      <form className="flex flex-col gap-4">
        <input className="border p-3 rounded" placeholder="Email" />
        <input className="border p-3 rounded" type="password" placeholder="Password" />
        <button className="bg-blue-600 text-white py-3 rounded">Login</button>
      </form>

      <Link className="text-blue-500 mt-4 block" to="/register">
        Create an account
      </Link>
    </div>
  );
}
