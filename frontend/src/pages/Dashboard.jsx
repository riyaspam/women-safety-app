export default function Dashboard() {
  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>

      <div className="grid md:grid-cols-3 gap-6">
        <div className="p-6 border shadow rounded-xl bg-white">
          <h3 className="font-bold mb-2">Audio Detection</h3>
          <button className="bg-blue-600 text-white px-4 py-2 rounded">
            Start Listening
          </button>
        </div>

        <div className="p-6 border shadow rounded-xl bg-white">
          <h3 className="font-bold mb-2">GPS Tracking</h3>
          <button className="bg-green-600 text-white px-4 py-2 rounded">
            Share Location
          </button>
        </div>

        <div className="p-6 border shadow rounded-xl bg-white">
          <h3 className="font-bold mb-2">Video Monitoring</h3>
          <button className="bg-red-600 text-white px-4 py-2 rounded">
            Enable Camera
          </button>
        </div>
      </div>
    </div>
  );
}
