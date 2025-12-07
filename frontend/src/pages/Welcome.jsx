export default function Welcome() {
  return (
    <div className="flex flex-col items-center justify-center h-screen text-center">
      <h1 className="text-4xl font-bold">Shadow Guardian AI</h1>
      <p className="mt-3 text-lg text-gray-600">
        Your AI-powered women safety system.
      </p>

      <a href="/login">
        <button className="mt-6 px-6 py-3 bg-blue-600 text-white rounded-lg">
          Get Started
        </button>
      </a>
    </div>
  );
}
