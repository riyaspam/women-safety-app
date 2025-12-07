export default function Register() {
  return (
    <div className="max-w-md mx-auto p-8 bg-white shadow rounded-xl">
      <h2 className="text-3xl font-bold mb-4">Register</h2>

      <form className="flex flex-col gap-4">
        <input className="border p-3 rounded" placeholder="Full Name" />
        <input className="border p-3 rounded" placeholder="Email" />
        <input className="border p-3 rounded" placeholder="Phone Number" />
        <input className="border p-3 rounded" type="password" placeholder="Password" />
        <button className="bg-green-600 text-white py-3 rounded">Register</button>
      </form>
    </div>
  );
}
