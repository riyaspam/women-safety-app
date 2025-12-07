import { useState } from "react";
import { uploadAudio, saveLocation } from "../api";

export default function Dashboard() {
  const user = JSON.parse(localStorage.getItem("user"));
  const [result, setResult] = useState("");

  const sendAudio = async (e) => {
    const file = e.target.files[0];
    const res = await uploadAudio(file);
    setResult(JSON.stringify(res));
  };

  const shareLocation = () => {
    navigator.geolocation.getCurrentPosition(async (pos) => {
      const payload = {
        user_id: user.user_id,
        latitude: pos.coords.latitude,
        longitude: pos.coords.longitude,
      };
      const res = await saveLocation(payload);
      setResult(JSON.stringify(res));
    });
  };

  return (
    <div className="p-10">
      <h2 className="text-3xl">Welcome, {user.name}</h2>

      <div className="mt-6">
        <h3 className="text-xl">Upload Audio</h3>
        <input type="file" accept="audio/*" onChange={sendAudio} />
      </div>

      <div className="mt-6">
        <h3 className="text-xl">Share Location</h3>
        <button onClick={shareLocation} className="bg-red-500 text-white px-4 py-2">
          Send Location
        </button>
      </div>

      <p className="mt-6 bg-gray-100 p-3 rounded">{result}</p>
    </div>
  );
}
