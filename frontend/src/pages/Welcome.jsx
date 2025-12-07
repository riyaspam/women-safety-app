import { Link } from "react-router-dom";

export default function Welcome() {
  return (
    <div className="p-10 text-center">
      <h1 className="text-4xl font-bold mb-4">Shadow Guardian AI</h1>
      <p className="text-lg mb-8">Your Personal Safety Companion</p>
      <Link to="/login" className="bg-blue-600 text-white px-6 py-3 rounded-xl">
        Continue
      </Link>
    </div>
  );
}
